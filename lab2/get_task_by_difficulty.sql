select task.id, task.name, task.description, task.code
from
	task
	--inner join task_difficulty on task.id_task_difficulty = task_difficulty.id
where task.id_task_difficulty = 1;