# CRM 知识库 Web 问答页面 — 部署与使用指南

> 版本：v1.0

---

## 一、功能概述

本项目提供一套基于 RAG（检索增强生成）的 CRM 知识库问答系统。其中 Web 页面是面向日常使用的前端入口：打开浏览器即可用自然语言提问，系统从 CRM 文档中检索相关内容，并调用大模型生成带来源引用的答案。

**核心能力：**

- 🔍 **语义检索**：BM25 关键词检索 + bge-m3 向量检索的混合召回，配合 bge-reranker 精排，能理解「返佣」≈「佣金」这类同义/口语化表达
- 💬 **智能问答**：检索到的段落拼进 prompt，由大模型基于真实文档生成答案（非编造）
- 📎 **来源引用**：每个答案末尾列出引用的文档文件名与章节
- 🌐 **浏览器访问**：无需安装客户端，打开网页即用

---

## 二、系统架构

```
┌─────────────────────────────────────────────────────────┐
│  浏览器 (localhost:8000)                                  │
│  ┌─────────────┐      ┌──────────────────────────────┐   │
│  │  Web 页面    │ ───→ │  Flask API (rag/api.py)      │   │
│  │  (内嵌 HTML) │      │   ├─ GET  /        → 页面     │   │
│  └─────────────┘      │   ├─ POST /ask     → 问答     │   │
│                       │   └─ GET  /health  → 健康检查 │   │
│                       └──────────────┬───────────────┘   │
│                                      │                    │
│         ┌────────────────────────────┼────────────────┐   │
│         │  检索层 (rag/query.py)     │                │   │
│         │  BM25 + bge-m3 混合检索    │                │   │
│         │  → bge-reranker 精排 top-5 │                │   │
│         └────────────────────────────┼────────────────┘   │
│                                      │                    │
│         ┌────────────────────────────┼────────────────┐   │
│         │  生成层 (rag/llm.py)       │                │   │
│         │  构建 prompt → 调用 LLM    │                │   │
│         └────────────────────────────┘                │   │
└─────────────────────────────────────────────────────────┘
          ↑                              ↑
   文档源 (md/ + zh-cn/)          大模型 API（中转服务）
```

---

## 三、环境要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows / Linux / macOS |
| Python | 3.9+（本项目在 3.14.5 验证通过） |
| 磁盘空间 | 约 8 GB（模型文件约 3.3 GB + 依赖 + 索引） |
| 网络 | 首次部署需联网下载模型与依赖 |

---

## 四、首次部署步骤

### 4.1 安装依赖

```bash
pip install sentence-transformers modelscope torch numpy anthropic flask
```

各包用途：

| 包 | 用途 |
|----|------|
| `sentence-transformers` | 加载 bge-m3 embedding 与 bge-reranker 精排模型 |
| `modelscope` | 从国内镜像（魔搭）下载模型 |
| `torch` / `numpy` | 模型推理与向量运算 |
| `anthropic` | 调用大模型 API |
| `flask` | HTTP 服务与 Web 页面 |

### 4.2 下载模型（仅首次）

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.download_models
```

模型从 **ModelScope（阿里魔搭）** 下载到 `rag_data/models/`：

| 模型 | 用途 | 大小 |
|------|------|------|
| `bge-m3` | 文本向量化（中英双语） | 约 2.3 GB |
| `bge-reranker-v2-m3` | 检索结果精排 | 约 2.3 GB |

> ⚠️ 若网络可直连 HuggingFace，也可自行下载对应模型放到 `rag_data/models/bge-m3` 与 `rag_data/models/bge-reranker-v2-m3` 目录。

### 4.3 构建索引

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.ingest
```

预期输出：

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

生成的索引文件位于 `rag_data/`：

| 文件 | 说明 |
|------|------|
| `chunks.json` | 切分后的文档段落 |
| `bm25_index.pkl` | BM25 关键词索引 |
| `vectors.npy` | bge-m3 向量索引（474 × 1024 维） |

### 4.4 配置大模型（通常无需操作）

系统通过 Anthropic 兼容 API 调用大模型，凭据按以下优先级自动读取：

1. **进程环境变量**（`ANTHROPIC_AUTH_TOKEN`、`ANTHROPIC_BASE_URL`、`ANTHROPIC_MODEL`）
2. **`~/.claude/settings.json` 的 `env` 字段**（Claude Code 配置，自动 fallback）

如果你使用 Claude Code，且其配置中已含中转服务凭据，则**无需任何操作**。否则需手动设置环境变量：

```bash
# Windows (PowerShell)
$env:ANTHROPIC_AUTH_TOKEN="sk-xxx"
$env:ANTHROPIC_BASE_URL="https://your-gateway.example.com"
$env:ANTHROPIC_MODEL="your-model-name"

# Linux / macOS
export ANTHROPIC_AUTH_TOKEN="sk-xxx"
export ANTHROPIC_BASE_URL="https://your-gateway.example.com"
export ANTHROPIC_MODEL="your-model-name"
```

### 4.5 启动服务

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.api
```

看到以下输出即启动成功：

```
LLM Model: deepseek-v4-pro
知识库助手: http://localhost:8000  (浏览器打开即可提问)
接口: GET / | POST /ask | GET /health
 * Running on http://127.0.0.1:8000
```

---

## 五、使用方法

1. 打开浏览器，访问 **http://localhost:8000**
2. 在底部输入框输入问题，例如：
   - `如何审批一笔入金？`
   - `怎么设置代理的返佣比例？`
   - `KYC 审核的流程是什么？`
3. 按回车或点击「发送」按钮
4. 等待答案生成（**首次提问需加载模型，约 20–30 秒**，之后每次约几秒）
5. 答案下方会列出引用来源（文件名 + 章节）

**使用技巧：**

- 问题尽量具体、包含业务关键词，检索更精准
- 支持中英文提问（系统自动检索对应语言文档）
- 换个说法提问往往能命中不同角度的文档内容

---

## 六、API 接口说明

| 接口 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 返回 Web 问答页面（HTML） |
| `/ask` | POST | 问答接口 |
| `/health` | GET | 健康检查 |

### POST /ask

请求体：

```json
{"question": "如何审批一笔入金？"}
```

响应体：

```json
{
  "answer": "审批入金的步骤如下：\n1. ...",
  "sources": [
    {"file": "zh-cn/待办入金.md", "section": "三 核心功能详解", "title": "待办入金"}
  ]
}
```

调用示例：

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "how to approve a deposit"}'
```

### GET /health

```bash
curl http://localhost:8000/health
# {"model": "deepseek-v4-pro", "status": "ok"}
```

---

## 七、日常维护

### 7.1 文档更新后重建索引

修改 `md/` 或 `zh-cn/` 下的文档后，需重建索引：

```bash
cd D:\008_Tradewise\001_Documents\000_manual_md\crmdocs
python -m rag.ingest
```

### 7.2 重启服务

在运行 `python -m rag.api` 的终端按 `Ctrl+C` 停止，再次执行 `python -m rag.api` 启动。

---

## 八、常见问题（FAQ）

### Q1：报错「未配置 API 密钥」

**原因**：系统既未在环境变量、也未在 `~/.claude/settings.json` 找到大模型凭据。

**解决**：按「4.4 配置大模型」一节设置 `ANTHROPIC_AUTH_TOKEN` 与 `ANTHROPIC_BASE_URL`。

### Q2：报错「模型不存在 / Embedding model not found」

**原因**：`rag_data/models/` 下缺少模型文件。

**解决**：运行 `python -m rag.download_models` 下载模型。

### Q3：报错「Index files missing」

**原因**：`rag_data/` 下缺少索引文件。

**解决**：运行 `python -m rag.ingest` 构建索引。

### Q4：首次提问特别慢

**正常现象**。首次请求需加载 bge-m3 与 reranker 两个模型（约 20–30 秒），之后每次请求仅需几秒。加载完成后进程内会缓存，无需重复加载。

### Q5：端口 8000 被占用

**解决**：指定其他端口启动：

```bash
# Windows (PowerShell)
$env:PORT="8001"; python -m rag.api

# Linux / macOS
PORT=8001 python -m rag.api
```

### Q6：局域网内其他设备访问

服务默认监听 `0.0.0.0`，同一局域网内的其他设备可通过本机 IP 访问，例如：

```
http://192.168.x.x:8000
```

> ⚠️ 需确保本机防火墙放行对应端口。

---

## 九、后台运行与生产部署

### 9.1 Windows 后台运行

可使用 `pythonw` 或将其注册为计划任务，避免终端窗口常驻。

### 9.2 Linux 生产部署

使用 `waitress` 或 `gunicorn` 替代 Flask 内置服务器：

```bash
pip install waitress
waitress-serve --host 0.0.0.0 --port 8000 rag.api:app
```

### 9.3 生产环境注意事项

- 大模型 API 密钥通过环境变量注入，**不要硬编码进代码或提交到 git**
- 可增加缓存层，相同问题不重复调用大模型
- 添加请求频率限制（rate limiting）防止滥用
- 如需对外提供服务，建议置于反向代理（Nginx）之后并配置 HTTPS

---

## 十、相关文件速查

| 文件 | 作用 |
|------|------|
| `rag/api.py` | Flask 服务 + Web 页面 |
| `rag/llm.py` | 大模型调用封装 |
| `rag/query.py` | 检索入口（混合检索 + rerank） |
| `rag/ingest.py` | 构建索引 |
| `rag/download_models.py` | 下载模型 |
| `rag/config.py` | 路径与模型配置 |
| `DEPLOYMENT.md` | 文档站 + RAG 总体部署维护指南 |
