# 🧠 Task Manager API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-Running-success?logo=uvicorn)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
A clean, production-ready FastAPI project built to showcase backend development skills — including RESTful design, data validation, timestamps, and modular architecture.

## 🚀 Features

- ✅ Full CRUD operations for task management
- 🕒 UTC timestamps for creation and updates
- 🔍 Filter tasks by completion status
- 🛡️ Input validation to prevent empty or duplicate titles
- 🌐 CORS-enabled for frontend integration
- 📄 Auto-generated Swagger and ReDoc documentation

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Omer31175/task-manager-api
cd task-manager-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows

# Install dependencies
pip install -r requirements.txt

uvicorn main:app --reload

Visit the docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc




