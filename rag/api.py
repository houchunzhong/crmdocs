"""RAG 问答 API 服务 — 基于 Flask 的 HTTP 接口.

用法:
    python -m rag.api

接口:
    POST /ask     {"question": "如何审批一笔入金？"}
    GET  /health
"""

import os

from flask import Flask, request, jsonify

from rag.query import retrieve
from rag.llm import build_prompt, generate, get_model

app = Flask(__name__)

INDEX_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MIM CRM 知识库助手</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, "Segoe UI", "Microsoft YaHei", sans-serif; background: #f5f6f8; height: 100vh; display: flex; flex-direction: column; }
  header { background: #fff; padding: 16px 24px; border-bottom: 1px solid #e5e6eb; }
  header h1 { font-size: 18px; color: #1f2329; }
  header p { font-size: 12px; color: #8a8f99; margin-top: 4px; }
  #chat { flex: 1; overflow-y: auto; padding: 24px; max-width: 860px; width: 100%; margin: 0 auto; }
  .msg { margin-bottom: 20px; }
  .q { background: #e8f3ff; padding: 12px 16px; border-radius: 10px; margin-left: auto; max-width: 80%; width: fit-content; font-size: 14px; color: #1f2329; }
  .a { background: #fff; padding: 16px 20px; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,.06); font-size: 14px; line-height: 1.8; color: #1f2329; }
  .a h3 { font-size: 15px; margin: 12px 0 6px; }
  .a strong { color: #1f2329; }
  .a code { background: #f2f3f5; padding: 1px 5px; border-radius: 4px; font-size: 13px; }
  .sources { margin-top: 10px; font-size: 12px; color: #8a8f99; list-style: none; }
  .sources li { margin: 2px 0; }
  .loading { color: #8a8f99; font-size: 13px; padding: 12px 16px; }
  .spinner { display: inline-block; width: 12px; height: 12px; border: 2px solid #c9cdd4; border-top-color: #3370ff; border-radius: 50%; animation: spin 0.8s linear infinite; margin-right: 8px; vertical-align: -2px; }
  @keyframes spin { to { transform: rotate(360deg); } }
  footer { background: #fff; border-top: 1px solid #e5e6eb; padding: 16px 24px; }
  #inputwrap { max-width: 860px; margin: 0 auto; display: flex; gap: 12px; }
  #q { flex: 1; padding: 12px 16px; border: 1px solid #d0d3d9; border-radius: 8px; font-size: 14px; outline: none; }
  #q:focus { border-color: #3370ff; }
  #send { padding: 12px 24px; background: #3370ff; color: #fff; border: none; border-radius: 8px; font-size: 14px; cursor: pointer; }
  #send:hover { background: #245bdb; }
  #send:disabled { background: #a8c0ff; cursor: not-allowed; }
</style>
</head>
<body>
<header>
  <h1>MIM CRM 知识库助手</h1>
  <p>基于 CRM 文档的知识问答 · 答案均引用文档来源</p>
</header>
<div id="chat"></div>
<footer>
  <div id="inputwrap">
    <input id="q" type="text" placeholder="输入问题，例如：如何审批一笔入金？" autocomplete="off">
    <button id="send">发送</button>
  </div>
</footer>
<script>
const chat = document.getElementById('chat');
const q = document.getElementById('q');
const send = document.getElementById('send');

function escapeHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function renderMarkdown(text) {
  let html = escapeHtml(text);
  html = html.replace(/^### (.*)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.*)$/gm, '<h3>$1</h3>');
  html = html.replace(/^# (.*)$/gm, '<h3>$1</h3>');
  html = html.replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>');
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
  html = html.replace(/\\n/g, '<br>');
  return html;
}
function addQ(text) {
  const div = document.createElement('div');
  div.className = 'msg';
  const qdiv = document.createElement('div');
  qdiv.className = 'q';
  qdiv.textContent = text;
  div.appendChild(qdiv);
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}
function addLoading() {
  const div = document.createElement('div');
  div.className = 'msg';
  div.id = 'loading';
  div.innerHTML = '<div class="loading"><span class="spinner"></span>正在检索文档并生成答案，首次查询需加载模型，请稍候…</div>';
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}
function addAnswer(answer, sources) {
  const div = document.createElement('div');
  div.className = 'msg';
  const a = document.createElement('div');
  a.className = 'a';
  a.innerHTML = renderMarkdown(answer);
  div.appendChild(a);
  if (sources && sources.length) {
    const ul = document.createElement('ul');
    ul.className = 'sources';
    ul.innerHTML = '<li style="font-weight:600;color:#646a73">来源：</li>' +
      sources.map(s => '<li>· ' + escapeHtml(s.file + ' §' + s.section) + '</li>').join('');
    div.appendChild(ul);
  }
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}
async function ask() {
  const text = q.value.trim();
  if (!text) return;
  addQ(text);
  q.value = '';
  send.disabled = true;
  addLoading();
  try {
    const resp = await fetch('/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question: text})
    });
    const data = await resp.json();
    document.getElementById('loading')?.remove();
    if (data.error) addAnswer('出错了：' + data.error, []);
    else addAnswer(data.answer || '（无答案）', data.sources || []);
  } catch (e) {
    document.getElementById('loading')?.remove();
    addAnswer('请求失败：' + e.message, []);
  } finally {
    send.disabled = false;
    q.focus();
  }
}
send.addEventListener('click', ask);
q.addEventListener('keydown', e => { if (e.key === 'Enter') ask(); });
</script>
</body>
</html>"""


@app.route("/")
def index():
    return INDEX_HTML


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True)
    if not data or "question" not in data:
        return jsonify({"error": "请求体必须包含 'question' 字段"}), 400

    query = data["question"].strip()
    if not query:
        return jsonify({"error": "question 不能为空"}), 400

    try:
        chunks = retrieve(query)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 500

    if not chunks:
        return jsonify({"answer": "未在文档中找到相关信息，请尝试换个问法。", "sources": []})

    prompt = build_prompt(query, chunks)
    try:
        answer = generate(prompt)
    except Exception as e:
        return jsonify({"error": f"LLM 调用失败: {str(e)}"}), 500

    sources = [
        {
            "file": c["file"],
            "section": f"{c['section_number']} {c['section_title']}",
            "title": c["title"],
        }
        for c in chunks
    ]

    return jsonify({"answer": answer, "sources": sources})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model": get_model()})


if __name__ == "__main__":
    print(f"LLM Model: {get_model()}")
    print("知识库助手: http://localhost:8000  (浏览器打开即可提问)")
    print("接口: GET / | POST /ask | GET /health")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")), debug=False)
