-- Ex:09 Organizer Event Summary

select u.full_name, e.status, count(e.event_id) as total_count
from Users u
join Events e on u.user_id = e.organizer_id
group by u.full_name, e.status
order by u.full_name;