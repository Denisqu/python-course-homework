select
	id_client,
	c2."name" 
from
	"case" c 
	inner join client c2 on c.id_client = c2.id
where
	c.id_service_type = 1;