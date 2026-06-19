-- Ex:6 Event resource summary 

select e.event_id, e.title, count(r.resource_id) as resource_count
from Events e
left join Resources r on e.event_id = r.event_id
group by e.event_id, e.title;