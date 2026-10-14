"""RAG 脚本驱动问答 — 检索 + LLM 生成.

用法:
    python -m rag.ask "如何审批一笔入金？"
"""

import sys

from rag.query import retrieve
from rag.llm import build_prompt, generate

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    if len(sys.argv) < 2:
        print("用法: python -m rag.ask \"你的问题\"", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]
    print(f"检索中: \"{query}\"\n")

    try:
        chunks = retrieve(query)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    if not chunks:
        print("未在文档中找到相关信息。")
        return

    print(f"找到 {len(chunks)} 个相关段落，正在生成答案...\n")
    print("=" * 60)

    prompt = build_prompt(query, chunks)
    answer = generate(prompt)
    print(answer)

    print("\n" + "=" * 60)
    print("参考来源:")
    for c in chunks:
        print(f"  - {c['file']} §{c['section_number']} {c['section_title']}")


if __name__ == "__main__":
    main()
