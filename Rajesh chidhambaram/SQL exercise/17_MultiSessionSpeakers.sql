-- Ex:17 Multi-Session Speakers

select speaker_name, count(session_id) as total_sessions
from Sessions
group by speaker_name
having count(session_id) > 1;