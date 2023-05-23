from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL



class Task_student(Base):
    __tablename__ = 'task_student'

    id_student = Column(Integer, ForeignKey('student.id'), primary_key=True)
    id_task = Column(Integer, ForeignKey('task.id'), primary_key=True)
    status = Column(Boolean, default=False)


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id'))
    name = Column(String(255), index=True)
    description = Column(String, nullable=True)
    code = Column(String, nullable=True)
    id_task_difficulty = Column(Integer, ForeignKey('task_difficulty.id'))
    tests = relationship('Test', backref='task')
    #students = db.relationship('Student', secondary=task_student, backref='tasks')  # (many-to-many)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    tasks = relationship('Task', backref='category') # one-to-many


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    id_group = Column(GUID, ForeignKey('group.id'))
    git = Column(String)
    tasks = relationship('Task',
                            secondary="task_student",
                            backref='students')


class Task_difficulty(Base):
    __tablename__ = 'task_difficulty'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    tasks = relationship('Task', backref='difficulty')


teacher_groups = Table('teacher_groups',
                          Base.metadata,
                          Column('id_teacher', Integer, ForeignKey('teacher.id')),
                          Column('id_group', Integer, ForeignKey('group.id'))
                          )


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    groups = relationship('Group', secondary=teacher_groups, backref='teachers')


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    students = relationship('Student', backref='group')


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    id_task = Column(Integer, ForeignKey('task.id'))
    name = Column(String)
    code = Column(String)


#
#
# //////////////////////////////////////////WITH_GUID_AS_ID:///////////////////////////////////////////
#
#
# from .database import Base
# from sqlalchemy import TIMESTAMP, Column, String, Boolean, ForeignKey, Table
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
#
#
#
# class Task_student(Base):
#     __tablename__ = 'task_student'
#
#     id_student = Column(GUID, ForeignKey('student.id'), primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     id_task = Column(GUID, ForeignKey('task.id'), primary_key=True)
#     status = Column(Boolean, default=False)
#
#
# class Task(Base):
#     __tablename__ = 'task'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     id_category = Column(GUID, ForeignKey('category.id'))
#     name = Column(String(255), index=True)
#     description = Column(String, nullable=True)
#     code = Column(String, nullable=True)
#     id_task_difficulty = Column(GUID, ForeignKey('task_difficulty.id'))
#     tests = relationship('Test', backref='task')
#     #students = db.relationship('Student', secondary=task_student, backref='tasks')  # (many-to-many)
#
#
# class Category(Base):
#     __tablename__ = 'category'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     name = Column(String(255))
#     tasks = relationship('Task', backref='category') # one-to-many
#
#
# class Student(Base):
#     __tablename__ = 'student'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     name = Column(String(255))
#     id_group = Column(GUID, ForeignKey('group.id'))
#     git = Column(String)
#     tasks = relationship('Task',
#                             secondary="task_student",
#                             backref='students')
#
#
# class Task_difficulty(Base):
#     __tablename__ = 'task_difficulty'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     name = Column(String(255))
#     tasks = relationship('Task', backref='difficulty')
#
#
# teacher_groups = Table('teacher_groups',
#                           Base.metadata,
#                           Column('id_teacher', GUID, ForeignKey('teacher.id')),
#                           Column('id_group', GUID, ForeignKey('group.id'))
#                           )
#
#
# class Teacher(Base):
#     __tablename__ = 'teacher'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     name = Column(String(255))
#     groups = relationship('Group', secondary=teacher_groups, backref='teachers')
#
#
# class Group(Base):
#     __tablename__ = 'group'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     name = Column(String(255))
#     students = relationship('Student', backref='group')
#
#
# class Test(Base):
#     __tablename__ = 'test'
#
#     id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
#     id_task = Column(GUID, ForeignKey('task.id'))
#     name = Column(String)
#     code = Column(String)
#
#
