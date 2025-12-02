#!/bin/bash
cd /home/ec2-user/my-docs/docs

# 获取当前时间作为提交信息
MESSAGE="Auto-update docs on $(date '+%Y-%m-%d %H:%M')"

sudo git add .
sudo git commit -m "$MESSAGE" || echo "No changes to commit"
sudo git push origin main

