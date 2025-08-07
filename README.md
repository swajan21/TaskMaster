
# TaskMaster – Personal Task Manager 📝

TaskMaster is a Django-based personal task management web application designed to help users efficiently manage their daily activities. It offers a clean and intuitive interface for creating, updating, deleting, and viewing tasks, along with functionality for filtering, sorting, and highlighting deadlines. The goal is to boost productivity and ensure that users never miss an important task.

---

## 🚀 Features

### ✅ User Registration & Authentication
- Secure user registration and login/logout functionality

### 📋 Task CRUD (Create, Read, Update, Delete)
- Create tasks with title, description, due date, priority, and completion status
- Update and delete existing tasks
- Each user can access only their own tasks

### 🧾 Task Fields
- Title
- Description
- Due date & time
- Priority level (Low, Medium, High)
- Status (Pending, Completed)
- User association (foreign key)

### 🔍 Filtering & Search
- Filter tasks by status and priority
- Search tasks by title or description

### ⏰ Overdue Task Highlighting
- Overdue tasks are visually highlighted for quick identification

### 📱 Responsive UI
- Built with Bootstrap for responsive design
- Includes a navigation bar, task table, and filters, create task, user, logout, login, Register

### 💬 User Feedback
- Uses Django messages framework to show success/error notifications

### 🔒 Secure Access Control
- Only logged-in users can access task features
- Users can only access their own data

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite 
- **Authentication:** Django built-in auth

---

## 📁 Project Structure

```
taskmaster/
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
|   └── static/
├── manage.py
└── README.md
```

---

## ⚙️ Setup Instructions
   ```bash
   cd taskmaster
   taskmaster> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   source env/bin/activate  # On Windows: env\Scripts\activate
   python manage.py runserver
   ```
**Open in browser:**
   Visit `http://127.0.0.1:8000/`
## Register: 
   Use short name and create strong password 8 cheracter
## Login:
   user name and password  
   
## 📸 Screenshot

![Create Task](https://github.com/swajan21/TaskMaster/blob/main/taskmaster/Screenshot/Create%20Task.png))


- You can use this project as a foundation for more advanced task management tools.
- Customize styles using Bootstrap or your own CSS.
- Extend features like recurring tasks, collaboration, or notifications.

---


