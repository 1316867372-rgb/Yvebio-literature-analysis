# Biomed Literature Analysis Skill

> 学术文献PDF完整拆解工具 —— 输入一篇英文学术论文PDF，自动产出8模块中文拆解文档、提取内嵌Fig图、生成研究流程图谱。

适用领域：生物医学（肿瘤、信号通路、细胞表型类研究）。

---

## 产出物

| 产物 | 格式 | 说明 |
|------|------|------|
| 8模块拆解文档 | `.docx` | 5000-8000字，含嵌入式图表 |
| Fig图独立提取 | `.png` | 从PDF逐Fig拆出高清图片 |
| 研究流程图谱 | `.png` | 4:3横版信息图，极简白底线条风格 |
| AI绘图提示词 | `.txt` | 可导入其他生图工具 |

---

## 8模块结构

| 一、关键要素 | 五、研究流程 |
|:---|:---|
| 二、科学假设 | 六、数据解读 |
| 三、逻辑关系 | 七、论证规范 |
| 四、知识背景 | 八、套路归纳 |

---

## 快速开始

### 1. 安装 Skill

将 `biomed-literature-analysis.skill` 放入 Agent（比如Openclaw、WorkBuddy等) skills 目录。

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 准备文件

把 PDF 文件和 `参考要求/` 文件夹放在同一目录下（参考规范需14篇全部就位）。

### 4. 触发拆解

在 WorkBuddy 中输入：

```
拆解文献 "你的论文.pdf"
```

---

## （可选）配置研究流程图自动生成

设置环境变量指向包含 `generate_infographic.py` 的目录：

```bash
# Windows
set INFOGRAPHIC_TOOL_DIR=D:\YourPath\infographic-tool

# macOS / Linux
export INFOGRAPHIC_TOOL_DIR=/path/to/infographic-tool
```

不配置则跳过此步，仅输出 AI 绘图提示词 txt。

---

## 目录结构

```
Yvebio-literature-analysis/
├── SKILL.md                              # Skill 定义
├── biomed-literature-analysis.skill      # 打包文件
├── requirements.txt                      # Python 依赖
├── scripts/
│   ├── extract_figures.py                # Fig图提取
│   ├── generate_infographic.py           # 信息图生成
│   └── insert_figures.py                 # 图表嵌入docx
├── references/
│   └── analysis_guide.md                 # 8模块详细要求
└── 文献拆解Skill使用说明书.md
```

---

## 常见问题

见 [文献拆解Skill使用说明书.md](./文献拆解Skill使用说明书.md)。

---

## 许可

MIT License
