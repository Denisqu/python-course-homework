from model import *
import random

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


    group_b52 = Group(name="b-52")
    # groups
    db.session.add_all([
        group_b52,
        Group(name="a-21"),
        Group(name="a-93")
    ])
    db.session.commit()

    # students
    for i in range(1, 10):
        student = Student(name=f"StudentName{i}", git=f"github.com/link{i}", id_group=((i % 3) + 1))
        db.session.add(student)
        db.session.commit()
        student.tasks.extend(db.session.query(Task).all()[0:i])
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


