"""RAG knowledge base — LLM generation via Anthropic-compatible API.

Reuses the same credentials Claude Code uses:
  ANTHROPIC_BASE_URL     — API endpoint (e.g. a gateway like newapi.fundeai.cn)
  ANTHROPIC_AUTH_TOKEN   — Bearer token (or ANTHROPIC_API_KEY)
  ANTHROPIC_MODEL / LLM_MODEL — model name (defaults to deepseek-v4-pro)
"""

import json
import os
from pathlib import Path

import anthropic

_client = None
_settings_env = None


def _get_settings_env() -> dict:
    """Read env fallback from Claude Code's settings.json."""
    global _settings_env
    if _settings_env is None:
        try:
            data = json.loads(
                (Path.home() / ".claude" / "settings.json").read_text(encoding="utf-8")
            )
            _settings_env = data.get("env", {}) or {}
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            _settings_env = {}
    return _settings_env


def _get_env(key: str) -> str | None:
    """Resolve a value from process env first, then Claude Code settings.json."""
    return os.environ.get(key) or _get_settings_env().get(key)


def get_client():
    global _client
    if _client is None:
        base_url = _get_env("ANTHROPIC_BASE_URL")
        auth_token = _get_env("ANTHROPIC_AUTH_TOKEN")
        api_key = _get_env("ANTHROPIC_API_KEY")

        if auth_token:
            _client = anthropic.Anthropic(base_url=base_url, auth_token=auth_token)
        elif api_key:
            _client = anthropic.Anthropic(base_url=base_url, api_key=api_key)
        else:
            raise RuntimeError(
                "未配置 API 密钥：请设置环境变量 ANTHROPIC_AUTH_TOKEN 或 ANTHROPIC_API_KEY"
            )
    return _client


def get_model() -> str:
    return (
        _get_env("ANTHROPIC_MODEL")
        or _get_env("LLM_MODEL")
        or "deepseek-v4-pro"
    )


def generate(prompt: str, max_tokens: int = 2000) -> str:
    """Send a prompt and return the assistant's text reply."""
    client = get_client()
    resp = client.messages.create(
        model=get_model(),
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(
        block.text for block in resp.content if getattr(block, "type", "") == "text"
    )
    return text.strip()


def build_prompt(query: str, chunks: list[dict]) -> str:
    """Assemble retrieval results + question into a single prompt."""
    context_parts = []
    for c in chunks:
        src = f"{c['file']} §{c['section_number']} {c['section_title']}"
        context_parts.append(f"--- 来源: {src} ---\n{c['content'][:1200]}")
    context = "\n\n".join(context_parts)

    return f"""你是 MIM CRM 系统的技术支持专家。
请基于以下文档内容回答用户问题。
如果文档中没有相关信息，请如实说"文档中未找到相关信息"，不要编造。

## 参考文档
{context}

## 用户问题
{query}

请用中文回答，并在末尾列出信息来源（文件名+章节）。"""
