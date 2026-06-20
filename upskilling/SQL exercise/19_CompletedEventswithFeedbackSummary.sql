-- Ex:19 Completed Events with Feedback Summary

select e.event_id, e.title, count(distinct r.registration_id) as total_registrations, avg(f.rating) as average_rating
from Events e
left join Registrations r on e.event_id = r.event_id
left join Feedback f on e.event_id = f.event_id
where e.status = 'completed'
group by e.event_id, e.title;