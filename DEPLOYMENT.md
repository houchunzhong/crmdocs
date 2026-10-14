# CRM 文档站 & RAG 知识库 — 部署与维护指南

> 版本：v1.0 | 最后更新：2026-07-09

---

## 一、概述

本项目包含两个子系统，共用同一份 Markdown 文档源：

| 系统 | 用途 | 面向对象 |
|------|------|----------|
| **Docsify 文档站** | 在线文档浏览（`index.html` + CDN 渲染） | 人类用户 |
| **RAG 知识库** | BM25 关键词检索 + AI 问答 | AI / 自动化 |

两者零冲突，Docsify 是前端渲染层，RAG 是后端检索层。

---

## 二、目录结构

```
crmdocs/
├── index.html              # Docsify 入口（CDN 加载 docsify 运行时）
├── _sidebar.md             # 文档站侧边栏导航
├── _navbar.md              # 文档站顶部导航
├── README.md               # 项目说明
├── images/                 # 文档引用的截图资源
├── md/                     # 英文文档（39 个 .md）
├── zh-cn/                  # 中文文档（43 个 .md）
├── rag/                    # RAG 知识库代码
│   ├── __init__.py
│   ├── __main__.py         # python -m rag 入口
│   ├── config.py           # 路径、切分参数、模型配置
│   ├── chunker.py          # Markdown 章节切分器
│   ├── retriever.py        # BM25 + 混合检索（RRF 融合）
│   ├── embeddings.py       # embedding / rerank 模型封装（懒加载）
│   ├── download_models.py  # 从 ModelScope 下载 bge 模型
│   ├── ingest.py           # 摄入脚本：扫描 → 切分 → 建索引 → 向量化
│   ├── query.py            # 查询脚本：混合检索 + rerank 精排 top-5
│   ├── llm.py              # LLM 调用封装（Anthropic 兼容 API）
│   ├── ask.py              # CLI 问答：检索 + LLM 生成
│   └── api.py              # Flask API：Web 问答页面 + POST /ask + GET /health
├── rag_data/               # 运行时生成（已加入 .gitignore）
│   ├── chunks.json         # 切分后的文档块（~474 个段落）
│   ├── bm25_index.pkl      # BM25 序列化索引
│   ├── vectors.npy         # 向量索引（bge-m3, 1024 维）
│   └── models/             # 下载的 embedding / rerank 模型
├── .gitignore              # 排除 rag_data/、__pycache__/ 等
└── .obsidian/              # Obsidian 编辑器配置（可选）
```

### 关键文件说明

| 文件 | 作用 | 是否需要修改 |
|------|------|-------------|
| `index.html` | Docsify 配置（主题色、插件、侧边栏折叠层级等） | 改配置时 |
| `_sidebar.md` | 文档站侧边栏目录 | 新增/删除文档时 |
| `_navbar.md` | 文档站顶部导航 | 改导航时 |
| `rag/config.py` | RAG 路径、章节切分正则、模型路径 | 文档结构变化时 |
| `rag/chunker.py` | 按 `##` 章节标题切分 MD 文件 | 通常不需要 |
| `rag/retriever.py` | BM25 + 向量混合检索（RRF） | 通常不需要 |
| `rag/embeddings.py` | embedding / rerank 模型封装 | 通常不需要 |
| `rag/download_models.py` | 从 ModelScope 下载模型 | 首次部署时 |
| `rag/ingest.py` | 摄入入口 | 通常不需要 |
| `rag/query.py` | 查询入口 | 通常不需要 |
| `rag/llm.py` | LLM 调用封装 | 换模型/换 API 时 |
| `rag/ask.py` | CLI 问答入口 | 通常不需要 |
| `rag/api.py` | HTTP 问答服务 | 通常不需要 |

---

## 三、环境依赖

### Docsify 文档站

零依赖。Docsify 通过 CDN 在浏览器端加载，只需一个静态文件服务器。

### RAG 知识库

- **Python 3.9+**（当前环境：3.14.5）
- **依赖**：
  - `sentence-transformers` — 加载 bge-m3 embedding 与 bge-reranker-v2-m3 精排模型
  - `modelscope` — 从国内镜像下载模型（HuggingFace 被墙时用）
  - `torch`（CPU 版即可）、`numpy`
  - `anthropic`、`flask` — AI 问答（`ask.py` / `api.py`，可选）
- **模型文件**：通过 `python -m rag.download_models` 下载到 `rag_data/models/`（约 3.3 GB）

---

## 四、部署方式

### 4.1 启动 Docsify 文档站

**方式 A：docsify-cli（推荐）**
```bash
npm i -g docsify-cli
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
docsify serve . --port 3000
```

**方式 B：任意静态服务器**
```bash
# Python
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m http.server 3000

# Node.js
npx serve . -p 3000
```

访问 `http://localhost:3000` 即可浏览文档站。

### 4.2 构建 RAG 索引

#### 步骤 0：下载模型（仅首次）

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.download_models
```

从 ModelScope 下载 bge-m3 与 bge-reranker-v2-m3 到 `rag_data/models/`（约 3.3 GB）。
若网络可直连 HuggingFace，也可改为手动放置模型文件到对应目录。

#### 步骤 1：安装依赖

```bash
pip install sentence-transformers modelscope torch numpy
```

#### 步骤 2：构建索引

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.ingest
```

输出示例：
```
Ingesting CRM documentation...
  Scanning .../md and .../zh-cn...
  Found 474 sections across documents.
  Saved chunks to .../rag_data/chunks.json
  Building BM25 index...
  Saved BM25 index to .../rag_data/bm25_index.pkl
  Embedding 474 chunks with bge-m3...
  Saved vector index (474, 1024) to .../rag_data/vectors.npy
Done. 236 English + 238 Chinese chunks indexed.
```

### 4.3 查询 RAG 知识库

```bash
# 中文查询
python -m rag.query "如何配置佣金方案？"

# 英文查询
python -m rag.query "how to approve a deposit"

# 输出 JSON 格式（供程序消费）
python -m rag.query "KYC verification" --json
```

---

## 五、日常维护

### 5.1 新增/修改文档

1. 在 `md/`（英文）或 `zh-cn/`（中文）中创建或编辑 `.md` 文件
2. 如需在文档站侧边栏显示，更新 `_sidebar.md`
3. **重新构建 RAG 索引**：
   ```bash
   cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
   python -m rag.ingest
   ```

### 5.2 删除文档

1. 删除对应 `.md` 文件
2. 更新 `_sidebar.md` 移除链接
3. 重新构建 RAG 索引（同上）

### 5.3 文档撰写规范

为保持 Docsify 和 RAG 切分的一致性，请遵循以下格式：

```markdown
# **文档标题**

## **1. 章节名称**

章节正文内容...

### **子章节（可选）**

子章节内容...

## **2. 下一个章节**

...
```

**要点：**
- `# **标题**` 作为文档主标题
- `## **N. 章节**`（英文）或 `## **N、章节**`（中文）作为一级章节切分边界
- RAG 按 `##` 边界将每个章节切分为一个独立检索段落
- 避免在 `##` 章节内嵌套另一层 `##`

### 5.4 图片资源

- 截图放入 `images/` 目录
- 中文文档的图片放入 `zh-cn/images/`
- MD 中引用：`![描述](../images/xxx.png)`

### 5.5 版本控制

```bash
# 提交文档变更
git add md/ zh-cn/ _sidebar.md
git commit -m "docs: 更新佣金方案配置说明"

# 注意：rag_data/ 在 .gitignore 中，不会被提交
# 每次文档更新后需手动运行 python -m rag.ingest 重建索引
```

---

## 六、RAG 技术细节

### 切分策略

- **边界识别**：正则匹配 `## **数字. 标题**`（英文）和 `## **中文数字、标题**`（中文）
- **不分段**：每个 `##` 章节作为一个完整段落，不进行固定长度切分
- **最小长度**：少于 50 字符的段落被丢弃
- **元数据**：每个段落保留文件路径、语言、章节号、章节标题

### 检索算法

- **BM25**（k1=1.5, b=0.75）：稀疏向量（关键词）检索
- **中文分词**：字符级 bigram（如 "佣金方案" → ["佣金", "金方", "方案"]）
- **英文分词**：按字母数字 token 切分，过滤单字符
- **向量检索**：bge-m3 将段落与查询编码为 1024 维向量，点积计分（L2 归一化后等价余弦相似度）
- **混合融合**：BM25 与向量各自召回 top-20，用 RRF（Reciprocal Rank Fusion）合并排名
- **精排（Rerank）**：bge-reranker-v2-m3 对融合后的 20 个候选重打分，取 top-5

### 性能

| 指标 | 数值 |
|------|------|
| 文档总数 | 85 个 .md 文件 |
| 段落总数 | ~474 个 |
| BM25 索引大小 | ~1.5 MB |
| 向量索引大小 | ~1.9 MB（474 × 1024 维 float32） |
| 模型体积 | ~3.3 GB（bge-m3 + reranker） |
| 构建时间（含向量化） | 1–3 分钟（CPU） |
| 查询延迟（模型已加载） | <1 秒 |

---

## 七、常见问题

### Q1：Docsify 和 RAG 会互相影响吗？

不会。Docsify 是纯前端渲染（一个 `index.html` + CDN），RAG 是独立的 Python 脚本和索引文件。两者只共享源 `.md` 文件（只读）。

### Q2：文档更新后 RAG 没有生效？

重新运行 `python -m rag.ingest` 重建索引。索引不会自动更新。

### Q3：能否用 ChatGPT/OpenAI 替代本地检索？

可以。将 `rag/query.py` 的 `--json` 输出传给任意 LLM 的 API 即可实现带上下文的问答。当前方案不需要 API Key，完全本地运行。

### Q4：如何让 AI 自动回答问题？

运行 `python -m rag.query "问题"` 获取 top-5 段落，将段落作为上下文附加到 LLM 的 prompt 中，LLM 基于上下文生成答案。（详见第八节）

---

## 八、AI 问答集成方案

### 8.1 方案一：Claude Code 直接问答（当前可用，零配置）

在 Claude Code 会话中直接提问，Claude 自动搜索文档并回答。

```
用户：佣金方案的结算周期是多久？
Claude：[自动搜索文档 → 给出答案并引用来源]
```

**优点**：无需任何额外配置或 API Key。
**缺点**：依赖 Claude Code 会话，无法集成到其他系统。

---

### 8.2 方案二：脚本驱动问答（命令行 + LLM API）

#### 核心理念

RAG = **R**etrieval（检索）+ **A**ugmented（增强）+ **G**eneration（生成）

```
┌──────────┐      ┌─────────────────┐      ┌──────────┐
│  用户问题  │ ───→ │ 1. 检索相关段落    │ ───→ │ 2. LLM   │ ───→ 答案
│          │      │ (python -m rag.  │      │ 生成答案   │
│          │      │  query --json)   │      │          │
└──────────┘      └─────────────────┘      └──────────┘
                         ↑
                  rag_data/ 中的 BM25 索引
```

**为什么不能跳过检索步骤？**

如果直接问 LLM "MIM CRM 的佣金怎么配置？"，LLM 的训练数据中没有你的内部文档，它只能编造答案（幻觉）。而 RAG 的做法是：先把文档中和问题相关的段落找出来，附在 prompt 里一起发给 LLM，LLM 就有了"参考资料"，能给出基于真实文档的答案。

#### 运行方式

代码已落地为 `rag/ask.py`（依赖 `rag/llm.py` 与 `rag/query.py`），直接运行：

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.ask "佣金方案的结算周期是多久？"
```

LLM 通过环境变量复用 Claude Code 的中转服务配置（`ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`），无需额外设置 API Key。模型默认取 `ANTHROPIC_MODEL`，可用 `LLM_MODEL` 覆盖。

#### 方案二的适用场景

- 开发者在终端里快速查询文档
- 写 CI/CD 脚本，自动检查文档一致性
- 作为其他自动化流程中的一个环节

---

### 8.3 方案三：完整 RAG 问答 API 服务

#### 核心理念

把方案二的逻辑包装成一个 **HTTP API 服务**，让它 7×24 小时运行，任何程序都能通过 HTTP 调用来获取答案。

#### 架构图

```
┌──────────────────┐
│  聊天机器人       │──┐
│ (飞书/企微/钉钉)   │  │
└──────────────────┘  │     POST /ask              ┌─────────────────┐
                       │ ────────────────────────→  │   Flask API     │
┌──────────────────┐  │ {"question": "..."}      │   服务器          │
│  CRM 后台        │──┤ ←────────────────────────  │   (rag/api.py)  │
│ (嵌入智能助手)    │  │ {"answer":"...",        │                 │
└──────────────────┘  │  "sources":[...]}        │  内部流程:       │
                       │                          │  1. BM25 检索    │
┌──────────────────┐  │                          │  2. 构建 prompt  │
│  任何能发 HTTP    │──┘                          │  3. 调用 LLM API│
│  请求的程序       │                              │  4. 返回答案     │
└──────────────────┘                              └─────────────────┘
```

#### 部署与运行

代码已落地为 `rag/api.py`（依赖 `rag/llm.py` 与 `rag/query.py`）。

```bash
# 1. 安装依赖
pip install flask anthropic

# 2. 环境变量（复用 Claude Code 的中转服务配置，无需额外设置）
#    ANTHROPIC_BASE_URL / ANTHROPIC_AUTH_TOKEN 已存在即可
#    可选：LLM_MODEL 覆盖默认模型

# 3. 启动服务
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.api
```

#### 调用示例

```bash
# 测试健康检查
curl http://localhost:8000/health

# 问答请求
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"如何审批一笔入金？\"}"
```

响应示例：
```json
{
  "answer": "根据文档，审批入金的步骤如下：\n1. 进入「资金管理 → 待办入金」\n2. ...",
  "sources": [
    {"file": "zh-cn/待办入金.md", "section": "三 核心功能详解", "title": "待办入金"},
    {"file": "md/deposit_to_do.md", "section": "1 Module Overview", "title": "Deposit To-do"}
  ]
}
```

#### 方案三的应用场景

| 场景 | 集成方式 |
|------|----------|
| **CRM 后台嵌入智能助手** | 在后台页面添加一个对话框，点"提问"时发 POST 请求到 `/ask` |
| **飞书/企微/钉钉机器人** | 收到 @机器人 消息 → 调 `/ask` → 把答案发回群里 |
| **内部知识库搜索** | 写一个简单的前端页面，搜索框提交到 `/ask`，展示答案+来源 |

#### 生产环境注意

- 使用 `gunicorn` 替代 Flask 内置服务器：`gunicorn -w 4 -b 0.0.0.0:8000 rag.api:app`
- 考虑增加缓存层（相同问题不重复调用 LLM）
- 添加请求频率限制（rate limiting）防止滥用
- LLM API 密钥通过环境变量注入，不要硬编码

---

> 📌 如有问题，检查 `rag/config.py` 中的路径配置是否正确，或运行 `python -m rag.ingest` 重建索引。
