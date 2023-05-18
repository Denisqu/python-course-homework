from flask import Flask
from typing import List
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import *
# from sqlalchemy import

# https://editor.ponyorm.com/user/Denis1902/test/python


db = SQLAlchemy()


# one to many tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database-legacy
# many-to-many tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends-legacy

# todo: понять как сделать связку двух стобцов форен ки ключом
# task_student = db.Table("task_student",
#                         db.Column('id_student', db.Integer, db.ForeignKey('student.id')),
#                         db.Column('id_task', db.Integer, db.ForeignKey('task.id')),
#                         db.Column('status', db.Boolean, default=False)
#                         )

class Task_student(db.Model):
    __tablename__ = 'task_student'

    id_student = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    id_task = db.Column(db.Integer, db.ForeignKey('task.id'), primary_key=True)
    status = db.Column(db.Boolean, default=False)


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(255), index=True)
    description = db.Column(db.String, nullable=True)
    code = db.Column(db.String, nullable=True)
    id_task_difficulty = db.Column(db.Integer, db.ForeignKey('task_difficulty.id'))
    #students = db.relationship('Student', secondary=task_student, backref='tasks')  # (many-to-many)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    tasks = db.relationship('Task', backref='category') # one-to-many


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    id_group = db.Column(db.Integer, db.ForeignKey('group.id'))
    git = db.Column(db.String())
    tasks = db.relationship('Task',
                            secondary="task_student",
                            backref='students')


class Task_difficulty(db.Model):
    __tablename__ = 'task_difficulty'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    tasks = db.relationship('Task', backref='difficulty')


teacher_groups = db.Table('teacher_groups',
                          db.Column('id_teacher', db.Integer, db.ForeignKey('teacher.id')),
                          db.Column('id_group', db.Integer, db.ForeignKey('group.id'))
                          )


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    groups = db.relationship('Group', secondary=teacher_groups, backref='teachers')


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    students = db.relationship('Student', backref='group')







