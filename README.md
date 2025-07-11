# ikuuu 自动签到脚本

这是一个用于 ikuuu.one 网站的自动签到脚本，可以帮助用户自动完成每日签到并查看流量使用情况。

## 功能特性

- 🎯 **自动签到**: 自动完成 ikuuu.one 的每日签到
- 📊 **流量查询**: 查看剩余流量和今日已用流量
- 🔒 **安全认证**: 使用环境变量存储敏感的 Cookie 信息
- 📱 **用户代理**: 模拟真实浏览器访问，避免被检测

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

### 获取 Cookie

1. 打开浏览器，访问 [ikuuu.one](https://ikuuu.one)
2. 登录你的账户
3. 按 F12 打开开发者工具
4. 切换到 Network (网络) 标签
5. 刷新页面或执行任意操作
6. 找到任意请求，查看 Request Headers
7. 复制完整的 Cookie 值

### GitHub Actions 自动化配置

本项目使用GitHub Actions实现自动化签到，无需手动运行，完全托管在云端。

### 设置GitHub Repository Secrets

1. 进入你的GitHub仓库页面
2. 点击 `Settings`（设置）标签
3. 在左侧菜单中找到 `Secrets and variables` → `Actions`
4. 点击 `New repository secret`
5. Name（名称）：`COOKIE_DATA`
6. Secret（密钥值）：粘贴你的完整Cookie字符串
7. 点击 `Add secret` 保存
