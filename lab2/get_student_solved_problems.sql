select
	task.id, task.name, task.description, task.code
from
	task
	inner join task_student on task_student.id_task = task.id
where
	task_student.id_student  = 2 and task_student.status = true;