-- Ex:08 Sessions per Upcoming Event


select e.event_id, e.title, count(s.event_id) as session_count
from Events e
left join Sessions s on e.event_id = s.event_id
where e.status = 'upcoming'
group by e.event_id, e.title;
