-- Ex:07 Low feedback alert

select u.full_name, e.title, f.rating, f.comments
from Feedback f
join Users u on u.user_id = f.user_id
join Events e on f.event_id = e.event_id
where f.rating<3;