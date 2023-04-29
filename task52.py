# DONE


#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания.
# Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.


import random
import copy

class Task:
    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return f"Task: value = {self.__value}"


class Lesson:
    def __init__(self, title, task_homework, teacher):
        self.__title = title
        self.__task_homework = task_homework
        self.__teacher = teacher

    def get_homework(self):
        return self.__task_homework

    def get_title(self):
        return self.__title

    def get_teacher(self):
        return self.__teacher


class Pupil:
    def __init__(self, name, github_link):
        self.__name = name
        self.__github_link = github_link
        self.__not_completed_tasks = list()
        self.__completed_tasks = list()
        self.__verified_tasks = list()

    def get_not_completed_tasks(self):
        return self.__not_completed_tasks

    def add_new_task(self, task):
        self.__not_completed_tasks.append(task)

    def complete_task(self, task):
        try:
            self.__not_completed_tasks.remove(task)
            self.__completed_tasks.append(task)
        except ValueError:
            print(f"No such {task} in __not_completed_tasks")

    def receive_approve(self, task):
        try:
            self.__completed_tasks.remove(task)
            self.__verified_tasks.append(task)
        except ValueError:
            print(f"No such {task} in __completed_tasks")

    def receive_deny(self, task):
        try:
            self.__completed_tasks.remove(task)
            self.__not_completed_tasks.append(task)
        except ValueError:
            print(f"No such {task} in __completed_tasks")

    def send_tasks_for_verification(self, teacher):
        teacher.receive_completed_tasks(self, self.__completed_tasks)

    def __repr__(self):
        return f"Pupil {self.__name} Github: {self.__github_link} \n" \
               f" - Not completed tasks: {self.__not_completed_tasks} \n" \
               f" - Completed tasks: {self.__completed_tasks} \n" \
               f" - Verified tasks: {self.__verified_tasks}"

class Teacher:
    def __init__(self, name):
        self.__name = name
        self.__tasks_for_approve = {}

    def receive_completed_tasks(self, student, tasks):
        if self.__tasks_for_approve.get(student, None) is None:
            self.__tasks_for_approve[student] = []
        for i in tasks:
            if i in self.__tasks_for_approve[student]:
                continue
            self.__tasks_for_approve[student].append(i)

    def verify_tasks(self):
        for pupil, student_tasks in self.__tasks_for_approve.items():
            for task in student_tasks:
                rdm_value = random.randint(0, 9)
                if rdm_value > 4:
                    pupil.receive_deny(task)
                else:
                    pupil.receive_approve(task)

    def teach_lesson(self, group, title, homework):
        lesson = Lesson(title, homework, self)
        group.add_new_teached_lesson(lesson)
        group.send_homework_to_everyone(lesson)


class Group:
    def __init__(self, name):
        self.__name = name
        self.__pupils = []
        self.__teached_lessons = []

    def add_pupil(self, pupil):
        self.__pupils.append(pupil)

    def get_pupils(self):
        return self.__pupils

    def add_new_teached_lesson(self, lesson):
        self.__teached_lessons.append(lesson)

    def send_homework_to_everyone(self, lesson):
        for i in self.__pupils:
            i.add_new_task(lesson.get_homework())

    def __repr__(self):
        _repr = f"{self.__name} Pupils: \n"
        for i in self.__pupils:
            _repr += f"{i} \n"
        return _repr


if __name__ == "__main__":
    # init teacher and group
    teacher = Teacher("Alex")
    group = Group("B-52")

    # add pupils
    group.add_pupil(Pupil("Andrew", "https://github.com/Andrew/homework"))
    group.add_pupil(Pupil("Alice", "https://github.com/Alice/homework"))
    group.add_pupil(Pupil("Bob", "https://github.com/Bob/homework"))

    # teach some lessons, add new homework after each lesson
    teacher.teach_lesson(group, "Math 101", "MathBook: p. 12, ex. 1-10")
    teacher.teach_lesson(group, "English 101", "EnglishBook: p. 1, ex. 3")

    # complete all tasks for all pupils
    for pupil in group.get_pupils():
        tasks_to_complete = copy.copy(pupil.get_not_completed_tasks())
        for j in tasks_to_complete:
            pupil.complete_task(j)
        pupil.send_tasks_for_verification(teacher)

    # verify task by teacher
    teacher.verify_tasks()

    # report group status:
    print(group)


