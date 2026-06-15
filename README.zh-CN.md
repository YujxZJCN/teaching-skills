[English](README.md) | 简体中文

# Claude Code 教学技能套件（Teaching Skills）

一套面向高校教师的完整 Claude Code 技能套件，覆盖教学全生命周期：**设计 → 构建 → 评估 → 实施 → 反思 → 改进**。

15 个技能 · 84 种模式 · 71 个智能体协同 · 2 道质量门控 · 1 份课程护照（Course Passport）

> **AI 是你的助教，不是你的替代者。** 这套工具不会替你教书。它接手的是结构性工作和琐碎的苦活——起草学习成果、先建蓝图再出试卷、审查教学一致性、排版教学大纲、为评教意见做编码归类——好让你专注于真正非你不可的事情：精通你的学科、了解你的学生、判断什么才重要。每一个有分量的决定，都会经过检查点，由你亲自拍板。

本套件的架构受 [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)
（Cheng-I Wu）启发——它是本套件在科研侧的姊妹项目。如果你同时也写论文，两者可以衔接：
teaching-reflector 的 SoTL（教学学术）模式可直接交棒给 ARS 的 deep-research 与
academic-paper 技能。

## 安装

**插件方式（推荐）：**

```text
/plugin marketplace add YujxZJCN/teaching-skills
/plugin install teaching-skills
```

**手动安装：**克隆本仓库，将各技能目录软链接到
`~/.claude/skills/`（或项目内的 `.claude/skills/`）。

**验证安装：**在包含 `course_passport.yaml` 的目录下运行 `/ts-status`，或直接说一句：
*「为 60 名大二学生设计一门关于 X 的新课程。」*

## 技能一览

| 技能 | 阶段 | 功能说明 |
|-------|-------|--------------|
| **course-designer**（课程设计） | 1 设计 | 反向设计（逆向教学设计）：按布卢姆分类法标注的学习成果 → 评估方案 → 学期主线 → 教学大纲。提供苏格拉底式对话模式，助你从一张白纸起步。 |
| **lesson-builder**（课时构建） | 2 构建 | 课时计划、讲义、幻灯片提纲、主动学习活动、教学案例、讨论引导、翻转课堂形式。 |
| **assessment-architect**（考核设计） | 3 评估 | 蓝图先行的考试与测验、评分量表、TILT（透明作业设计）项目任务书、面向 AI 时代的诚信韧性审查、考后试题分析。 |
| **student-mentor**（学生指导） | 4 实施 | 反馈撰写、学业困难学生干预方案、推荐信、棘手邮件、学业指导与导师计划。 |
| **submission-auditor**（作业审查） | 4 实施 | 规范驱动的作业提交检查：将你的模板/要求编译为可核查的规范，对提交（单份或批量）进行带证据定位的审查，生成每生反馈报告 + 全班共性问题报告。 |
| **teaching-reflector**（教学反思） | 5 反思 | 正视偏差的评教分析、期中学生反馈、同行听课、教学档案与教学陈述、SoTL 研究设计。 |
| **teaching-pipeline**（教学流水线） | 编排器 | 基于课程护照运行完整教学生命周期，含两道不可跳过的门控和每周实施循环。 |

**扩展技能** —— 制作、运维与合规层；每个技能都可独立使用，流水线也会按需调度它们：

| 技能 | 阶段 | 功能说明 |
|-------|-------|--------------|
| **deck-studio**（幻灯片工坊） | 2 | 真正渲染出幻灯片成品（Marp/Pandoc/Beamer/python-pptx），全课程统一主题、代码生成的图表、讲义、海报。强制执行无障碍要求，绝不伪造渲染结果。 |
| **lab-forge**（实验锻造） | 2 | 可执行的 STEM 教学制品：实验包、每生独立且真值可还原的合成数据集、起步代码、自动评分器、经实际运行验证的参考答案。 |
| **media-scripter**（媒体脚本） | 2 | 录播媒体脚本创作：6–9 分钟微课讲稿、分镜脚本、系列节目、字幕/逐字稿清理、音频版改编。 |
| **course-publisher**（课程发布） | 4 | 基于课程护照生成面向学生的沟通材料：通知公告、每周邮件、静态课程网站、LMS 打包、持续更新的 FAQ。仅产出草稿——事实全部可溯源，绝不杜撰。 |
| **ta-coordinator**（助教协调） | 4 | 教学团队运营：助教手册、评分校准会、按工时均衡的任务分配、会议议程、跨助教一致性检查（不做排名榜）。 |
| **accreditation-mapper**（认证映射） | 1 | 面向专业认证（工程教育认证）：学习成果 → 专业培养目标 → 认证标准的对应矩阵（含证据状态）、证据包、差距分析、以诚实为底线的自评报告草稿。 |
| **bilingual-courseware**（双语课件） | 支持 | 术语严格受控的双语教学材料：经教师确认的术语表、受术语表约束的翻译、双语版本同步、一致性审查。 |
| **cohort-analyst**（学情分析） | 支持 | 学情分析：课前诊断问卷设计、由能力清单/问卷结果生成班级学情画像、课时校准、循证分组。只写入聚合数据——涉及具体学生一律转交 student-mentor。 |

## 流水线

```
Stage 0 CONTEXT  → 初始化课程护照                                🧑
Stage 1 DESIGN   → course-designer                              🧑
Gate 1.5 ALIGNMENT — 一致性建构审查                              ✓ 机器校验 + 教师确认
Stage 2 BUILD    → lesson-builder（默认按需即时构建）              🧑
Stage 3 ASSESS   → assessment-architect + 学术诚信审查            🧑
Gate 3.5 QUALITY — AI 诚信、透明度、UDL、工作量                    ✓ 机器校验 + 教师确认
Stage 4 DELIVER  → 每周循环：教学材料 · 学生指导 · 作业审查 · 期中反馈
Stage 5 REFLECT  → teaching-reflector 评教分析                    🧑
Stage 6 IMPROVE  → 迭代记录 → 下学期重新进入 Stage 1
```

🧑 = 教师检查点（由你决定） · ✓ = 确定性门控，随后由你确认

把这一切串在一起的，是两个核心理念：

- **课程护照**（`shared/course_passport_schema.md`）——一份 YAML 文件，是课程的唯一事实来源。
  学习成果、评估方案、教学进度、课程政策、门控结论、制品台账、迭代历史，尽收其中。
  状态保存在护照里而非对话里：任何新会话都能从护照恢复进度。同时，每个技能在没有
  护照时也都能独立工作。
- **把一致性建构变成机器检查**——对齐门控（Alignment Gate）在任何构建开始之前，
  先验证「学习成果—教学活动—评估」三角是否闭合；质量门控（Quality Gate）在学生
  看到材料之前，验证已构建的制品是否透明（TILT）、无障碍（UDL）、诚信自洽
  （AI 时代），且工作量在常人可承受的范围内。

## 示例展示：实际产出长什么样

**[查看完整示例 →](examples/showcase/)** —— 一门演示课程（CS 304 机器学习导论，90 人）
的全套制品：填写完整的课程护照、教学大纲、带「已驳回警告」记录的对齐门控报告、
课时计划与课堂活动单、含样题和详解答案的考试蓝图，以及促成课程项目重新设计的
AI 诚信审查报告。数据均为合成并明确标注——但每份文件都严格遵守套件自身的规则，
你可以在安装之前先判断产出质量。

## 快速上手

```
# Full lifecycle
"I'm teaching a new course on environmental economics next fall — run the full pipeline"

# Blank page
"Guide me — I know my field but I've never designed a course"          → socratic

# Single artifacts
/ts-outcomes  /ts-syllabus  /ts-lesson  /ts-exam  /ts-rubric  /ts-letter  /ts-evals

# Mid-entry
"I already have a syllabus, build me week 3's materials"
"Semester's over, here are my student evaluations"                      → eval-analysis

# Status
/ts-status    "What's next for my course?"
```

完整的首次使用示例见 [QUICKSTART.md](QUICKSTART.md)，全部 84 种模式见
[MODE_REGISTRY.md](MODE_REGISTRY.md)。

## 设计原则

1. **教师是机长。** 每个阶段都设有检查点；「替你做出的关键决定」一律明示，绝不
   埋没；你说一句「直接继续」也会被尊重（`shared/checkpoint_protocol.md`）。
2. **循证的默认方案，教师的最终裁量。** 各项建议均援引
   `shared/pedagogy_foundations.md`（反向设计、一致性建构、主动学习、提取练习、
   TILT、UDL、认知负荷、反馈研究）。当你否决某条原则时，该决定会被记录在案，
   且不会被反复追问。
3. **绝不虚构背景信息。** 学习者画像为空 → 技能会主动询问。涉及学校规章政策 →
   以 `[NEEDS PROFESSOR INPUT]` 标记，绝不填入貌似合理的内容。生成材料中不确定的
   学科论断 → 加 `[VERIFY]` 标记。
4. **涉及具体个人的输出严格基于证据。** 反馈、推荐信、干预方案只使用你提供的
   材料——绝不杜撰任何轶事——并且一律以「发送前请核实」的提醒结尾。学生数据
   永远不会写入课程护照。
5. **以设计保障诚信，而非依赖检测。** AI 时代学术诚信模型
   （`shared/ai_era_integrity.md`）采用按作业划分的政策层级与结构化的诚信韧性
   模式。本套件不依赖任何 AI 检测工具。
6. **契约由机器校验。** 课程护照有正式的 JSON Schema
   （`shared/course_passport.schema.json`）和配套校验器：`scripts/check_passport.py`
   （交叉引用不变量——ID 双向映射、权重总和）与 `scripts/check_alignment_gate.py`
   （对齐门控以确定性脚本执行，而非依赖模型解读）。CI 在每次推送时运行校验器和
   变异测试套件。
7. **诚实地解读证据。** 学生评教被视为带有偏差的小样本证据，反映的是学生体验
   ——做主题分析、多源印证、并附限定说明——而不是当作一个教学质量分数。

## 仓库结构

```
course-designer/        SKILL.md + agents/ + references/ + templates/
lesson-builder/         〃
assessment-architect/   〃
student-mentor/         〃
submission-auditor/     〃
teaching-reflector/     〃
teaching-pipeline/      SKILL.md + agents/ + references/
deck-studio/            扩展技能，目录结构同上
lab-forge/              〃
media-scripter/         〃
course-publisher/       〃
ta-coordinator/         〃
accreditation-mapper/   〃
bilingual-courseware/   〃
cohort-analyst/         〃
shared/                 课程护照 schema（文档 + JSON Schema）· 教学法基础 · 门控协议
                        · AI 时代学术诚信 · 检查点协议
scripts/                check_passport.py · check_alignment_gate.py · build_dashboard.py · 注册表一致性检查
tests/                  校验器测试套件（黄金样例 + 变异测试）
commands/               /ts-* 斜杠命令
docs/                   ARCHITECTURE.md
.claude-plugin/         插件与插件市场清单
skills/                 供插件自动发现的符号链接
```

## 语言支持

英文与简体中文触发关键词默认内置；基于意图的模式（苏格拉底式设计、中途接入路由）
适用于任何语言。在技能的 `description` frontmatter 中加入你所用语言的关键词，可提升
触发匹配效果。

## 跨工具可移植性

本仓库是 **Claude Code** 发行版（原生技能、`/plugin` 安装、`/ts-*` 斜杠命令）。
整套工具分三层，可移植程度不同：

- **技能本体**（`SKILL.md` 内容）遵循 Anthropic 的 Agent Skills 格式，也可通过
  Skills 功能在其他 Claude 界面（claude.ai、Claude 桌面端、IDE 插件）中使用。
- **Python 工具链**（`scripts/`、JSON Schema、课程仪表盘）完全与工具无关——
  任何装有 `python3` 的终端都能运行，无需 AI。
- **插件封装**（插件市场安装、斜杠命令）是 Claude Code 专属的。

针对 **OpenAI Codex CLI**，由本仓库的 `scripts/build_codex.py` 生成姊妹发行版，
发布于 [`YujxZJCN/teaching-skills-codex`](https://github.com/YujxZJCN/teaching-skills-codex)
——把整套工具打包为单个 Codex 技能并提供 `ts-*` 别名。它是构建产物
（自动生成、绝不手改），因此永远不会与本源仓库产生偏差。

## 许可证

MIT。本项目架构（技能/智能体/门控/护照模式）受
[Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)
启发（CC BY-NC 4.0），未复制其内容。
