# 🧠 Task Manager API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-Running-success?logo=uvicorn)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A clean, production-ready FastAPI project built to showcase backend development skills — including RESTful design, data validation, timestamps, and modular architecture.



## 📑 Table of Contents

- [Features](#🚀-features)
- [Installation](#📦-installation)
- [API Endpoints & Screenshots](#📮-api-endpoints--screenshots)
  - [GET /tasks](#🧭-get-tasks-—-list-all-tasks)
  - [POST /tasks](#🆕-post-tasks-—-create-a-new-task)
  - [PATCH /tasks/{id}](#✏️-patch-tasksid-—-update-a-task)
  - [DELETE /tasks/{id}](#🗑️-delete-tasksid-—-remove-a-task)
  - [Swagger UI](#🧭-swagger-ui-—-interactive-api-explorer)
  - [ReDoc](#📘-redoc-—-clean-api-documentation)
- [Validation Error Example](#⚠️-validation-error-example)
- [Credits](#🙌-credits)



## 🚀 Features

- ✅ Full CRUD operations for task management
- 🕒 UTC timestamps for creation and updates
- 🔍 Filter tasks by completion status
- 🛡️ Input validation to prevent empty or duplicate titles
- 🌐 CORS-enabled for frontend integration
- 📄 Auto-generated Swagger and ReDoc documentation



## 📦 Installation


# Clone the repository
git clone https://github.com/Omer31175/task-manager-api
cd task-manager-api

# Create a virtual environment
python -m venv venv
# Activate
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload
Visit the docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📮 API Endpoints & Screenshots
🧭 GET /tasks — List All Tasks
Retrieve all tasks or filter by completion status.

Example Request:



curl -X GET http://127.0.0.1:8000/tasks
Screenshot:


🆕 POST /tasks — Create a New Task
Create a task with validation. Titles must be unique.

Example Request:



curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Build portfolio", "completed": false}'
Screenshot:


✏️ PATCH /tasks/{id} — Update a Task
Update task fields like title or completion status. Partial updates supported.

Example Request:



curl -X PATCH http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
Screenshot:


🗑️ DELETE /tasks/{id} — Remove a Task
Delete a task by ID.

Example Request:



curl -X DELETE http://127.0.0.1:8000/tasks/1
Screenshot:


🧭 Swagger UI — Interactive API Explorer
FastAPI’s built-in Swagger interface lets you test endpoints live.



📘 ReDoc — Clean API Documentation
Structured view of OpenAPI schema including models, parameters, and responses.



⚠️ Validation Error Example
If you try to create a task with an empty title:



{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "title"],
      "msg": "Title must not be empty"
    }
  ]
}
🙌 Credits
Built by Noushad — backend developer focused on automation, FastAPI, and clean architecture.

