-- Ex:22 Duplicate Registrations Check

select user_id, event_id, count(*) as duplicate_count
from Registrations
group by user_id, event_id
having count(*) > 1;