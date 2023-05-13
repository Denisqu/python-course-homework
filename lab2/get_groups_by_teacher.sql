select 
	g.name
from
	"group" g 
	inner join teacher_groups tg on tg.id_group = g.id
	inner join teacher t on t.id = tg.id_teacher
where
	t.id = 1;