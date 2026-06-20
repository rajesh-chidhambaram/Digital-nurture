-- Ex:20 User Engagement Index

select u.user_id, u.full_name,
count(distinct r.event_id) as attended_events, count(distinct f.feedback_id) as feedback_count
from Users u
left join Registrations r on u.user_id = r.user_id
left join Feedback f on u.user_id = f.user_id
group by u.user_id, u.full_name;