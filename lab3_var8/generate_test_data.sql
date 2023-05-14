
insert into service_type (base_price, name) values
	(1000, 'консультация'),
	(1550, 'ведение дела в суде');

insert into case_domain (name) values
	('гражданские'),
	('уголовные');

insert into case_type (name) values
	('жилищные'),
	('семейные'),
	('убийства');

insert into client (name) values
	('Anna L.'),
	('Anton K.'),
	('Mike W.');


insert into lawyer (price_multiplier, "name") values
	(1, 'Kostya M.'),
	(5, 'Andrew U.');

insert into lawyer_service_type (id_service_type, id_lawyer) values
	(1, 1),
	(1, 2),
	(2, 2);

insert into "case" (description, id_lawyer, id_client, id_case_type, id_case_domain, status, id_service_type) values
	('Описание консультации...', 1, 1, 1, 1, true, 1),
	('Описание дела...', 2, 2, 2, 2, false, 2);











/*
insert into "group" (name) values
	('A-21'),
	('S-02');

insert into student (name, id_group, git) values
	('Andrew L.', 1, 'https://github.com/Andrusha/homework'),
	('Mattew M.', 1, 'https://github.com/boss/homework'),
	('Anna W.', 2, 'https://github.com/Andrusha/homework');

insert into "task_difficulty" (name) values
	('Легкая'),
	('Нормальная'),
	('Сложная'),
	('Очень сложная');

insert into category (name) values
	('Математика. Простые числа.'),
	('Алгоритмы. Быстрая сортировка'),
	('Алгоритмы. Поиск кратчайшего пути'),
	('Сети. Понятие сокета.');


insert into task (id_category, name, description, code, id_task_difficulty) values
	(1, 'Решить задачу 1 ...', 'Описание 1 ...', 'Код... 1', 1),
	(2, 'Решить задачу 2 ...', 'Описание 2 ...', 'Код... 2', 2),
	(3, 'Решить задачу 3 ...', 'Описание 3 ...', 'Код... 3', 3),
	(3, 'Решить задачу 4 ...', 'Описание 4 ...', 'Код... 4', 4);

insert into task_student (id_student, id_task, status) values
	(2, 2, False),
	(2, 3, True),
	(2, 4, False),
	(3, 1, True),
	(3, 2, False),
	(3, 3, False),
	(3, 4, False);

insert into teacher (name) values
	('Boris L.'),
	('Anna M.');
	
insert into teacher_groups (id_teacher, id_group) values
	(2, 2),
	(2, 1);
*/
	