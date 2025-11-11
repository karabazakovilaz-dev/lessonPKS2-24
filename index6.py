# Задача Учёта учеников с сохранением данных 
# 1 добавления ученика
# запрашивает имя, возраст, балл и любимый предмет 
# повторяерт
# длину имени (не более 16 и не мнее 3 символов)
# что возраст введен числом
# после добавлнгия  сразу сохроняет обновленный словарь в students.txt.
# 2 удаление ученика
# запрашивает имя и удоляет его если найдён
# после удаления записывают изменения в students.txt
# 3 просмотр всех учеников
# Выводит всех учеников построчно 
# Имя: aman / Возраст: 16
# Баллы: 4.8 / Любимый предмет: математика
# загружает данные  из файла перед поеазом (если файл существует)
# 4 изменение данных ученика
# запрашивает имя 
# позволяет изменить
# 1 - возраст
# 2 - балл
# 3 - любимый предмет
# после изменения сохраняет в файл
# 5 выход из программы
################################
# 1 Добавление ученика
import json
import os                                                                                 
STUDENTS_FILE = 'students.txt'
students = {}

def load_students():
    global students
    if os.path.exists(STUDENTS_FILE):
        try:
            with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
                students = json.load(f)
        except Exception:
            students = {}
    else:
        students = {}

def save_students():
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def remove_student():
    load_students()
    name = input("Введите имя ученика для удаления (Enter — отмена): ").strip()
    if name == "":
        print("Отменено.")
        return
    if name in students:
        del students[name]
        save_students()
        print(f"Ученик {name} удалён.")
    else:
        print("Ученик не найден.")

def main():
    load_students()
    while True:
        print("\n1 - Удалить ученика\n2 - Выход")
        cmd = input("Выберите действие: ").strip()
        if cmd == "1":
            remove_student()
        elif cmd == "2":
            break
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()
# ...existing code...
# filepath: c:\Users\user\Desktop\Новая папка\index6.py
# ...existing code...
import json
import os

STUDENTS_FILE = 'students.txt'
students = {}

def load_students():
    global students
    if os.path.exists(STUDENTS_FILE):
        try:
            with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
                students = json.load(f)
        except Exception:
            students = {}
    else:
        students = {}

def save_students():
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def remove_student():
    load_students()
    name = input("Введите имя ученика для удаления (Enter — отмена): ").strip()
    if name == "":
        print("Отменено.")
        return
    if name in students:
        del students[name]
        save_students()
        print(f"Ученик {name} удалён.")
    else:
        print("Ученик не найден.")

def main():
    load_students()
    while True:
        print("\n1 - Удалить ученика\n2 - Выход")
        cmd = input("Выберите действие: ").strip()
        if cmd == "1":
            remove_student()
        elif cmd == "2":
            break
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()
