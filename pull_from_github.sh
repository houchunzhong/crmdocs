#!/bin/bash

# 日志文件路径
LOG_FILE="/home/ec2-user/logs/git-pull.log"
REPO_DIR="/home/ec2-user/my-docs"

# 创建日志目录（如果不存在）
mkdir -p "$(dirname "$LOG_FILE")"

# 记录开始时间
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting git pull..." >> "$LOG_FILE"

# 进入仓库目录
cd "$REPO_DIR" || {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: Failed to cd into $REPO_DIR" >> "$LOG_FILE"
    exit 1
}

# 拉取最新代码
if git pull origin main >> "$LOG_FILE" 2>&1; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] SUCCESS: Git pull completed." >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: Git pull failed!" >> "$LOG_FILE"
fi

# 可选：重启 docsify 服务（如果你用 systemd 管理）
sudo systemctl restart docsify >> "$LOG_FILE" 2>&1

exit 0
