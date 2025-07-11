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

### 1. 获取 Cookie

1. 打开浏览器，访问 [ikuuu.one](https://ikuuu.one)
2. 登录你的账户
3. 按 F12 打开开发者工具
4. 切换到 Network (网络) 标签
5. 刷新页面或执行任意操作
6. 找到任意请求，查看 Request Headers
7. 复制完整的 Cookie 值

### 2. 设置环境变量

#### 方法一：临时设置（推荐用于测试）

##### Windows (PowerShell)
```powershell
# 设置环境变量（当前会话有效）
$env:COOKIE_DATA = "你的完整Cookie字符串"

# 验证设置是否成功
echo $env:COOKIE_DATA
```

##### Windows (CMD)
```cmd
REM 设置环境变量（当前会话有效）
set COOKIE_DATA=你的完整Cookie字符串

REM 验证设置是否成功
echo %COOKIE_DATA%
```

##### Linux/macOS
```bash
# 设置环境变量（当前会话有效）
export COOKIE_DATA="你的完整Cookie字符串"

# 验证设置是否成功
echo $COOKIE_DATA
```

#### 方法二：永久设置（推荐用于长期使用）

##### Windows 系统级设置

**方法 2.1：通过系统设置界面**
1. 右键点击"此电脑" → "属性"
2. 点击"高级系统设置"
3. 点击"环境变量"
4. 在"用户变量"区域点击"新建"
5. 变量名：`COOKIE_DATA`
6. 变量值：你的完整Cookie字符串
7. 点击"确定"保存
8. **重新启动命令行工具或VS Code**

**方法 2.2：通过PowerShell永久设置**
```powershell
# 设置用户级环境变量（永久）
[Environment]::SetEnvironmentVariable("COOKIE_DATA", "你的完整Cookie字符串", "User")

# 验证设置（需要重新打开PowerShell）
[Environment]::GetEnvironmentVariable("COOKIE_DATA", "User")
```

##### Linux/macOS 永久设置

**For Bash (.bashrc/.bash_profile)**
```bash
# 编辑配置文件
nano ~/.bashrc

# 在文件末尾添加以下行
export COOKIE_DATA="你的完整Cookie字符串"

# 保存并退出，然后重新加载配置
source ~/.bashrc
```

**For Zsh (.zshrc)**
```bash
# 编辑配置文件
nano ~/.zshrc

# 在文件末尾添加以下行
export COOKIE_DATA="你的完整Cookie字符串"

# 保存并退出，然后重新加载配置
source ~/.zshrc
```

#### 方法三：使用 .env 文件（高级用户）

1. 在项目根目录创建 `.env` 文件：
```env
COOKIE_DATA=你的完整Cookie字符串
```

2. 安装 python-dotenv：
```bash
pip install python-dotenv
```

3. 修改 main.py，在文件开头添加：
```python
from dotenv import load_dotenv
load_dotenv()  # 加载 .env 文件
```

4. 将 `.env` 文件添加到 `.gitignore`：
```gitignore
.env
```

#### 验证环境变量设置

运行以下Python代码验证环境变量是否正确设置：

```python
import os

cookie = os.getenv('COOKIE_DATA')
if cookie:
    print(f"环境变量设置成功！Cookie长度: {len(cookie)} 字符")
    print(f"Cookie前50个字符: {cookie[:50]}...")
else:
    print("❌ 环境变量未设置或为空")
```

#### 常见设置问题

1. **环境变量设置后无效**:
   - 重新启动命令行工具或IDE
   - 确保没有拼写错误
   - 检查Cookie字符串是否包含特殊字符需要转义

2. **Cookie字符串包含特殊字符**:
   ```bash
   # 使用单引号包裹（Linux/macOS）
   export COOKIE_DATA='cookie_name=value; other_cookie="special chars"'
   ```

3. **VS Code中环境变量无效**:
   - 重启VS Code
   - 或在VS Code终端中重新设置

#### 方法四：GitHub Actions 环境变量配置

如果你想在GitHub Actions中自动运行这个脚本，需要配置Repository Secrets：

##### 1. 设置GitHub Repository Secrets

1. 进入你的GitHub仓库页面
2. 点击 `Settings`（设置）标签
3. 在左侧菜单中找到 `Secrets and variables` → `Actions`
4. 点击 `New repository secret`
5. Name（名称）：`COOKIE_DATA`
6. Secret（密钥值）：粘贴你的完整Cookie字符串
7. 点击 `Add secret` 保存

##### 2. 创建GitHub Actions工作流

在项目根目录创建 `.github/workflows/auto-checkin.yml` 文件：

```yaml
name: 自动签到

on:
  schedule:
    # 每天北京时间早上8点执行（UTC时间0点）
    - cron: '0 0 * * *'
  workflow_dispatch: # 允许手动触发

jobs:
  checkin:
    runs-on: ubuntu-latest
    
    steps:
    - name: 检出代码
      uses: actions/checkout@v4
      
    - name: 设置Python环境
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 安装依赖
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifulsoup4
        
    - name: 执行签到脚本
      env:
        COOKIE_DATA: ${{ secrets.COOKIE_DATA }}
      run: python main.py
```

##### 3. 高级配置选项

**3.1 多时区支持**
```yaml
name: 多时区自动签到

on:
  schedule:
    # 每天多个时间点尝试签到，提高成功率
    - cron: '0 0 * * *'   # UTC 00:00 (北京时间 08:00)
    - cron: '0 12 * * *'  # UTC 12:00 (北京时间 20:00)
  workflow_dispatch:

jobs:
  checkin:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    - name: 设置Python环境
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 安装依赖
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifulsoup4
        
    - name: 执行签到
      env:
        COOKIE_DATA: ${{ secrets.COOKIE_DATA }}
        TZ: 'Asia/Shanghai'  # 设置时区
      run: |
        echo "当前时间: $(date)"
        python main.py
```

**3.2 添加通知功能**
```yaml
name: 签到并通知

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  checkin:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    - name: 设置Python环境
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 安装依赖
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifulsoup4
        
    - name: 执行签到
      id: checkin
      env:
        COOKIE_DATA: ${{ secrets.COOKIE_DATA }}
      run: |
        python main.py 2>&1 | tee output.log
        echo "result=$(cat output.log)" >> $GITHUB_OUTPUT
        
    - name: 发送邮件通知（可选）
      if: always()
      uses: dawidd6/action-send-mail@v3
      with:
        server_address: smtp.gmail.com
        server_port: 587
        username: ${{ secrets.EMAIL_USERNAME }}
        password: ${{ secrets.EMAIL_PASSWORD }}
        subject: ikuuu签到结果
        body: |
          签到执行结果：
          ${{ steps.checkin.outputs.result }}
        to: your-email@example.com
        from: GitHub Actions
```

##### 4. 环境变量安全最佳实践

**4.1 使用Organization Secrets（组织级密钥）**
- 如果你有多个相关仓库，可以在Organization级别设置Secrets
- 路径：Organization Settings → Secrets and variables → Actions

**4.2 使用Environment Secrets（环境级密钥）**
```yaml
jobs:
  checkin:
    runs-on: ubuntu-latest
    environment: production  # 使用特定环境
    
    steps:
    - name: 执行签到
      env:
        COOKIE_DATA: ${{ secrets.COOKIE_DATA }}
      run: python main.py
```

**4.3 密钥轮换策略**
- 定期更新Cookie值
- 设置提醒，建议每月检查一次
- 监控Actions执行日志，及时发现认证失败

##### 5. 调试和监控

**5.1 启用调试日志**
```yaml
- name: 执行签到（调试模式）
  env:
    COOKIE_DATA: ${{ secrets.COOKIE_DATA }}
    ACTIONS_STEP_DEBUG: true
  run: |
    echo "开始执行签到脚本..."
    python main.py
    echo "签到脚本执行完成"
```

**5.2 添加状态检查**
```yaml
- name: 检查Cookie有效性
  env:
    COOKIE_DATA: ${{ secrets.COOKIE_DATA }}
  run: |
    if [ -z "$COOKIE_DATA" ]; then
      echo "❌ COOKIE_DATA环境变量未设置"
      exit 1
    else
      echo "✅ COOKIE_DATA环境变量已设置，长度: ${#COOKIE_DATA}"
    fi
```

##### 6. 故障排除

**常见GitHub Actions问题：**

1. **Secret未设置或为空**
   ```yaml
   - name: 验证Secrets
     run: |
       if [ -z "${{ secrets.COOKIE_DATA }}" ]; then
         echo "❌ COOKIE_DATA secret未设置"
         exit 1
       fi
   ```

2. **时区问题**
   ```yaml
   - name: 显示时区信息
     run: |
       echo "UTC时间: $(date -u)"
       echo "北京时间: $(TZ='Asia/Shanghai' date)"
   ```

3. **依赖安装失败**
   ```yaml
   - name: 安装依赖（带重试）
     run: |
       for i in {1..3}; do
         pip install requests beautifulsoup4 && break
         echo "重试安装依赖 ($i/3)"
         sleep 5
       done
   ```

## 使用方法

### 直接运行
```bash
python main.py
```

### 输出示例
```
签到结果: 签到成功，获得了 5MB 流量
剩余流量: 2.5 GB
今日已用: 150 MB
```

## 文件结构

```
ikuuu/
│
├── main.py          # 主程序文件
└── README.md        # 项目说明文档
```

## 代码说明

### 主要函数

- `checkin()`: 执行自动签到操作
- `get_user_traffic()`: 获取用户流量使用情况

### 安全特性

- 使用环境变量存储敏感信息
- 模拟真实浏览器的 User-Agent
- 包含适当的 Referer 和 Origin 头部

## 注意事项

⚠️ **重要提醒**:

1. **Cookie 安全**: 请妥善保管你的 Cookie 信息，不要泄露给他人
2. **使用频率**: 建议每天只运行一次，避免频繁请求
3. **账户安全**: 如果发现异常情况，请及时更换密码
4. **合规使用**: 请遵守网站的使用条款和服务协议

## 故障排除

### 常见问题

1. **签到失败**: 
   - 检查 Cookie 是否正确
   - 确认账户是否正常
   - 检查网络连接

2. **流量信息获取失败**:
   - 网站页面结构可能发生变化
   - Cookie 可能已过期

3. **环境变量未设置**:
   - 确保正确设置了 `COOKIE_DATA` 环境变量
   - 重新启动终端或IDE

## 自动化部署

### 使用 Windows 任务计划程序

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器为每日执行
4. 操作设置为启动程序: `python`
5. 参数填写: `main.py`
6. 起始位置填写脚本所在目录

### 使用 Linux Cron

```bash
# 编辑 crontab
crontab -e

# 添加每日早上8点执行的任务
0 8 * * * cd /path/to/ikuuu && python main.py
```

## 更新日志

- **v1.0.0**: 初始版本，支持基本签到和流量查询功能

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 免责声明

本脚本仅供学习和个人使用，请遵守相关网站的使用条款。使用本脚本所产生的任何后果由使用者自行承担。

## 许可证

MIT License

---

如果这个项目对你有帮助，请给个 ⭐️ Star 支持一下！
