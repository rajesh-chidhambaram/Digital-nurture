-- Ex:15 Event Session Time Conflict

select s1.event_id, s1.title as session1, s2.title as session2
from Sessions s1
join Sessions s2 on s1.event_id = s2.event_id
and s1.session_id < s2.session_id
where s1.start_time < s2.end_time
and s1.end_time > s2.start_time;