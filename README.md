<div align="center">

# 🎓 Online Learning Platform with Adaptive Learning

**A full-stack web application for managing students, courses, and tracking adaptive learning progress — built with React.js, Flask, and SQLite.**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![React](https://img.shields.io/badge/Frontend-React.js-61DAFB?logo=react&logoColor=white)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend & Database Setup](#1-backend--database-setup)
  - [Frontend Setup](#2-frontend-setup)
- [API Endpoints](#-api-endpoints)

---

## 🔭 Overview

The **Online Learning Platform with Adaptive Learning** is a full-stack CRUD web application that enables educators and administrators to manage students, courses, and track each student's learning progress. 

The platform recently underwent a major architectural and design overhaul. It now features a modern "Glassmorphism" deep-slate UI with responsive CSS Grids and has been migrated to **SQLite** for a seamless, zero-configuration local development experience.

---

## 📸 Screenshots

### Home Page
![Home Page](frontend/public/Screenshot%202026-04-09%20104149.png)

### Learning Dashboard
![Learning Dashboard - Add Forms](frontend/public/Screenshot%202026-04-09%20104208.png)

![Learning Dashboard - Overview](frontend/public/Screenshot%202026-04-09%20104220.png)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Learning Dashboard** | Centralized hub to view all students, enrolled courses, and completion progress in a responsive grid layout. |
| 👥 **Student Management** | Register and manage students with ID, name, email, and age. |
| 📚 **Course Management** | Add and manage courses with dynamic adaptive difficulty levels. |
| 📈 **Progress Tracking** | Link students to courses and monitor completion percentage in real time. |
| 🎨 **Modern Glassmorphism UI** | Sleek custom deep slate dark theme with frosted glass effects and animated transitions. |
| ⚡ **Zero-Config Database** | Runs completely locally on SQLite. No separate database server installation required. |

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|-----------|----------------------|
| React.js | UI component library |
| React Router DOM | Client-side routing |
| Pure CSS | Custom Glassmorphism UI styling |

### Backend
| Technology | Version | Purpose |
|------------|---------|--------|
| Python | 3.x | Runtime environment |
| Flask | 3.0.3 | REST API framework |
| Flask-CORS | 5.0.0 | Cross-Origin Resource Sharing |
| SQLite3 | Built-in | Relational data storage |

---

## 📁 Project Structure

```
Online-Learning-Platform-with-Adaptive-Learning/
├── backend/
│   ├── app.py                   # Flask app entry point & routes
│   ├── init_db.py               # SQLite database initialization script
│   ├── database.db              # Auto-generated SQLite database
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/          # Reusable React components
│   │   ├── pages/               # Page-level React views (Home, Dashboard)
│   │   ├── App.js               # Root component with routing
│   │   └── App.css              # Global styles & Glassmorphism UI
│   └── package.json             # Node dependencies
├── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your system:
- [Python 3.x](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/)

### Clone the Repository

```bash
git clone https://github.com/Vishalkumarjaiswal16/Online-Learning-Platform-with-Adaptive-Learning.git
cd Online-Learning-Platform-with-Adaptive-Learning
```

### 1. Backend & Database Setup

The backend is completely self-contained and uses SQLite.

```bash
cd backend

# Create and activate virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize the SQLite database (this creates database.db and seeds data)
python init_db.py

# Start the Flask server
python app.py
```

> The backend API will be running at **http://localhost:5000**

### 2. Frontend Setup

Open a new terminal window:

```bash
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

> The frontend will be running at **http://localhost:3000** (or another port if 3000 is occupied).

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check (Backend Running) |
| `GET` | `/students` | Fetch all students |
| `POST` | `/add-student` | Register a new student |
| `GET` | `/courses` | Fetch all courses |
| `POST` | `/add-course` | Add a new course |
| `GET` | `/progress` | Fetch all progress records |
| `POST` | `/add-progress`| Add new progress record |

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.