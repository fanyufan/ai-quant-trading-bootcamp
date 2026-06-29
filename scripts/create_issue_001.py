# -*- coding: utf-8 -*-
"""
将本地 docs/issues/001-qmt-mysql-access-denied.md 同步创建为
GitHub / Gitee issue。

运行前请设置环境变量：
    Windows PowerShell:
        $env:GITHUB_TOKEN="your_github_token"
        $env:GITEE_TOKEN="your_gitee_token"
        python scripts/create_issue_001.py

    Windows CMD:
        set GITHUB_TOKEN=your_github_token
        set GITEE_TOKEN=your_gitee_token
        python scripts/create_issue_001.py
"""
import os
import re
import sys
from pathlib import Path

import requests

REPO_OWNER = "fanyufan"
REPO_NAME = "ai-quant-trading-bootcamp"
ISSUE_FILE = Path(__file__).parent.parent / "docs" / "issues" / "001-qmt-mysql-access-denied.md"


def parse_issue_file(file_path: Path) -> tuple[str, str]:
    """解析 Markdown 文件，返回 (标题, 正文)"""
    content = file_path.read_text(encoding="utf-8")

    # 提取第一个 # 标题作为 issue 标题
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if not match:
        raise ValueError("无法在 Markdown 中找到一级标题")
    title = match.group(1).strip()

    # 正文：去掉标题行
    body = re.sub(r"^#\s+.+\n+", "", content, count=1, flags=re.MULTILINE).strip()

    return title, body


def create_github_issue(title: str, body: str) -> dict:
    """调用 GitHub API 创建 issue"""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise EnvironmentError("请设置环境变量 GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }
    payload = {"title": title, "body": body}

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def create_gitee_issue(title: str, body: str) -> dict:
    """调用 Gitee API 创建 issue"""
    token = os.environ.get("GITEE_TOKEN")
    if not token:
        raise EnvironmentError("请设置环境变量 GITEE_TOKEN")

    url = f"https://gitee.com/api/v5/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    params = {"access_token": token}
    payload = {"title": title, "body": body}

    resp = requests.post(url, params=params, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def main():
    if not ISSUE_FILE.exists():
        print(f"错误：找不到 issue 文件 {ISSUE_FILE}", file=sys.stderr)
        sys.exit(1)

    title, body = parse_issue_file(ISSUE_FILE)
    print(f"Issue 标题: {title}")
    print(f"正文长度: {len(body)} 字符\n")

    # GitHub
    try:
        github_issue = create_github_issue(title, body)
        print(f"✅ GitHub issue 创建成功: {github_issue['html_url']}")
        print(f"   编号: #{github_issue['number']}")
    except Exception as e:
        print(f"❌ GitHub issue 创建失败: {e}", file=sys.stderr)

    print()

    # Gitee
    try:
        gitee_issue = create_gitee_issue(title, body)
        print(f"✅ Gitee issue 创建成功: {gitee_issue['html_url']}")
        print(f"   编号: #{gitee_issue['number']}")
    except Exception as e:
        print(f"❌ Gitee issue 创建失败: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
