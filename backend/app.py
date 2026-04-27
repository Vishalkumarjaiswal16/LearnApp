from flask import Flask, g
import sqlite3
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return "Backend Running 🚀"

@app.route('/courses')
def get_courses():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM Courses")
    data = [dict(row) for row in cur.fetchall()]
    return {"data": data}

@app.route('/progress')
def get_progress():
    cur = get_db().cursor()
    cur.execute("""
        SELECT s.name, c.course_name, p.completion_percentage
        FROM Progress p
        JOIN Students s ON p.student_id = s.student_id
        JOIN Courses c ON p.course_id = c.course_id
    """)
    data = [dict(row) for row in cur.fetchall()]
    return {"data": data}

@app.route('/students', methods=['GET'])
def get_students():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM Students")
    data = cur.fetchall()

    students = []
    for row in data:
        students.append({
            "id": row['student_id'],
            "name": row['name'],
            "email": row['email'],
            "age": row['age']
        })

    return {"data": students}

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json

    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO Students (student_id, name, email, age) VALUES (?, ?, ?, ?)",
        (data['id'], data['name'], data['email'], data['age'])
    )
    db.commit()

    return {"message": "Student added successfully"}

@app.route('/add-course', methods=['POST'])
def add_course():
    data = request.json
    db = get_db()
    cur = db.cursor()
    # Assuming course_id, course_name, difficulty_level
    cur.execute(
        "INSERT INTO Courses (course_id, course_name, difficulty_level) VALUES (?, ?, ?)",
        (data['id'], data['course_name'], data['difficulty_level'])
    )
    db.commit()
    return {"message": "Course added successfully"}

@app.route('/add-progress', methods=['POST'])
def add_progress():
    data = request.json
    db = get_db()
    cur = db.cursor()
    # Assuming student_id, course_id, completion_percentage
    cur.execute(
        "INSERT INTO Progress (student_id, course_id, completion_percentage) VALUES (?, ?, ?)",
        (data['student_id'], data['course_id'], data['completion_percentage'])
    )
    db.commit()
    return {"message": "Progress added successfully"}

import os

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=debug_mode)