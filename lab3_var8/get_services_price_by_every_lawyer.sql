select 
	st.id as id_service,
	st.name as service_name,
	l.price_multiplier * st.base_price as calculated_price,
	l.name,
	l.id as id_lawyer
from
	service_type st
	inner join lawyer_service_type lst on st.id = lst.id_service_type
	inner join lawyer l on lst.id_lawyer = l.id;