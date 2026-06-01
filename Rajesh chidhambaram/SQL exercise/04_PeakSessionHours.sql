-- Ex:4 Peak session hours

select e.event_id, e.title, count(s.session_id) AS session_count
from Events e
join Sessions s on e.event_id = s.event_id
where time(s.start_time) between '10:00:00' and '12:00:00'
group by e.event_id, e.title;
