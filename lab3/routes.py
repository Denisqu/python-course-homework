from main import app
from flask import render_template, request, url_for, flash, redirect
from model import *
import query


@app.route("/")
def index():
    return render_template('index.html')


#https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
#todo: Сделать форму с добавлением новой задачи для студентов группы
@app.route('/group/<int:group_id>', methods=['POST', 'GET'])
def group(group_id):
    group_query = db.session.query(Group).filter(Group.id == group_id).one()
    students_with_tasks = query.get_students_with_ratio_from_group(group_query)

    if request.method == 'POST':
        _task_id = request.form['task_id']
        _is_int = True
        try:
            _task_id = int(_task_id)
        except ValueError:
            _is_int = False
        _task = db.session.query(Task).filter(Task.id == _task_id).first()\
            if _is_int else None

        if not _task_id:
            flash('Task id is required!')
        elif not _is_int:
            flash('Task id should be an integer!')
        elif not _task:
            flash('This task does not exist!')
        else:
            query.add_new_task_to_a_students([i[0] for i in students_with_tasks], _task)
            students_with_tasks = query.get_students_with_ratio_from_group(group_query)

    group_ratio = 0
    for i in students_with_tasks:
        group_ratio += float(i[1]) / i[2]
    group_ratio = group_ratio / len(students_with_tasks)

    return render_template('group.html', students_w_tasks=students_with_tasks,
                           group_ratio=group_ratio,
                           group=group_query)


@app.route('/groups')
def groups():
    _groups = db.session.query(Group)
    return render_template('groups.html', groups=_groups)


@app.route('/student/<int:student_id>')
def student(student_id):
    _student = db.session.query(Student).filter(Student.id == student_id).first()
    _student_tasks = query.get_student_tasks(_student)
    return render_template('student_tasks.html', student_tasks=_student_tasks, student=_student)


@app.route('/tasks_db')
def tasks_db():
    tasks = query.get_all_tasks()
    return render_template('task_db.html', tasks=tasks)
