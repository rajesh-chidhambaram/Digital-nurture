-- HANDS-ON 1
-- Schema Design & Core SQL

-- TASK 1: CREATE DATABASE
CREATE DATABASE IF NOT EXISTS college_db;

USE college_db;


-- CREATE TABLE: departments
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

 
-- CREATE TABLE: students
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

 
-- CREATE TABLE: courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

 
-- CREATE TABLE: enrollments
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),

    CONSTRAINT fk_enrollment_student
    FOREIGN KEY (student_id)
    REFERENCES students(student_id),

    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);

 
-- CREATE TABLE: professors
CREATE TABLE professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

 
-- TASK 2: NORMALIZATION ANALYSIS
 
-- 1NF ANALYSIS
-- All columns contain atomic values.
-- Each field stores a single value only.
-- Example: first_name contains one name.
-- If multiple phone numbers were stored in one column,
-- it would violate First Normal Form (1NF).

-- 2NF ANALYSIS
-- All tables use a single-column primary key.
-- Every non-key attribute depends completely on its primary key.
-- In enrollments, enrollment_date and grade depend on the
-- enrollment record itself and not partially on any key.

-- 3NF ANALYSIS
-- No transitive dependencies exist in the schema.
-- Department information is stored separately in departments.
-- Students store only department_id as a foreign key.
-- If dept_name were stored in students,
-- it would create redundancy and violate 3NF.

-- ENROLLMENTS TABLE 3NF ANALYSIS
-- enrollment_id uniquely identifies each enrollment record.
-- student_id identifies the student enrolled.
-- course_id identifies the course enrolled.
-- enrollment_date depends directly on enrollment_id.
-- grade depends directly on enrollment_id.
-- No non-key attribute depends on another non-key attribute.
-- Therefore, the enrollments table satisfies 3NF.

 
-- TASK 3: ALTER AND EXTEND THE SCHEMA
 
-- Step 10: Add phone_number column

ALTER TABLE students
ADD COLUMN phone_number VARCHAR(15);

-- Step 11: Add max_seats column

ALTER TABLE courses
ADD COLUMN max_seats INT DEFAULT 60;

-- Step 12: Add CHECK constraint on grade

ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (
    grade IN ('A','B','C','D','F')
    OR grade IS NULL
);

-- Step 13: Rename hod_name to head_of_dept

ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- Step 14: Drop phone_number column

ALTER TABLE students
DROP COLUMN phone_number;

 
-- VERIFICATION QUERIES
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
DESCRIBE professors;
