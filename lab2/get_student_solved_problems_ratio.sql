select
	cast(solved_count.coalesce as float) / nullif(not_solved_count.coalesce + solved_count.coalesce, 0) as ratio,
	solved_count.coalesce,
	not_solved_count.coalesce
from
(
	select * from coalesce((
		select
			count(status) as solved
		from
			task_student ts
		where 
			ts.id_student = 1
		group by
			ts.status
		having
			status = true
			), 0)
) as solved_count,
(
		select * from coalesce ((
		select
			count(status) as not_solved
		from
			task_student ts
		where 
			ts.id_student = 1
		group by
			ts.status
		having
			status = false 
			), 0)
) as not_solved_count;
