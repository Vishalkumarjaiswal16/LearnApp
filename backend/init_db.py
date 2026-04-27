import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.executescript("""
        DROP TABLE IF EXISTS Progress;
        DROP TABLE IF EXISTS Learning_Paths;
        DROP TABLE IF EXISTS Assessments;
        DROP TABLE IF EXISTS Enrollments;
        DROP TABLE IF EXISTS Courses;
        DROP TABLE IF EXISTS Students;

        CREATE TABLE Students (
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            age INT
        );

        CREATE TABLE Courses (
            course_id INT PRIMARY KEY,
            course_name VARCHAR(100),
            difficulty_level VARCHAR(50)
        );

        CREATE TABLE Enrollments (
            enrollment_id INT PRIMARY KEY,
            student_id INT,
            course_id INT,
            enrollment_date DATE,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        CREATE TABLE Assessments (
            assessment_id INT PRIMARY KEY,
            course_id INT,
            marks INT,
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        CREATE TABLE Learning_Paths (
            path_id INT PRIMARY KEY,
            student_id INT,
            recommended_course VARCHAR(100),
            FOREIGN KEY (student_id) REFERENCES Students(student_id)
        );

        CREATE TABLE Progress (
            progress_id INT PRIMARY KEY,
            student_id INT,
            course_id INT,
            completion_percentage INT,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        );

        INSERT INTO Students VALUES (1, 'Kushagra', 'kush@gmail.com', 20);
        INSERT INTO Courses VALUES (101, 'DBMS', 'Intermediate');
        INSERT INTO Enrollments VALUES (1, 1, 101, '2026-03-20');
        INSERT INTO Assessments VALUES (1, 101, 85);
        INSERT INTO Learning_Paths VALUES (1, 1, 'Advanced DBMS');
        INSERT INTO Progress VALUES (1, 1, 101, 75);
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()