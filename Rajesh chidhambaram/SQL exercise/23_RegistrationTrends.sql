-- Ex:23 Registration Trends

select date_format(registration_date, '%Y-%m') as month,
count(*) as registration_count
from Registrations
where registration_date >= curdate() - interval 12 month
group by date_format(registration_date, '%Y-%m')
order by month;