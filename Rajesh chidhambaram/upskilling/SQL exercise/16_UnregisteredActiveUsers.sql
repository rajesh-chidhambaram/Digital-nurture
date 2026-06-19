-- Ex:16 Unregistered Active Users

select u.user_id, u.full_name
from Users u
left join Registrations r on u.user_id = r.user_id
where u.registration_date >= curdate() - interval 30 day
and r.registration_id is null;