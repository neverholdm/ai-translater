# AI Translator

基于 Python 和 DeepSeek API 开发的 AI 翻译工具。

该项目实现了一个简单的中英互译应用，支持命令行模式（CLI）和图形界面模式（GUI），通过调用 DeepSeek API 实现 AI 翻译功能。

---

## ✨ 项目功能

- ✅ 中文 → 英文翻译
- ✅ 英文 → 中文翻译
- ✅ 基于 DeepSeek API 的 AI 翻译
- ✅ 命令行交互模式（CLI）
- ✅ Tkinter 图形界面（GUI）
- ✅ 翻译历史记录保存
- ✅ 应用日志记录
- ✅ API Key 环境变量配置
- ✅ 单元测试支持

---

## 🛠 技术栈

| 技术 | 用途 |
| --- | --- |
| Python 3.11 | 项目主要开发语言 |
| DeepSeek API | AI 翻译服务 |
| OpenAI SDK | API 调用 |
| Tkinter | 图形用户界面开发 |
| python-dotenv | 环境变量管理 |
| logging | 日志记录 |
| unittest | 自动化测试 |

---

# 📁 项目结构

```
ai-translator
│
├── main.py                  # 命令行程序入口
├── gui.py                   # Tkinter 图形界面
├── translate.py             # 翻译核心逻辑
├── translate_history.py     # 翻译历史记录管理
├── logger.py                # 日志配置
│
├── test.py                  # 单元测试
│
├── requirements.txt         # 项目依赖
├── .env                     # API 配置文件
│
├── translation_history.txt  # 翻译历史记录
└── app.log                  # 应用日志
```

---

# 🚀 安装与运行

## 1. 克隆项目

```bash
git clone https://github.com/neverholdm/ai-translater.git

cd ai-translator
```

---

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 3. 配置 API Key

在项目根目录创建：

```
.env
```

填写：

```env
DEEPSEEK_API_KEY=你的API_KEY
```

项目通过环境变量读取 API Key，避免将敏感信息直接写入代码。

---

# ▶️ 使用方式

## 1. 命令行模式（CLI）

运行：

```bash
python main.py
```

示例：

```
====================
 AI Translator
====================

1. 开始翻译
2. 查看历史记录
3. 退出

请选择：
```

输入：

```
你好，世界
```

输出：

```
Hello, world.
```

---

## 2. 图形界面模式（GUI）

运行：

```bash
python gui.py
```

功能包括：

- 输入待翻译文本
- 选择源语言和目标语言
- 点击按钮进行翻译
- 查看翻译结果

---

# 🧪 自动化测试

运行：

```bash
python -m unittest
```

示例：

```
.
----------------------------------------------------------------------
Ran 1 test

OK
```

---

# 📝 数据记录

## 翻译历史

每次翻译结果会保存到：

```
translation_history.txt
```

方便查看历史翻译记录。

---

## 日志记录

程序运行日志保存到：

```
app.log
```

记录：

- 程序运行信息
- API 调用异常
- 错误信息

---

# ⚙️ 配置说明

项目使用 `.env` 文件管理 API Key。

示例：

```env
DEEPSEEK_API_KEY=xxxx
```

通过：

```python
python-dotenv
```

读取配置，提高项目安全性。

---

# 📷 项目展示

（此处添加 GUI 截图）

例如：

```
assets/
└── gui.png
```

---

# 🔮 后续计划

- [ ] 支持更多语言翻译
- [ ] 优化 GUI 界面设计
- [ ] 增加翻译历史搜索功能
- [ ] 增加程序打包
- [ ] 增加更多自动化测试
- [ ] 支持更多 AI 模型

---

# 📄 License

MIT License

---

# 👨‍💻 作者

GitHub:

https://github.com/neverholdm