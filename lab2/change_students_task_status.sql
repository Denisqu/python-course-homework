update 
	task_student t1
set
	status = false
from
	task_student t
where
	t.id_student = 1
	and task.id = 1