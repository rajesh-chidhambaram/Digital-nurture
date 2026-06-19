-- Ex:12 Event with Maximum Sessions

select e.event_id, e.title, count(s.session_id) as session_count
from Events e
join Sessions s on e.event_id = s.event_id
group by e.event_id, e.title
having count(s.session_id) = (
    select max(session_count)
    from (
        select count(session_id) as session_count
        from Sessions
        group by event_id
    ) t
);