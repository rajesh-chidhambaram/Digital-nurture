-- Ex:25 Events Without Sessions

select e.event_id, e.title
from Events e
left join Sessions s on e.event_id = s.event_id
where s.session_id is null;