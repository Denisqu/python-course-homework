select task.id, task.name, task.description, task.code
from
	task
	-- inner join category on task.id_category = category.id
where task.id_category = 1;