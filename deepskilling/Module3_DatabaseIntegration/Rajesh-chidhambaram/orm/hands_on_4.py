import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = conn.cursor()

print("Version 1 : N+1 Problem")

start = time.time()

query_count = 1
# Step 56 - 58
cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for enrollment in enrollments:
    student_id = enrollment[1]

    cursor.execute(
        "SELECT first_name,last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    cursor.fetchone()
    query_count += 1

end = time.time()

print(f"Queries Executed : {query_count}")
print(f"Time Taken : {end-start:.6f} seconds")


print("\nVersion 2 : JOIN Solution")

start = time.time()

cursor.execute("""
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
""")

rows = cursor.fetchall()

end = time.time()

print(f"Queries Executed : 1")
print(f"Time Taken : {end-start:.6f} seconds")

cursor.close()
conn.close()

"""
Step 59

If there are 10,000 enrollments:

N+1 Approach:
1 query to fetch enrollments
10,000 queries to fetch student data

Total = 10,001 queries

JOIN Approach:
1 query only

N+1 generates 10,000 extra database round trips.
This significantly impacts performance in production.
"""