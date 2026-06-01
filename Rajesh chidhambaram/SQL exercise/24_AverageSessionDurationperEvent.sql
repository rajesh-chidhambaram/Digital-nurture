-- Ex:24 Average Session Duration per Event

select e.event_id, e.title,
avg(timestampdiff(minute, s.start_time, s.end_time)) as avg_duration
from Events e
join Sessions s on e.event_id = s.event_id
group by e.event_id, e.title;