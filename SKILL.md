---
name: biomed-literature-analysis
description: 学术文献PDF完整拆解。将英文学术PDF按要求拆解为8模块中文文档、提取内嵌Fig图、生成研究流程图谱。触发词：文献拆解、拆解文献、分析文献、解读文献、PDF拆解、做文献拆解。
---

# 学术文献PDF拆解

完整流程：读取全部参考规范 → 提取PDF全文 → 分析撰写8模块文档(5000-8000字) → 提取研究流程生成信息图 → 拆出Fig → 嵌入文档。

## 输出质量基线

- 8模块文档纯文本目标 5000-8000 字
- 数据解读每Fig逐子图详读，不可一句话概括
- 知识背景每项至少3-5个自然段
- 套路归纳优缺点各至少5条，每条附具体分析

## 环境准备

```bash
pip install -r requirements.txt
```

### 可选：信息图生成

第5步研究流程图需要外部生图工作流工具。如未配置，该步骤自动跳过，不影响其余产出。

配置方法：设置环境变量指向包含 `generate_infographic.py`（接收 `process_infographic_task` 的模块）的目录：

```bash
set INFOGRAPHIC_TOOL_DIR=D:\YourPath\infographic-tool
```

该工具需自行搭建，依赖 Dify 工作流 API 或 OpenAI API。不配置此变量时，skill 仅生成绘图提示词 txt 文件，用户可手动导入其他生图工具使用。

## 工作流程

### 第1步：读取全部参考规范

用 Python 遍历 PDF 源文件所在目录及子目录 `参考要求/`，提取所有 `.docx` 全文（含表格）。**不可遗漏** `参考要求/` 子目录下的文件。

### 第2步：提取PDF全文

用 pdfplumber 逐页提取文本。

### 第3步：撰写8模块拆解文档

用 `python-docx` 生成 `.docx`，保存到 PDF 同目录。文件名：`{PDF文件名}_文献拆解_{主变量}_{解读者}.docx`。

严格按照参考规范（尤其论证规范1-3）分析。各模块详细要求见 `references/analysis_guide.md`。

### 第4步：提取研究流程 → 生成信息图

将"五、研究流程"的骨架写成 AI 绘图提示词 txt，保存到 PDF 同目录。命名：`{PDF文件名}_研究流程_AI绘图提示词.txt`。

要求：极简白底线条风格、4:3、中文，只保留核心逻辑链+关键词，不添加数据。

```bash
python scripts/generate_infographic.py "\\path\to\xxx_研究流程_AI绘图提示词.txt"
```

如未配置生图工具，此步自动跳过。

### 第5步：从PDF拆出Fig图

```bash
python scripts/extract_figures.py "\\path\to\xxx.pdf"
```

输出到同目录，命名 `{PDF文件名} Fig.1.png` ~ `Fig.N.png`。

### 第6步：Fig图+流程图嵌入文档

```bash
python scripts/insert_figures.py "\\path\to\xxx_文献拆解_xxx.docx"
```

## 注意事项

- 所有输出与源 PDF 同一目录
- 因果逻辑：先辨主次、再分上下；两两调控、三三回复
- 论证规范：理论与实际逐项对照，标注完成/缺失
- 交互论证：双向互拉、位点解析、交互必要性
- 文本不可偷懒缩减
