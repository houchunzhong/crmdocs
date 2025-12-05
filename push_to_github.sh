#!/bin/bash
cd /home/ec2-user/my-docs

# 获取当前时间作为提交信息（修复格式错误）
MESSAGE="Auto-update docs on $(date '+%Y-%m-%d %H:%M')"

# 移除 sudo！
git add .
git commit -m "$MESSAGE" || echo "No changes to commit"
git push origin main
