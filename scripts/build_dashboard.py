#!/usr/bin/env python3
"""Course Dashboard generator.

Renders a Course Passport into a single self-contained HTML file the professor
can open locally — a complete overview of the course design and every generated
resource, with clickable links to artifact files on disk.

Usage:
  python3 scripts/build_dashboard.py path/to/course_passport.yaml [-o out.html]

Output defaults to course_dashboard.html next to the passport, so relative
artifact links resolve. Deterministic apart from the generation timestamp:
regenerate freely at every checkpoint — the passport is the source of truth,
the dashboard is a build product.

Exit codes: 0 = written · 2 = error
"""

import argparse
import datetime
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_passport import load_passport, crossref_findings  # noqa: E402
from check_alignment_gate import gate_findings, suppress_dismissed  # noqa: E402

e = html.escape

BLOOM = {"remember": "#64748b", "understand": "#0891b2", "apply": "#2563eb",
         "analyze": "#7c3aed", "evaluate": "#c026d3", "create": "#dc2626"}
GATE = {"pass": ("#16a34a", "pass"), "fail": ("#dc2626", "fail"),
        "not_run": ("#94a3b8", "not run")}
SEV = {"BLOCK": "#dc2626", "WARN": "#d97706", "NOT_EVALUABLE": "#64748b"}

CSS = """
:root{--ink:#1e293b;--mut:#64748b;--line:#e2e8f0;--bg:#f8fafc;--acc:#2563eb}
*{box-sizing:border-box}body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,
"Segoe UI","PingFang SC","Noto Sans",sans-serif;color:var(--ink);background:var(--bg)}
header{background:#fff;border-bottom:1px solid var(--line);padding:28px 32px}
h1{margin:0 0 4px;font-size:22px}h2{font-size:16px;margin:0 0 12px}
.sub{color:var(--mut)}.chips{margin-top:10px}
.chip{display:inline-block;background:var(--bg);border:1px solid var(--line);
border-radius:999px;padding:2px 10px;margin:2px 4px 2px 0;font-size:12.5px}
nav{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);
padding:8px 32px;z-index:9}nav a{color:var(--acc);text-decoration:none;margin-right:16px;
font-size:13.5px}main{max-width:1080px;margin:0 auto;padding:24px 32px 64px}
section{background:#fff;border:1px solid var(--line);border-radius:10px;
padding:20px 24px;margin:18px 0}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{text-align:left;color:var(--mut);font-weight:600;border-bottom:2px solid var(--line);
padding:6px 8px}td{border-bottom:1px solid var(--line);padding:7px 8px;vertical-align:top}
.b{display:inline-block;color:#fff;border-radius:4px;padding:1px 7px;font-size:11.5px;
font-weight:600}.tag{display:inline-block;background:#eef2ff;color:#3730a3;
border-radius:4px;padding:1px 6px;font-size:11.5px;margin:1px 2px}
.bar{background:var(--line);border-radius:4px;height:8px;min-width:120px}
.bar i{display:block;height:8px;border-radius:4px;background:var(--acc)}
.ok{color:#16a34a}.miss{color:#dc2626;font-weight:600}
.dim{color:var(--mut);font-size:12.5px}
a.f{color:var(--acc);text-decoration:none}a.f:hover{text-decoration:underline}
footer{color:var(--mut);font-size:12.5px;text-align:center;padding:18px}
.note{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;
padding:10px 14px;font-size:13px;margin-top:10px}
"""


def badge(text, color):
    return f'<span class="b" style="background:{color}">{e(str(text))}</span>'


def file_cell(base, ref):
    if not ref:
        return '<span class="dim">—</span>'
    p = (base / ref)
    if p.exists():
        return f'<a class="f" href="{e(ref)}">{e(ref)}</a>'
    return f'<span class="miss" title="file not found next to the passport">{e(ref)} ⚠ missing</span>'


def sec_outcomes(p):
    rows = []
    for o in p.get("learning_outcomes") or []:
        bl = o.get("bloom_level", "")
        rows.append(
            f"<tr id='{e(o['id'])}'><td><b>{e(o['id'])}</b></td>"
            f"<td>{e(o.get('statement',''))}</td>"
            f"<td>{badge(bl, BLOOM.get(bl, '#64748b'))}</td>"
            f"<td>{''.join(f'<span class=tag>{e(x)}</span>' for x in o.get('assessed_by') or []) or '<span class=miss>unassessed</span>'}</td>"
            f"<td>{''.join(f'<span class=tag>{e(x)}</span>' for x in o.get('taught_in') or []) or '<span class=miss>untaught</span>'}</td></tr>")
    return ("<section id='outcomes'><h2>Learning outcomes</h2><table>"
            "<tr><th>id</th><th>statement</th><th>Bloom</th><th>assessed by</th>"
            "<th>taught in</th></tr>" + "".join(rows) + "</table></section>")


def sec_assessments(p, base):
    rows = []
    for a in p.get("assessment_plan") or []:
        w = a.get("weight") or 0
        air = a.get("ai_resilience", "not_reviewed")
        air_color = {"reviewed": "#16a34a", "redesigned": "#2563eb"}.get(air, "#d97706")
        rows.append(
            f"<tr id='{e(a['id'])}'><td><b>{e(a['id'])}</b></td><td>{e(a.get('title',''))}"
            f"<div class=dim>{e(a.get('type',''))} · {e(str(a.get('week') or ''))}</div></td>"
            f"<td><div class=bar><i style='width:{min(w,100)}%'></i></div>"
            f"<span class=dim>{w}%</span></td>"
            f"<td>{''.join(f'<span class=tag>{e(x)}</span>' for x in a.get('outcomes_assessed') or [])}</td>"
            f"<td>{badge(air, air_color)}</td>"
            f"<td>{file_cell(base, a.get('artifact_ref'))}</td></tr>")
    return ("<section id='assessments'><h2>Assessment plan</h2><table>"
            "<tr><th>id</th><th>assessment</th><th>weight</th><th>outcomes</th>"
            "<th>AI integrity</th><th>artifact</th></tr>" + "".join(rows) + "</table></section>")


def sec_schedule(p, base):
    rows = []
    for w in p.get("schedule") or []:
        refs = "".join(f"<div>{file_cell(base, r)}</div>" for r in w.get("artifact_refs") or []) \
               or '<span class="dim">none yet</span>'
        tag = ' <span class="tag">logistics</span>' if w.get("tag") == "logistics" else ""
        rows.append(
            f"<tr><td><b>{e(w['id'])}</b></td><td>{e(w.get('topic',''))}{tag}</td>"
            f"<td>{''.join(f'<span class=tag>{e(x)}</span>' for x in w.get('outcomes') or [])}</td>"
            f"<td>{''.join(f'<span class=tag>{e(x)}</span>' for x in w.get('assessments_due') or [])}</td>"
            f"<td>{refs}</td></tr>")
    return ("<section id='schedule'><h2>Schedule &amp; week resources</h2><table>"
            "<tr><th>week</th><th>topic</th><th>outcomes</th><th>due</th>"
            "<th>resources</th></tr>" + "".join(rows) + "</table></section>")


def sec_artifacts(p, base):
    rows = []
    for a in p.get("artifacts") or []:
        ok = '<span class="ok">✓ confirmed</span>' if a.get("confirmed_by_professor") \
            else '<span class="dim">pending confirmation</span>'
        rows.append(
            f"<tr><td>{file_cell(base, a.get('path'))}</td><td>{e(a.get('type',''))}</td>"
            f"<td>{e(str(a.get('produced_by','')))}</td><td>{e(str(a.get('stage','')))}</td>"
            f"<td>{ok}</td></tr>")
    return ("<section id='artifacts'><h2>Artifacts ledger</h2><table>"
            "<tr><th>file</th><th>type</th><th>produced by</th><th>stage</th>"
            "<th>status</th></tr>" + "".join(rows) + "</table></section>")


def sec_gates(p):
    out = ["<section id='gates'><h2>Gates</h2>"]
    for name, gate in (p.get("gates") or {}).items():
        color, label = GATE.get((gate or {}).get("status", "not_run"), GATE["not_run"])
        out.append(f"<p><b>{e(name.replace('_', ' '))}</b> {badge(label, color)} "
                   f"<span class=dim>last run: {e(str((gate or {}).get('last_run') or '—'))}</span></p>")
        fnds = (gate or {}).get("findings") or []
        if fnds:
            rows = []
            for f in fnds:
                st = (f'<span class=dim>dismissed: {e(f["dismissed"])}</span>'
                      if f.get("dismissed") else "open")
                rows.append(
                    f"<tr><td>{badge(f.get('severity',''), SEV.get(f.get('severity'), '#64748b'))}</td>"
                    f"<td><b>{e(f.get('check_id',''))}</b></td><td>{e(f.get('detail',''))}</td>"
                    f"<td>{st}</td></tr>")
            out.append("<table><tr><th></th><th>check</th><th>finding</th>"
                       "<th>status</th></tr>" + "".join(rows) + "</table>")
    # live re-check, so the dashboard never shows a stale green
    live, _ = gate_findings(p)
    live, _ = suppress_dismissed(live, p)
    live += [f for f in crossref_findings(p)]
    if live:
        items = "".join(f"<li>{badge(f['severity'], SEV.get(f['severity'], '#64748b'))} "
                        f"<b>{e(f['check_id'])}</b> {e(f['detail'])}</li>" for f in live)
        out.append(f"<div class=note><b>Live re-check found open issues "
                   f"(passport changed since the gate last ran?):</b><ul>{items}</ul></div>")
    else:
        out.append('<p class="dim">Live re-check: structure and alignment checks are clean right now.</p>')
    out.append("</section>")
    return "".join(out)


def sec_misc(p):
    wa = p.get("workload_audit") or {}
    wl = (f"estimated <b>{e(str(wa.get('estimated_hours_per_week')))}</b> h/week "
          f"vs target {e(str(wa.get('credit_hour_target')))} — "
          f"{badge(wa.get('status', 'not_audited'), '#2563eb' if wa.get('status') == 'within_range' else '#d97706')}")
    its = "".join(
        f"<li><b>{e(i.get('term',''))}</b>: "
        f"{'; '.join(e(c) for c in i.get('changes') or [])}"
        f"<div class=dim>{e(i.get('evidence',''))}</div></li>"
        for i in p.get("iteration_history") or []) or "<li class=dim>none yet</li>"
    lp = p.get("learner_profile") or {}
    kd = "".join(f"<li>{e(d)}</li>" for d in lp.get("known_difficulties") or []) or "<li class=dim>—</li>"
    return (f"<section id='more'><h2>Workload, learners &amp; iteration</h2>"
            f"<p>{wl}</p><p><b>Known difficulties</b> (learner profile):</p><ul>{kd}</ul>"
            f"<p><b>Iteration history:</b></p><ul>{its}</ul></section>")


def build(passport_path, out_path=None):
    passport_path = Path(passport_path)
    p = load_passport(passport_path)
    base = passport_path.parent
    out = Path(out_path) if out_path else base / "course_dashboard.html"

    c = p.get("course") or {}
    n_art = len(p.get("artifacts") or [])
    chips = "".join(f'<span class="chip">{e(x)}</span>' for x in [
        f"{len(p.get('learning_outcomes') or [])} outcomes",
        f"{len(p.get('assessment_plan') or [])} assessments",
        f"{len(p.get('schedule') or [])} weeks",
        f"{n_art} artifacts",
        str(c.get("modality") or ""), f"{c.get('class_size') or '?'} students"] if x)

    body = (sec_gates(p) + sec_outcomes(p) + sec_assessments(p, base)
            + sec_schedule(p, base) + sec_artifacts(p, base) + sec_misc(p))
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(c.get('code',''))} — Course Dashboard</title><style>{CSS}</style></head><body>
<header><h1>{e(c.get('code',''))}: {e(c.get('title',''))}</h1>
<div class="sub">{e(c.get('discipline',''))} · {e(c.get('level',''))}</div>
<div class="chips">{chips}</div></header>
<nav><a href="#gates">Gates</a><a href="#outcomes">Outcomes</a>
<a href="#assessments">Assessments</a><a href="#schedule">Schedule</a>
<a href="#artifacts">Artifacts</a><a href="#more">More</a></nav>
<main>{body}</main>
<footer>Generated {e(stamp)} from {e(passport_path.name)} ·
regenerate anytime: <code>python3 scripts/build_dashboard.py {e(str(passport_path.name))}</code> ·
Teaching Skills</footer></body></html>"""
    out.write_text(doc, encoding="utf-8")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("passport")
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args(argv)
    try:
        out = build(args.passport, args.out)
    except Exception as ex:
        print(f"error: {type(ex).__name__}: {ex}", file=sys.stderr)
        return 2
    print(f"dashboard written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
