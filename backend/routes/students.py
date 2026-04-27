from app import app, get_db
from flask import jsonify

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

    return jsonify(students)