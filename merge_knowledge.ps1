# ============================================================
# Merge Script: Y:\000_Knowledge → Z:\000_Knowledge
# 目的: 将 Y 盘的内容合并到 Z 盘，使 Z 盘拥有最全最优化的目录结构
# 策略: 只添加 Z 盘缺失的文件，不覆盖 Z 盘已有文件
# 生成时间: 2026-08-07
# ============================================================

$Y_SRC = "Y:\000_Knowledge"
$Z_DST = "Z:\000_Knowledge"

$ROBO_FLAGS = "/E /XO /XC /XN /R:3 /W:5 /NP /NDL /MT:8"
# /E   = 复制子目录(含空目录)
# /XO  = 排除目标中更新的文件
# /XC  = 排除目标中已变更的文件
# /XN  = 排除目标中较新的文件
# /R:3 = 重试3次
# /W:5 = 重试间隔5秒
# /MT:8= 多线程(8线程)
# /NP  = 不显示进度百分比
# /NDL = 不显示目录列表

$LogFile = "$env:USERPROFILE\Desktop\merge_knowledge_log_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
# 先测试 Z 盘可写性
Write-Host ">>> 检查 Z: 盘写入权限..." -ForegroundColor Yellow
try {
    $testFile = "$Z_DST\.merge_test_$([Guid]::NewGuid())"
    New-Item -Path $testFile -ItemType File -Force -ErrorAction Stop | Out-Null
    Remove-Item $testFile -Force
    Write-Host ">>> Z: 盘可写，继续执行..." -ForegroundColor Green
} catch {
    Write-Host ">>> 错误: Z: 盘不可写! 请先以适当权限重新挂载 Z: 盘。" -ForegroundColor Red
    Write-Host "    Z: 映射到 \\10.26.10.247\f，当前仅有只读权限。" -ForegroundColor Red
    Write-Host "    请在 NAS 管理界面或通过 net use 重新挂载为可写后重试。" -ForegroundColor Red
    pause
    exit 1
}

function Write-Log {
    param($Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$timestamp] $Message"
    Write-Host $line
}

function Invoke-RoboMerge {
    param($Source, $Dest, $Description)

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Log "START: $Description"
    Write-Host "  Source: $Source"
    Write-Host "  Dest:   $Dest"
    Write-Host "========================================" -ForegroundColor Cyan

    # Ensure destination parent exists
    $destParent = Split-Path $Dest -Parent
    if (-not (Test-Path $destParent)) {
        Write-Log "WARNING: Destination parent not found: $destParent"
    }

    if (-not (Test-Path $Source)) {
        Write-Log "WARNING: Source not found, skipping: $Source"
        return
    }

    $result = robocopy $Source $Dest $ROBO_FLAGS 2>&1

    # robocopy exit codes: 0=no changes, 1=files copied, 2=extra files, 3=2+1, 4-7=mismatch+copy, 8+=errors
    $exitCode = $LASTEXITCODE
    if ($exitCode -ge 8) {
        Write-Log "WARNING: robocopy exit code $exitCode (errors detected)"
    } else {
        Write-Log "OK: robocopy exit code $exitCode"
    }

    Write-Log "DONE: $Description"
}

# ============================================================
# STEP 1: 001_Upload_Yuque (语雀知识库导出)
# Z 盘没有此目录，全新复制
# ============================================================
Invoke-RoboMerge `
    -Source "$Y_SRC\001_Upload_Yuque" `
    -Dest "$Z_DST\001_Upload_Yuque" `
    -Description "001_Upload_Yuque: 语雀知识库导出 (Word/Excel/PDF/PPT/Markdown/RuiLi/等保/Tradewise)"

# ============================================================
# STEP 2: 002_Git_documents (Git 仓库文档)
# 差异: Y 盘多了 git_backup/ 仓库
# ============================================================
Invoke-RoboMerge `
    -Source "$Y_SRC\002_Git_documents" `
    -Dest "$Z_DST\002_Git_documents" `
    -Description "002_Git_documents: Git仓库 (补充 git_backup 等)"

# ============================================================
# STEP 3: 003_SVN_documents (SVN 文档归档)
# 合并两者的内容，Z 盘保留为主
# ============================================================
Invoke-RoboMerge `
    -Source "$Y_SRC\003_SVN_documents" `
    -Dest "$Z_DST\003_SVN_documents" `
    -Description "003_SVN_documents: SVN文档 (南京机房/外部项目/部门工作/雅安机房/视频等)"

# ============================================================
# STEP 4: 004_NetworkArchitecture (网络架构)
# Z 盘没有此目录，全新复制
# ============================================================
Invoke-RoboMerge `
    -Source "$Y_SRC\004_NetworkArchitecture" `
    -Dest "$Z_DST\004_NetworkArchitecture" `
    -Description "004_NetworkArchitecture: 网络架构 (北京DC/交换机配置备份/Huawei手册)"

# ============================================================
# STEP 5: 006_AI_platform -> 005_AI_platform (AI平台, 重编号)
# Z 盘没有此目录，从 Y 的 006 复制并重编号为 005
# ============================================================
Invoke-RoboMerge `
    -Source "$Y_SRC\006_AI_platform" `
    -Dest "$Z_DST\005_AI_platform" `
    -Description "005_AI_platform: AI平台 (DeepSeek/AnythingLLM) [从006重编号]"

# ============================================================
# FINAL: 验证结果
# ============================================================
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  合并完成! 最终 Z:\000_Knowledge 结构:" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

Get-ChildItem $Z_DST -Directory | Sort-Object Name | ForEach-Object {
    $itemCount = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue | Measure-Object).Count
    Write-Host "  $($_.Name)/  (items: $itemCount)"
}

Write-Host ""
Write-Log "===== ALL DONE ====="
Write-Host ""
Write-Host "Z 盘现已包含以下编号目录:" -ForegroundColor Yellow
Write-Host "  001_Upload_Yuque        - 语雀知识库导出" -ForegroundColor White
Write-Host "  002_Git_documents       - Git 仓库文档" -ForegroundColor White
Write-Host "  003_SVN_documents       - SVN 文档归档" -ForegroundColor White
Write-Host "  004_NetworkArchitecture - 网络架构" -ForegroundColor White
Write-Host "  005_AI_platform         - AI 平台" -ForegroundColor White
Write-Host ""
Write-Host "以及以下学习/认证资料目录 (Z 盘原有):" -ForegroundColor Yellow
Write-Host "  HCIE_Security, HCIP_Datacom, Linux-fastfood, MySQL_进阶,"
Write-Host "  Network_Knowledge, PMP给你的新人礼包, Tidb_videos,"
Write-Host "  企业无线知识, 百万架构师, 看漫画学Python, 讲义"
Write-Host ""
Write-Host "注意: 若执行时提示权限拒绝，请以管理员身份运行 PowerShell 并重新执行此脚本。" -ForegroundColor Red
