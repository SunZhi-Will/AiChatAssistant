<div align="center">

# 🤖 AI 對話助手系統

[English](README.md) | [繁體中文](README.zh-TW.md)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-orange)](https://deepmind.google/technologies/gemini/)

這是一個整合了多種AI模型的對話系統，支援Azure OpenAI、Google Gemini等服務，  
並具備資料庫查詢和圖表生成功能。

[功能特點](#功能特點) •
[快速開始](#環境設置) •
[使用說明](#主要模組說明) •
[參與貢獻](#參與貢獻)

</div>

---

## 功能特點

- 支援多種AI模型整合
  - Azure OpenAI
  - Google Gemini
- SQLite資料庫操作
- 圖表生成功能
- API整合
- 文字處理工具

## 系統需求

- Python 3.x
- 相關套件依賴（請參考 requirements.txt）

## 環境設置

1. 建立 `.env` 檔案，包含以下設定：

```
AZURE_OPENAI_ENDPOINT=您的Azure端點
AZURE_OPENAI_API_KEY=您的Azure API金鑰
AZURE_OPENAI_DEPLOYMENT=您的部署名稱
GOOGLE_API_KEY=您的Google API金鑰
```

2. 安裝相依套件：

```bash
pip install -r requirements.txt
```

## 主要模組說明

### 1. AI模型整合
- `azure_open_ai.py`: Azure OpenAI服務整合
- `gemini_calling.py`: Google Gemini服務整合

### 2. 資料庫操作
- `sql_db.py`: SQLite資料庫操作工具
- `get_db.py`: 資料庫查詢範例

### 3. 工具模組
- `tool/text_processing.py`: 文字處理工具
- `tool/chart.py`: 圖表生成工具

### 4. 核心功能
- `core/azure_functions.py`: Azure功能定義
- `basic_functions.py`: 基礎功能實作

## 使用方式

1. 啟動Azure OpenAI對話：

```bash
python azure_open_ai.py
```

2. 啟動Google Gemini對話：

```bash
python gemini_calling.py
```


## 資料庫結構

系統使用SQLite資料庫，位於 `./db/data.db`，包含以下表格：
- my_table
- my_table1

## 注意事項

- 使用前請確保已正確設置所有API金鑰
- 資料庫操作前請確認資料表結構
- 圖表生成功能需要matplotlib支援

## 授權說明

MIT License
