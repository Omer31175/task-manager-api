![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)  
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)  
![Uvicorn](https://img.shields.io/badge/Uvicorn-Running-success?logo=uvicorn)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 🧠 Portfolio Task Manager API

A clean, production-ready FastAPI project built to showcase backend development skills, including RESTful design, data validation, timestamps, and modular architecture.

📦 Note: Currently implemented in a single file (`main.py`) for simplicity. Easily modularized into `models.py`, `routes.py`, etc. — future-ready for scaling.

## 🚀 Features
- Create, read, update, delete tasks
- UTC timestamps for tracking changes
- Filter tasks by completion status
- Validation to prevent empty or duplicate titles
- CORS-ready for frontend integration
- Auto-generated Swagger documentation

## 📁 Project Structure
TaskManagerAPI/
├── app/
│ └── main.py # FastAPI app with all logic
├── venv/ # Virtual environment
├── README.md # This documentation
├── requirements.txt # Project dependencies
└── screenshots/ # Screenshots for README

bash
Copy code

## 📦 Installation
```bash
git clone https://github.com/yourusername/task-manager-api
cd TaskManagerAPI

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows

# Install dependencies
pip install -r requirements.txt
▶️ Run the API
bash
Copy code
uvicorn app.main:app --reload
Now visit:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📮 API Endpoints
Method	Endpoint	Description
GET	/tasks	List all tasks or filter by completed
POST	/tasks	Create a new task
PATCH	/tasks/{id}	Update an existing task
DELETE	/tasks/{id}	Delete a task

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
⚠️ Example Validation Error
If you try to create a task with an empty title:

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
📸 Screenshots

![Swagger UI](https://github.com/Omer31175/task-manager-api/blob/main/screenshots/swagger.png?raw=true)
![ReDoc](https://github.com/Omer31175/task-manager-api/blob/main/screenshots/redoc.png?raw=true)
![GET /tasks](https://github.com/Omer31175/task-manager-api/blob/main/screenshots/get_tasks.png?raw=true)
![POST /tasks](https://github.com/Omer31175/task-manager-api/blob/main/screenshots/post_task.png?raw=true)
![PATCH /tasks](https://github.com/Omer31175/task-manager-api/blob/main/screenshots/update_task.png?raw=true)
![DELETE /tasks](https://github.com/Omer31175/task-manager-api/blob/main/screenshots/delete_task.png?raw=true)



🙌 Credits
Built by Noushad — backend developer focused on automation, FastAPI, and clean architecture.
