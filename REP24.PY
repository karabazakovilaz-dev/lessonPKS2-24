# Задача: Система управления колледжем
# Ты пишешь программу, которая помогает колледжу управлять студентами
# Система должна уметь:

def add_students(students):
    name = input("Введите имя: ").title().strip()
    if name in students:
        print("Такой студент уже существует")
        return
    group = input("Введите название группы: ").strip()
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Введите только цифры для возраста")
        return
    students[name] = {"группа": group, "возраст": age}
    print(f"Студент {name} добавлен")

def add_subject(subjects):
    name = input("Введите название предмета: ").strip()
    if name in subjects:
        print("Такой предмет уже есть")
        return
    teacher = input("Введите имя и фамилию преподавателя: ").strip()
    subjects[name] = teacher
    print(f"Предмет {name} добавлен. Преподаватель: {teacher}")

def add_mark(students, subjects):
    student_name = input("Введите имя студента: ").title().strip()
    if student_name not in students:
        print("Студент не найден")
        return
    subject_name = input("Введите название предмета: ").strip()
    if subject_name not in subjects:
        print("Предмет не найден")
        return
    try:
        mark = float(input("Введите оценку: "))
    except ValueError:
        print("Введите корректную оценку")
        return
    if "оценки" not in students[student_name]:
        students[student_name]["оценки"] = {}
    students[student_name]["оценки"][subject_name] = mark
    print(f"Оценка {mark} добавлена для студента {student_name} по предмету {subject_name}")

def show_student(students, subjects):
    student_name = input("Введите имя студента: ").title().strip()
    if student_name not in students:
        print("Студент не найден")
        return
    student_info = students[student_name]
    print(f"Имя: {student_name}")
    print(f"Возраст: {student_info['возраст']}")
    print(f"Группа: {student_info['группа']}")
    if "оценки" in student_info and student_info["оценки"]:
        print("Оценки:")
        for subj, mark in student_info["оценки"].items():
            teacher = subjects.get(subj, "Неизвестен")
            print(f"  {subj} (Преподаватель: {teacher}): {mark}")
    else:
        print("Оценок нет")

def calculate_average(students):
    student_name = input("Введите имя студента: ").title().strip()
    if student_name not in students:
        print("Студент не найден")
        return
    marks = students[student_name].get("оценки", {})
    if not marks:
        print("Нет оценок для вычисления среднего")
        return
    average = sum(marks.values()) / len(marks)
    print(f"Средний балл студента {student_name}: {average:.2f}")

def show_top_students(students):
    group_name = input("Введите название группы: ").strip()
    group_students = [(name, s) for name, s in students.items() if s["группа"] == group_name]
    if not group_students:
        print("Группа не найдена или в группе нет студентов")
        return

    def avg(s): 
        marks = s.get("оценки", {})
        return sum(marks.values()) / len(marks) if marks else 0
    top_students = sorted(group_students, key=lambda item: avg(item[1]), reverse=True)[:3]
    print(f"Топ-студенты группы {group_name}:")
    for name, student in top_students:
        average = avg(student)
        print(f"  {name} - Средний балл: {average:.2f}")

def expel_students(students):
    to_expel = []
    for name, data in list(students.items()):
        marks = data.get("оценки", {})
        if marks:
            average = sum(marks.values()) / len(marks)
            if average < 50:
                to_expel.append((name, average))
    for student_name, average in to_expel:
        print(f"Студент {student_name} отчислен (Средний балл: {average:.2f})")
        del students[student_name]

students = {}
subjects = {}

while True:
    print("""
        1. Регистрировать студентов (имя, возраст, группа)
        2. Добавить предмет (название, преподаватель)
        3. Назначать оценки студентам по предметам
        4. Вычислять средний балл студента
        5. Показать топ-студентов группы
        6. Проверить кто подлежит отчислению (если средний балл < 50)
        7. Показать информацию о студенте
        0. Выход
    """)
    choice = input("Выберите действие: ").strip()
    if choice == "1":
        add_students(students)
    elif choice == "2":
        add_subject(subjects)
    elif choice == "3":
        add_mark(students, subjects)
    elif choice == "4":
        calculate_average(students)
    elif choice == "5":
        show_top_students(students)
    elif choice == "6":
        expel_students(students)
    elif choice == "7":
        show_student(students, subjects)
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Вводите от 0 до 7")