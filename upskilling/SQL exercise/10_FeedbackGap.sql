-- Ex:10 Feedback Gap

select e.event_id,e.title
from Events e
join Registrations r on e.event_id = r.event_id
left join Feedback f on e.event_id = f.event_id
where f.feedback_id is null
group by e.event_id, e.title;