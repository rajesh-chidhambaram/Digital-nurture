-- HANDS-ON 3
-- Advanced SQL - Subqueries, Views & Transactions


-- TASK 1: SUBQUERIES

-- Step 35: Students enrolled in more courses than average

SELECT s.student_id,
       CONCAT(s.first_name, ' ', s.last_name) AS student_name,
       COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(course_id) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) avg_table
);


-- Step 36: Courses where all enrolled students received grade A

SELECT c.course_name,
       c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND e.grade <> 'A'
);


-- Step 37: Highest paid professor in each department

SELECT p.prof_name,
       p.salary,
       d.dept_name
FROM professors p
JOIN departments d
ON p.department_id = d.department_id
WHERE p.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);


-- Step 38: Departments with average professor salary greater than 85000

SELECT dept_name,
       avg_salary
FROM
(
    SELECT d.dept_name,
           AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) dept_avg
WHERE avg_salary > 85000;


-- TASK 2: CREATING AND USING VIEWS

-- Step 39: Student Enrollment Summary View

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade = 'A' THEN 4
                WHEN e.grade = 'B' THEN 3
                WHEN e.grade = 'C' THEN 2
                WHEN e.grade = 'D' THEN 1
                WHEN e.grade = 'F' THEN 0
            END
        ),
        2
    ) AS gpa
FROM students s
LEFT JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, student_name, d.dept_name;


-- Step 40: Course Statistics View

CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade = 'A' THEN 4
                WHEN e.grade = 'B' THEN 3
                WHEN e.grade = 'C' THEN 2
                WHEN e.grade = 'D' THEN 1
                WHEN e.grade = 'F' THEN 0
            END
        ),
        2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.course_code;


-- Step 41: Students with GPA above 3.0

SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3.0;


-- Step 42: Attempt to update through the view

UPDATE vw_student_enrollment_summary
SET student_name = 'Test User'
WHERE student_id = 1;

-- Result: Aggregate views are not updatable in MySQL.


-- Step 43: Drop and recreate views

DROP VIEW IF EXISTS vw_course_stats;

DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_cs_students AS
SELECT *
FROM students
WHERE department_id = 1
WITH CHECK OPTION;

-- WITH CHECK OPTION ensures that INSERT and UPDATE operations through the view must satisfy the view condition.



-- TASK 3: STORED PROCEDURES AND TRANSACTIONS

-- Step 44: Create Enrollment Procedure

DELIMITER $$

CREATE PROCEDURE sp_enroll_student
(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    IF EXISTS
    (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    )
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student already enrolled in this course';
    ELSE

        INSERT INTO enrollments
        (
            student_id,
            course_id,
            enrollment_date
        )
        VALUES
        (
            p_student_id,
            p_course_id,
            p_enrollment_date
        );

    END IF;

END$$

DELIMITER ;

CALL sp_enroll_student(1, 3, '2022-07-01');


-- Step 45: Department Transfer Log Table

CREATE TABLE department_transfer_log
(
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


DELIMITER $$

CREATE PROCEDURE sp_transfer_student
(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN

    DECLARE v_old_department INT;

    START TRANSACTION;

    SELECT department_id
    INTO v_old_department
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (
        student_id,
        old_department,
        new_department
    )
    VALUES
    (
        p_student_id,
        v_old_department,
        p_new_department
    );

    COMMIT;

END$$

DELIMITER ;

CALL sp_transfer_student(1, 2);


-- Step 46: Transaction Failure Test

CALL sp_transfer_student(1, 999);

-- Result: Foreign key constraint violation occurs.


-- Step 47: SAVEPOINT Example

START TRANSACTION;

INSERT INTO enrollments
(
    student_id,
    course_id,
    enrollment_date,
    grade
)
VALUES
(
    2,
    2,
    CURDATE(),
    'A'
);

SAVEPOINT first_insert;

INSERT INTO enrollments
(
    student_id,
    course_id,
    enrollment_date,
    grade
)
VALUES
(
    999,
    2,
    CURDATE(),
    'A'
);

ROLLBACK TO first_insert;

COMMIT;


-- Verification Query

SELECT *
FROM enrollments
WHERE student_id = 2
AND course_id = 2;