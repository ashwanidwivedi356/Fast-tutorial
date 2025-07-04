🚀 FastAPI CRUD Example
This is a simple FastAPI project that demonstrates basic CRUD operations using Pydantic models and an in-memory list.

📋 Features
✅ Welcome root route

📥 Create (POST) a new item

📄 Read (GET) all items

✏️ Update (PUT) an item by ID

❌ Delete (DELETE) an item by ID

🛠️ Tech Stack
Python 3.8+

FastAPI

Pydantic

Uvicorn (for running the server)

📦 Installation
bash
Copy
Edit
# Clone this repository
git clone https://github.com/your-username/fastapi-crud-example.git
cd fastapi-crud-example

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn
🚀 Running the App
bash
Copy
Edit
uvicorn main:app --reload
📌 main is the filename (main.py) and app is the FastAPI instance.

📬 API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/nums	Get all items
POST	/nums	Add a new item
PUT	/nums/{num_id}	Update item by ID
DELETE	/nums/{num_id}	Delete item by ID

🧪 Sample JSON Format
json
Copy
Edit
{
  "id": 1,
  "name": "Sample Name",
  "origin": "India"
}
🐛 Known Issues
❗ @app.get("nums") should be @app.get("/nums") (missing /)

❗ In update_num, use if num.id == num_id instead of num.id == num.id

❗ In return statements with error, use proper dict: {"error": "Num not found"}

✅ To Do
 Add persistent database (e.g. SQLite/PostgreSQL)

 Implement input validation

 Add unit tests using pytest![fastapi1](https://github.com/user-attachments/assets/d8fe6a75-9e13-4307-862a-23decb5be46d)
![fastapi](https://github.com/user-attachments/assets/2061154b-6587-440b-ad14-dabe50ba4794)
