-- Ex:18 Resource Availability Check

select e.event_id, e.title
from Events e
left join Resources r on e.event_id = r.event_id
where r.resource_id is null;