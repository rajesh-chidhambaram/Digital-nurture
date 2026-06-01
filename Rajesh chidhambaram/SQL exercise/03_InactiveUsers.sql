-- Ex:3 Inactive users

SELECT u.user_id, u.full_name,
MAX(r.registration_date) AS last_registration
FROM Users u 
LEFT JOIN Registrations r ON u.user_id = r.user_id
GROUP BY u.user_id, u.full_name 
HAVING last_registration IS NULL OR last_registration < DATE_SUB(CURDATE(), INTERVAL 90 DAY);