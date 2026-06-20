-- HANDS-ON 4
-- Query Optimization - Indexes, EXPLAIN & N+1 Problem


-- TASK 1: BASELINE PERFORMANCE

-- Step 48: EXPLAIN Query

EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;


-- Step 49 & 50: Document Findings

-- Before indexes:
-- MySQL may perform full table scans on students, enrollments or courses depending on optimizer choice.
-- Rows examined and execution plan can be viewed in the JSON output returned by EXPLAIN.



-- TASK 2: ADD INDEXES AND COMPARE PLANS

-- Step 51: B-Tree Index on enrollment_year

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);


-- Step 52: Composite UNIQUE Index

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);


-- Step 53: Index on course_code

CREATE INDEX idx_courses_course_code
ON courses(course_code);


-- Step 54: Re-run EXPLAIN

EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- After indexes:
-- Query plan should show index usage.
-- Compare rows examined before and after indexing.
-- Index scan is preferred over full table scan for large datasets.


-- Step 55: Partial Index Alternative for MySQL

-- MySQL does not support partial indexes.
-- Use a normal index instead.

CREATE INDEX idx_enrollment_grade
ON enrollments(grade);