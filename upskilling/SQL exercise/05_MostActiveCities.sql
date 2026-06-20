-- Ex:5 Most Active Cities 

select u.city, count(distinct r.user_id) as total_registrations
from Users u
join Registrations r on u.user_id = r.user_id
group by u.city
order by total_registrations desc
limit 5;