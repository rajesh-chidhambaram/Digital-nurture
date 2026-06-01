-- Ex:11 Daily New User Count

select registration_date, count(user_id) as user_count
from Users
where registration_date >= curdate() - interval 7 day
group by registration_date
order by registration_date;