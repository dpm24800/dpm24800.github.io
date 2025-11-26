CREATE DATABASE UniversityDB;

-- Use the database
USE UniversityDB;

-- Students Table
-- (MySQL doesn’t have UUID by default, so we store as CHAR(36))
CREATE TABLE Students (
    student_id      CHAR(36) PRIMARY KEY,     -- UUID
    full_name       VARCHAR(120) NOT NULL,
    major           VARCHAR(50),
    email           VARCHAR(120) UNIQUE,
    gpa             FLOAT CHECK (gpa >= 0 AND gpa <= 4),
    admission_year  YEAR,
    birthdate       DATE,
    metadata        JSON
);

-- Courses Table
-- (MySQL doesn't support XML natively, so we use TEXT to store XML-like data)
CREATE TABLE Courses (
    course_id       CHAR(6) PRIMARY KEY,
    course_name     VARCHAR(150) NOT NULL,
    credits         SMALLINT NOT NULL,
    syllabus        TEXT,
    course_outline  TEXT        -- XML stored as text
);

-- Enrollments Table
CREATE TABLE Enrollments (
    enrollment_id   BIGINT PRIMARY KEY AUTO_INCREMENT,
    student_id      CHAR(36) NOT NULL,
    course_id       CHAR(6) NOT NULL,
    grade           CHAR(2),
    semester        VARCHAR(10),
    attendance      DECIMAL(5,2),
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Professors Table
CREATE TABLE Professors (
    prof_id        INT AUTO_INCREMENT PRIMARY KEY,
    full_name      VARCHAR(100) NOT NULL,
    department     VARCHAR(50),
    salary         DECIMAL(12,2),
    join_date      DATE,
    profile        JSON,
    location       GEOMETRY      -- spatial type
);

-- CourseAssignments Table
CREATE TABLE CourseAssignments (
    assignment_id  INT AUTO_INCREMENT PRIMARY KEY,
    prof_id        INT NOT NULL,
    course_id      CHAR(6) NOT NULL,
    semester       VARCHAR(10),
    is_active      BOOLEAN DEFAULT TRUE,

    FOREIGN KEY (prof_id) REFERENCES Professors(prof_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
