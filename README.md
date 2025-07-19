# ikuuu 自动签到脚本

这是一个用于 ikuuu.one 网站的自动签到脚本，可以帮助用户自动完成每日签到并查看流量使用情况。

## 功能特性

- 🎯 **自动签到**: 自动完成 ikuuu.one 的每日签到
- 📊 **流量查询**: 查看剩余流量和今日已用流量
- 🔐 **安全登录**: 自动登录获取Cookie，无需手动配置
- 🛡️ **隐私保护**: 使用环境变量存储敏感信息，确保账户安全
- 📱 **真实模拟**: 模拟真实浏览器访问，避免被检测
- ⏰ **定时执行**: 支持GitHub Actions定时自动运行

## 环境要求

- Python 3.6+
- 依赖包：
  - `requests`
  - `beautifulsoup4`

## 安装依赖

```bash
pip install requests beautifulsoup4
```

## 配置说明

### 环境变量配置

本脚本需要以下环境变量：

- `IKUUU_EMAIL`: 你的ikuuu账户邮箱
- `IKUUU_PASSWORD`: 你的ikuuu账户密码

**⚠️ 重要提示**: 
- 请确保邮箱和密码信息的安全性
- 不要在代码中硬编码敏感信息
- 使用环境变量或GitHub Secrets存储


### GitHub Actions 自动化配置

本项目使用GitHub Actions实现自动化签到，无需手动运行，完全托管在云端。

#### 设置GitHub Repository Secrets

1. 进入你的GitHub仓库页面
2. 点击 `Settings`（设置）标签
3. 在左侧菜单中找到 `Secrets and variables` → `Actions`
4. 添加以下两个密钥：

**第一个密钥:**
- Name（名称）：`IKUUU_EMAIL`
- Secret（密钥值）：你的ikuuu邮箱地址

**第二个密钥:**
- Name（名称）：`IKUUU_PASSWORD`
- Secret（密钥值）：你的ikuuu账户密码

5. 点击 `Add secret` 保存

#### 自动运行时间

- 脚本会在每天北京时间 00:05 自动运行
- 也可以在 Actions 页面手动触发运行

## 故障排除

### 常见问题

1. **登录失败**: 检查邮箱和密码是否正确
2. **环境变量未设置**: 确保正确设置了 IKUUU_EMAIL 和 IKUUU_PASSWORD
3. **网络连接**: 确保网络连接正常，可以访问 ikuuu.one

### 获取帮助

如果遇到问题，请检查运行日志中的错误信息，或提交Issue获取帮助。

## 免责声明

本脚本仅供学习和个人使用，请遵守ikuuu.one的服务条款。使用本脚本所产生的任何后果由使用者自行承担。