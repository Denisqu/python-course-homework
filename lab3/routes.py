from main import app
from flask import render_template
from model import *
import query

@app.route('/test', methods=['GET'])
def test():
    return 'it works!'


@app.route('/group/<int:group_id>')
def group(group_id):
    group_query = db.session.query(Group).filter(Group.id == group_id).one()
    students_with_tasks = query.get_students_with_ratio_from_group(group_query)
    group_ratio = 0
    for i in students_with_tasks:
        group_ratio += float(i[1]) / i[2]
    group_ratio = group_ratio / len(students_with_tasks)

    return render_template('group.html', students_w_tasks=students_with_tasks,
                           group_ratio=group_ratio,
                           group=group_query)


# todo: give list of all students
@app.route('/students')
def students():
    pass

# todo: give list of all student tasks
@app.route('/student_tasks/<int:student_id>')
def student_tasks():
    pass

# todo: print task db:
@app.route('/tasks_db')
def tasks_db():
    pass
