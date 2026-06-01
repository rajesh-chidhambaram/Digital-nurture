-- Ex:13 Average Rating per City

select e.city, avg(f.rating) as average_rating
from Events e
join Feedback f on e.event_id = f.event_id
group by e.city;