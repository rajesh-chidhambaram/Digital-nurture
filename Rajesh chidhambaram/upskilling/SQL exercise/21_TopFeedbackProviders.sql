-- Ex:21 Top Feedback Providers

select u.full_name, count(f.feedback_id) as total_feedbacks
from Users u
join Feedback f on u.user_id = f.user_id
group by u.full_name
order by total_feedbacks desc
limit 5;