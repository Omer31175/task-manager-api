# 📝 Task Manager API

A simple and modern **Task Manager API** built with **FastAPI** and **SQLite**.  
This project demonstrates CRUD operations, API documentation, and clean project structure — great for learning and as a portfolio showcase.

---

## 🚀 Features
- ✅ Create, read, update, and delete tasks  
- 📂 FastAPI automatic docs (Swagger & ReDoc)  
- 🗄️ SQLite database (lightweight & file-based)  
- 🖼️ API documentation screenshots included  

---

## ⚙️ Installation

```bash
# 1️⃣ Clone repository
git clone https://github.com/Omer31175/task-manager-api.git
cd task-manager-api

# 2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run server
uvicorn app.main:app --reload
API will be available at:
👉 http://127.0.0.1:8000/docs (Swagger UI)
👉 http://127.0.0.1:8000/redoc (ReDoc)

📸 Screenshots
🧭 Swagger UI — Interactive API Explorer


📘 ReDoc — Clean API Documentation


📥 GET /tasks — Retrieve All Tasks


🆕 POST /tasks — Create a New Task


✏️ PATCH /tasks — Update a Task


🗑️ DELETE /tasks — Remove a Task


📊 Example Requests
🆕 Create a Task
bash
Copy code
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Build portfolio", "completed": false}'
✏️ Update a Task
bash
Copy code
curl -X PATCH http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
🗑️ Delete a Task
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
📌 Tech Stack
FastAPI — high-performance web framework

SQLite — lightweight relational database

Uvicorn — ASGI server for running FastAPI

📜 License
This project is licensed under the MIT License.
Feel free to use and adapt it for your own portfolio or projects 🚀




