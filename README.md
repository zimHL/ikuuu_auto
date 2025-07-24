# GitHub Actions 自动化部署指南

本文档详细介绍如何使用 GitHub Actions 实现 ikuuu 自动签到的云端自动化运行。

## 🚀 快速开始

### 第一步：Fork 或创建仓库

1. **Fork 本仓库**（推荐）
   - 点击右上角的 "Fork" 按钮
   - 选择你的 GitHub 账户

2. **或者创建新仓库**
   - 在 GitHub 创建新的私有仓库
   - 将代码文件上传到仓库

### 第二步：配置 Secrets

⚠️ **重要：所有敏感信息必须通过 GitHub Secrets 配置，确保隐私安全**

1. 进入你的 GitHub 仓库页面
2. 点击 `Settings`（设置）
3. 在左侧菜单找到 `Secrets and variables` → `Actions`
4. 点击 `New repository secret` 添加以下密钥：

#### 必需的 Secrets

| Secret 名称 | 说明 | 示例 |
|------------|------|------|
| `IKUUU_EMAIL` | 你的 ikuuu 账户邮箱 | `user@example.com` |
| `IKUUU_PASSWORD` | 你的 ikuuu 账户密码 | `your_password_here` |

#### 配置步骤说明

```
GitHub 仓库 → Settings → Secrets and variables → Actions → New repository secret
```

1. **添加邮箱**
   - Name: `IKUUU_EMAIL`
   - Secret: 输入你的邮箱地址

2. **添加密码**
   - Name: `IKUUU_PASSWORD`
   - Secret: 输入你的密码

### 第三步：启用 GitHub Actions

1. 进入仓库的 `Actions` 标签页
2. 如果显示需要启用，点击 `I understand my workflows, go ahead and enable them`
3. 找到 `Daily Check-in` 工作流
4. 点击 `Enable workflow`

## ⏰ 运行时间配置

### 当前配置

```yaml
schedule:
  - cron: '30 16 * * *'  # 北京时间 00:30 每日执行
```

### 时间说明

- **执行时间**: 每天北京时间 00:30（UTC 16:30）
- **时区**: 脚本运行时设置为 `Asia/Shanghai`
- **频率**: 每日一次

### 自定义运行时间

如需修改运行时间，编辑 `.github/workflows/daily-checkin.yml` 文件中的 cron 表达式：

```yaml
# 北京时间 06:00 执行
- cron: '0 22 * * *'

# 北京时间 12:00 执行  
- cron: '0 4 * * *'

# 每天多次执行（早8点和晚8点）
- cron: '0 0 * * *'   # 北京时间 08:00
- cron: '0 12 * * *'  # 北京时间 20:00
```

## 🎯 手动触发

除了定时执行，还支持手动触发：

1. 进入仓库的 `Actions` 标签页
2. 选择 `Daily Check-in` 工作流
3. 点击右侧的 `Run workflow` 按钮
4. 点击绿色的 `Run workflow` 确认

## 📊 查看运行日志

### 查看执行历史

1. 进入 `Actions` 标签页
2. 查看 `Daily Check-in` 工作流的运行历史
3. 点击任意一次运行记录查看详细日志

### 日志输出示例

```
============================================================
[2024-01-01 00:30:15] 🚀 iKuuu 自动签到程序启动
============================================================
[2024-01-01 00:30:16] 🔑 正在使用账号 use***@example.com 登录...
[2024-01-01 00:30:18] ✅ 登录成功
[2024-01-01 00:30:19] ✅ 签到成功: 获得了 1024MB 流量
[2024-01-01 00:30:20] 📊 流量使用情况:
==================================================
📈 剩余流量: 309.97GB
📊 今日已用: 166.45MB
==================================================
============================================================
[2024-01-01 00:30:21] ✨ 程序执行完成
============================================================
```

### 配置说明

| 配置项 | 说明 |
|--------|------|
| `runs-on: ubuntu-latest` | 使用最新的 Ubuntu 环境 |
| `actions/checkout@v4` | 检出代码到运行环境 |
| `actions/setup-python@v4` | 设置 Python 环境 |
| `TZ: 'Asia/Shanghai'` | 设置时区为北京时间 |

## 🛡️ 安全最佳实践

### ✅ 推荐做法

- ✅ 使用 GitHub Secrets 存储敏感信息
- ✅ 设置仓库为私有（Private）
- ✅ 定期检查 Actions 运行日志
- ✅ 及时更新依赖包版本

### ❌ 避免的做法

- ❌ 在代码中硬编码账户信息
- ❌ 在公开仓库中存储敏感信息
- ❌ 共享包含密码的日志
- ❌ 使用弱密码

## 🔍 故障排除

### 常见问题及解决方案

#### 1. 工作流未自动运行

**可能原因**：
- GitHub Actions 未启用
- Secrets 配置错误
- 仓库处于非活跃状态

**解决方案**：
```bash
# 检查 Actions 是否启用
Repository Settings → Actions → General → Allow all actions

# 手动触发一次测试
Actions → Daily Check-in → Run workflow
```

#### 2. 登录失败

**可能原因**：
- 邮箱或密码错误
- 账户被锁定
- 网络连接问题

**解决方案**：
```bash
# 检查 Secrets 配置
Settings → Secrets → IKUUU_EMAIL / IKUUU_PASSWORD

# 确认账户状态
手动登录当前配置的域名网站验证
```

## 📞 支持与反馈

如果遇到问题或有改进建议：

1. 查看 [Issues](../../issues) 页面
2. 创建新的 Issue 描述问题
3. 提供详细的错误日志和环境信息

---

**⚠️ 免责声明**: 本项目仅供学习和个人使用，请遵守相关服务条款。
