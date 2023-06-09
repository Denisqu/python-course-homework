from model import *
import random
from sqlalchemy import func
from sqlalchemy.sql.expression import false, true


def create_test_data():
    # task difficulty
    medium = Task_difficulty(name="medium")
    db.session.add_all([
        Task_difficulty(name="easy"),
        medium,
        Task_difficulty(name="hard"),
        Task_difficulty(name="hard+")
    ])
    db.session.commit()

    # task category
    math_category = Category(name="Math")
    network_category = Category(name="Algorithms")
    db.session.add_all([
        math_category,
        network_category,
        Category(name="CS"),
        Category(name="Network")
    ])
    db.session.commit()

    # task
    for i in range(0, 10):
        db.session.add(Task(name=f"TaskName{i}", description=f"TaskDescription{i}",
                            code=f"TaskCode{i}", category=math_category,
                            difficulty=medium))
        db.session.commit()

    # test
    db.session.add(Test(id_task=1, name='Tests for something #1', code='Code...'))
    db.session.commit()

    group_b52 = Group(name="b-52")
    # groups
    db.session.add_all([
        group_b52,
        Group(name="a-21"),
        Group(name="a-93")
    ])
    db.session.commit()

    # students
    for i in range(1, 35):
        student = Student(name=f"StudentName{i}", git=f"github.com/link{i}", id_group=((i % 3) + 1))
        db.session.add(student)
        db.session.commit()
        student.tasks.extend(db.session.query(Task).all()[0:(i % 3) + 1])
        db.session.add(student)
        db.session.commit()

    # set some students tasks to be in status "Done" by random
    students_tasks = db.session.query(Task_student).all()
    for i in students_tasks:
        if random.random() < 0.45:
            i.status = True
            db.session.add(i)
            db.session.commit()

    # teachers
    for i in range(0, 3):
        t = Teacher(name=f"TeacherName{i}")
        db.session.add(t)
        db.session.commit()
        t.groups.append(group_b52)
        db.session.add(t)
        db.session.commit()


def get_all_students_in_group(group):
    return db.session.query(Student).filter(Student.id_group == group.id)


def get_all_tasks():
    return db.session.query(Task).all()


def get_student_tasks(student):
    _query = db.session.query(Task, Task_student.status)\
        .join(Task_student, Task_student.id_task == Task.id)\
        .filter(student.id == Task_student.id_student).all()
    return _query


def get_students_with_tasks_from_group(group):
    result = {}

    _query = db.session.query(Student, Task_student) \
        .filter(Student.id_group == group.id) \
        .filter(Task_student.id_student == Student.id) \
        .all()
    print(_query)

    return result


def get_students_with_ratio_from_group(group):
    _query_student_done_tasks = db.session.query(Student, Task_student) \
        .join(Task_student) \
        .filter(Student.id_group == group.id) \
        .filter(Task_student.id_student == Student.id) \
        .filter(Task_student.status == true()).subquery()

    _query_done_tasks = db.session.query(Student,
                                         func.count(_query_student_done_tasks.c.id_task).label('done_count')) \
        .select_from(Student) \
        .outerjoin(_query_student_done_tasks, _query_student_done_tasks.c.id_student == Student.id) \
        .filter(Student.id_group == group.id) \
        .group_by(Student.id).all()

    _query_all_tasks = db.session.query(Student, func.count(Task_student.id_task)) \
        .join(Task_student, isouter=True) \
        .filter(Student.id_group == group.id) \
        .filter(Task_student.id_student == Student.id) \
        .group_by(Student.id) \
        .all()

    result = []
    for i, elem in enumerate(_query_done_tasks):
        s = elem[0], elem[1], _query_all_tasks[i][1]
        result.append(s)

    return result


def add_new_task_to_a_students(students, task):
    for student in students:
        student.tasks.append(task)
        db.session.add(student)
    db.session.commit()


