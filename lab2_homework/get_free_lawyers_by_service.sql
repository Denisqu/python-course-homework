select 
	id_lawyer,
	l."name"
from
	"case" c
	inner join lawyer l on c.id_lawyer = l.id
where
	id_lawyer not in (
		select c2.id_lawyer 
		from "case" c2
		where c2.status = true
	)
	and id_lawyer in (
		select lst.id_lawyer 
		from lawyer_service_type lst
		where lst.id_service_type = 2
	);
	