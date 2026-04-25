<div align="center">

# 🎓 Online Learning Platform with Adaptive Learning

**A full-stack web application for managing students, courses, and tracking adaptive learning progress — built with React.js + Flask + MySQL.**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![React](https://img.shields.io/badge/Frontend-React.js-61DAFB?logo=react&logoColor=white)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)

</div>

---

## 📸 Screenshots

| Home Page | Dashboard |
|-----------|----------|
| ![Home](frontend/public/Screenshot%202026-04-09%20104220.png) | ![Dashboard](frontend/public/Screenshot%202026-04-09%20104149.png) |

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#1-database-setup)
  - [Backend Setup](#2-backend-setup)
  - [Frontend Setup](#3-frontend-setup)
- [API Endpoints](#-api-endpoints)
- [Environment Variables](#-environment-variables)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🔭 Overview

The **Online Learning Platform with Adaptive Learning** is a full-stack CRUD web application that enables educators and administrators to manage students, courses, and track each student's learning progress. The platform features a modern dark-themed UI with adaptive difficulty levels for courses, giving students a personalized learning experience.

> Built as a hands-on project to demonstrate full-stack development skills using a Python/Flask REST API backend connected to a React.js SPA frontend.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Learning Dashboard** | Centralized hub to view all students, enrolled courses, and completion progress |
| 👥 **Student Management** | Register and manage students with ID, name, email, and age |
| 📚 **Course Management** | Add and manage courses with dynamic adaptive difficulty levels |
| 📈 **Progress Tracking** | Link students to courses and monitor completion percentage in real time |
| 🎨 **Modern Dark UI** | Sleek custom dark theme designed with pure CSS — no UI framework dependency |
| 🔀 **Responsive Navigation** | Fast client-side routing between views using React Router DOM |

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|-----------|----------------------|
| React.js | UI component library |
| React Router DOM | Client-side routing |
| Pure CSS | Custom dark theme styling |

### Backend
| Technology | Version | Purpose |
|------------|---------|--------|
| Python | 3.x | Runtime environment |
| Flask | 3.0.3 | REST API framework |
| Flask-CORS | 5.0.0 | Cross-Origin Resource Sharing |
| Flask-MySQLdb | 2.0.0 | MySQL database connector |

### Database
| Technology | Purpose |
|------------|--------|
| MySQL | Relational data storage |

---

## 📁 Project Structure

```
Online-Learning-Platform-with-Adaptive-Learning/
├── backend/
│   ├── routes/                  # All Flask route blueprints
│   ├── app.py                   # Flask app entry point
│   ├── config.py                # DB configuration (credentials)
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── public/                  # Static assets & screenshots
│   └── src/
│       ├── components/          # Reusable React components
│       ├── pages/               # Page-level React views
│       ├── api.js               # Axios/fetch API service layer
│       ├── App.js               # Root component with routing
│       ├── App.css              # Global styles
│       └── index.js             # React DOM entry point
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone https://github.com/Vishalkumarjaiswal16/Online-Learning-Platform-with-Adaptive-Learning.git
cd Online-Learning-Platform-with-Adaptive-Learning
```

### 1. Database Setup

Log into MySQL and create a database:

```sql
CREATE DATABASE learning_platform;
```

Then update `backend/config.py` with your credentials:

```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'learning_platform'
```

### 2. Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask server
python app.py
```

> The backend API will be running at **http://localhost:5000**

### 3. Frontend Setup

Open a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

> The frontend will be running at **http://localhost:3000**

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/students` | Fetch all students |
| `POST` | `/students` | Register a new student |
| `PUT` | `/students/<id>` | Update student details |
| `DELETE` | `/students/<id>` | Delete a student |
| `GET` | `/courses` | Fetch all courses |
| `POST` | `/courses` | Add a new course |
| `GET` | `/progress` | Fetch all progress records |
| `POST` | `/progress` | Link student to course with progress |

---

## 🔐 Environment Variables

Create or update `backend/config.py` — **never commit credentials to version control**.

```python
# backend/config.py
MYSQL_HOST = 'localhost'
MYSQL_USER = '<your_db_user>'
MYSQL_PASSWORD = '<your_db_password>'
MYSQL_DB = '<your_database_name>'
```

> ⚠️ Make sure `config.py` is listed in `.gitignore` if it contains real credentials.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Vishal Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-Vishalkumarjaiswal16-181717?style=flat-square&logo=github)](https://github.com/Vishalkumarjaiswal16)


---

<div align="center">

*If you found this project helpful, consider giving it a ⭐ star!*

</div>
