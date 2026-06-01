-- Ex:14 Most Registered Events

select e.event_id, e.title, count(r.registration_id) as registration_count
from Events e
join Registrations r on e.event_id = r.event_id
group by e.event_id, e.title
order by registration_count desc
limit 3;