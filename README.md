# 🧠 Task Manager API

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)](https://fastapi.tiangolo.com/) 
[![Uvicorn](https://img.shields.io/badge/Uvicorn-Running-success?logo=uvicorn)](https://www.uvicorn.org/) 
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]() 
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

A clean, production-ready **FastAPI project** built to showcase backend development skills — including RESTful design, data validation, timestamps, and modular architecture.

---

## 🚀 Features

- ✅ Full CRUD operations for task management  
- 🕒 UTC timestamps for creation and updates  
- 🔍 Filter tasks by completion status  
- 🛡️ Input validation to prevent empty or duplicate titles  
- 🌐 CORS-enabled for frontend integration  
- 📄 Auto-generated Swagger and ReDoc documentation  

---

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

# Run the API
uvicorn app.main:app --reload
Visit the docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📮 API Endpoints
Method	Endpoint	Description
GET	/tasks	List all tasks or filter by status
POST	/tasks	Create a new task
PATCH	/tasks/{id}	Update an existing task
DELETE	/tasks/{id}	Delete a task by ID

📊 Example Requests
🆕 Create a Task

curl -X POST /tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Build portfolio", "completed": false}'
✏️ Update a Task

curl -X PATCH /tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
🗑️ Delete a Task

curl -X DELETE /tasks/1
⚠️ Validation Error Example

{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "title"],
      "msg": "Title must not be empty"
    }
  ]
}
📸 Screenshots (GitHub URLs)
🧭 Swagger UI — Interactive API Explorer


📘 ReDoc — Clean API Documentation


📥 GET /tasks — Retrieve All Tasks


🆕 POST /tasks — Create a New Task


✏️ PATCH /tasks — Update a Task


🗑️ DELETE /tasks — Remove a Task


🙌 Credits
Built by Noushad Omer — backend developer focused on automation, FastAPI, and clean architecture.


