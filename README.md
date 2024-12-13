<div align="center">

# 🤖 AI Chat Assistant System

[English](README.md) | [繁體中文](README.zh-TW.md)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-orange)](https://deepmind.google/technologies/gemini/)

An integrated AI conversation system supporting multiple AI models including Azure OpenAI and Google Gemini,
with database query and chart generation capabilities.

[Features](#features) •
[Quick Start](#setup) •
[Documentation](#module-documentation) •
[Contributing](#contributing)

</div>

---

## Features

- Multiple AI Model Integration
  - Azure OpenAI
  - Google Gemini
- SQLite Database Operations
- Chart Generation
- API Integration
- Text Processing Tools

## System Requirements

- Python 3.x
- Dependencies (See requirements.txt)

## Setup

1. Create a `.env` file with the following settings:

```
AZURE_OPENAI_ENDPOINT=Your Azure endpoint
AZURE_OPENAI_API_KEY=Your Azure API key
AZURE_OPENAI_DEPLOYMENT=Your deployment name
GOOGLE_API_KEY=Your Google API key
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Module Documentation

### 1. AI Model Integration
- `azure_open_ai.py`: Azure OpenAI service integration
- `gemini_calling.py`: Google Gemini service integration

### 2. Database Operations
- `sql_db.py`: SQLite database operation tools
- `get_db.py`: Database query examples

### 3. Utility Modules
- `tool/text_processing.py`: Text processing tools
- `tool/chart.py`: Chart generation tools

### 4. Core Functions
- `core/azure_functions.py`: Azure function definitions
- `basic_functions.py`: Basic function implementations

## Usage

1. Start Azure OpenAI conversation:

```bash
python azure_open_ai.py
```

2. Start Google Gemini conversation:

```bash
python gemini_calling.py
```

## Database Structure

The system uses SQLite database located at `./db/data.db` with the following tables:
- my_table
- my_table1

## Notes

- Ensure all API keys are properly configured before use
- Verify table structure before database operations
- Chart generation requires matplotlib support

## License

MIT License
