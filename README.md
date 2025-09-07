![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-Running-success?logo=uvicorn)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 🧠 Portfolio Task Manager API

A clean, production-ready FastAPI project demonstrating CRUD operations, timestamps, input validation, and modular architecture.

---

## 🚀 Features

- ✅ Create, read, update, delete tasks
- 🕒 UTC timestamps for creation and updates
- 🔍 Filter tasks by completion status
- 🛡️ Input validation to prevent empty or duplicate titles
- 🌐 CORS-ready for frontend integration
- 📄 Auto-generated Swagger and ReDoc documentation

---

## 📁 Project Structure

TaskManagerAPI/
├── app/
│ └── main.py # FastAPI app with all logic
├── venv/ # Virtual environment
├── screenshots/ # Folder containing screenshots
├── README.md # Project documentation (this file)
└── requirements.txt # Project dependencies

yaml
Copy code

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YourUsername/task-manager-api.git
cd task-manager-api

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload
Visit:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📮 API Endpoints
Method	Endpoint	Description
GET	/tasks	List all tasks or filter by status
POST	/tasks	Create a new task
PATCH	/tasks/{id}	Update an existing task
DELETE	/tasks/{id}	Delete a task by ID

📊 Example Requests
Create a Task

bash
Copy code
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Build portfolio", "completed": false}'
Update a Task

bash
Copy code
curl -X PATCH http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
Delete a Task

bash
Copy code
curl -X DELETE http://127.0.0.1:8000/tasks/1
⚠️ Validation Error Example
json
Copy code
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "title"],
      "msg": "Title must not be empty"
    }
  ]
}
📸 Screenshots (relative paths)
## 📸 Screenshots

Here’s a visual walkthrough of the Task Manager API in action:

### 🧭 Swagger UI — Interactive API Explorer
FastAPI’s built-in Swagger interface lets you test endpoints, view schemas, and explore your API live.

![Swagger UI](screenshots/swagger.png)

### 📘 ReDoc — Clean API Documentation
ReDoc provides a structured view of your OpenAPI schema, including models, parameters, and responses.

![ReDoc](screenshots/redoc.png)

### 📥 GET /tasks — Retrieve All Tasks
Returns a list of tasks with timestamps and completion status.

![GET /tasks](screenshots/get_tasks.png)

### 🆕 POST /tasks — Create a New Task
Accepts a JSON payload to create a task with validation.

![POST /tasks](screenshots/post_task.png)

### ✏️ PATCH /tasks — Update a Task
Modifies task fields like title or completion status.

![PATCH /tasks](screenshots/update_task.png)

### 🗑️ DELETE /tasks — Remove a Task
Deletes a task by ID with confirmation response.

![DELETE /tasks](screenshots/delete_task.png)

🙌 Credits
Built by Noushad — backend developer focused on automation, FastAPI, and clean architecture.


