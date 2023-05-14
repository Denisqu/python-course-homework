
with students_ratio as (
select 
	s.id,
	(
	select
		cast(solved_count.coalesce as float) / nullif(not_solved_count.coalesce + solved_count.coalesce, 0) as ratio
	from
	(
		select * from coalesce((
			select
				count(status) as solved
			from
				task_student ts
			where 
				ts.id_student = s.id
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
				ts.id_student = s.id
			group by
				ts.status
			having
				status = false 
			), 0)
	) as not_solved_count) as ratio
from
	"group" g 
	inner join student s on g.id = s.id_group
where
	g.id = 1
)
select
	sum(coalesce(ratio, 0)) / count(id) as group_ratio
from
	students_ratio;
	







