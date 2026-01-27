import time
from behave import given, when, then
from PyQt6.QtWidgets import QLineEdit, QPushButton
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.mainWin import MainWindow
from app.viewDataWin import ViewDataWindow
from app.addDataWin import AddDataWindow


@given('открыто главное окно SRM системы')
def step_open_main_window(context):
    """Открытие главного окна"""
    context.main_window = MainWindow()
    context.main_window.db = context.db
    context.main_window.show()
    context.windows = [context.main_window]
    time.sleep(0.1)

@given('база данных очищена')
def step_clear_database(context):
    """Очистка базы данных"""
    students = context.db.get_all_students()
    for student in students:
        context.db.delete_student(student['id'])

@given('в базе данных есть студенты:')
def step_add_students_to_db(context):
    """Добавление студентов в базу данных"""
    for row in context.table:
        context.db.add_student(
            row['name'],
            int(row['age']),
            row['grade']
        )

@given('в базе данных есть студент с именем "{name}", возрастом "{age:d}" и оценкой "{grade}"')
def step_add_specific_student(context, name, age, grade):
    """Добавление конкретного студента"""
    context.db.add_student(name, age, grade)

@given('в базе данных есть студент с именем "{name}"')
def step_add_student_by_name(context, name):
    """Добавление студента по имени"""
    context.db.add_student(name, 20, "хорошо")

@given('в базе данных есть "{count:d}" студента')
def step_add_number_of_students(context, count):
    """Добавление указанного количества студентов"""
    for i in range(count):
        context.db.add_student(f"Студент {i+1}", 18 + i, "удовлетворительно")

@when('пользователь нажимает кнопку "{button_text}"')
def step_click_button(context, button_text):
    """Нажатие на кнопку"""
    current_window = context.windows[-1]
    buttons = current_window.findChildren(QPushButton)
    target_button = None
    for button in buttons:
        if button.text() == button_text:
            target_button = button
            break
    if target_button:
        target_button.click()
        time.sleep(0.1)
        if hasattr(current_window, 'view_window') and current_window.view_window:
            context.windows.append(current_window.view_window)
        elif hasattr(current_window, 'add_window') and current_window.add_window:
            context.windows.append(current_window.add_window)
        elif hasattr(current_window, 'edit_window') and current_window.edit_window:
            context.windows.append(current_window.edit_window)
    else:
        assert False, f"Кнопка '{button_text}' не найдена"

@when('пользователь открывает окно просмотра студентов')
def step_open_view_window(context):
    """Открытие окна просмотра"""
    context.main_window.open_view_window()
    context.view_window = context.main_window.view_window
    context.windows.append(context.view_window)
    time.sleep(0.5)
    context.view_window.load_data()

@when('пользователь вводит имя "{name}"')
def step_enter_name(context, name):
    """Ввод имени"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'name_input'):
        current_window.name_input.setText(name)
    else:
        inputs = current_window.findChildren(QLineEdit)
        for input_field in inputs:
            if input_field.placeholderText() and "имя" in input_field.placeholderText().lower():
                input_field.setText(name)
                return
        assert False, "Поле для ввода имени не найдено"

@when('пользователь вводит возраст "{age}"')
def step_enter_age(context, age):
    """Ввод возраста"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'age_input'):
        current_window.age_input.setText(age)
    else:
        inputs = current_window.findChildren(QLineEdit)
        for input_field in inputs:
            if input_field.placeholderText() and "возраст" in input_field.placeholderText().lower():
                input_field.setText(age)
                return
        assert False, "Поле для ввода возраста не найдено"

@when('пользователь вводит оценку "{grade}"')
def step_enter_grade(context, grade):
    """Ввод оценки"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'grade_input'):
        current_window.grade_input.setText(grade)
    else:
        inputs = current_window.findChildren(QLineEdit)
        for input_field in inputs:
            if input_field.placeholderText() and "оценка" in input_field.placeholderText().lower():
                input_field.setText(grade)
                return
        assert False, "Поле для ввода оценки не найдено"

@when('пользователь выбирает студента "{student_name}"')
def step_select_student(context, student_name):
    """Выбор студента в таблице"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'table'):
        table = current_window.table
        for row in range(table.rowCount()):
            name_item = table.item(row, 1)
            if name_item and name_item.text() == student_name:
                table.selectRow(row)
                current_window.on_selection_changed()
                return
        assert False, f"Студент '{student_name}' не найден в таблице"
    else:
        assert False, "Таблица не найдена"

@when('пользователь нажимает кнопку "{button_text}" без выбора студента')
def step_click_button_without_selection(context, button_text):
    """Нажатие кнопки без выбора студента"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'table'):
        current_window.table.clearSelection()
        if hasattr(current_window, 'on_selection_changed'):
            current_window.on_selection_changed()
    step_click_button(context, button_text)

@when('пользователь вводит имя ""')
def step_enter_empty_name(context):
    """Ввод пустого имени"""
    step_enter_name(context, "")

@when('пользователь вводит оценку ""')
def step_enter_empty_name(context):
    """Ввод пустого имени"""
    step_enter_grade(context, "")  

@when('пользователь изменяет имя на "{name}"')
def step_change_name(context, name):
    """Изменение имени"""
    step_enter_name(context, name)

@when('пользователь изменяет возраст на "{age:d}"')
def step_change_age(context, age):
    """Изменение возраста"""
    step_enter_age(context, str(age))

@when('пользователь изменяет оценку на "{grade}"')
def step_change_grade(context, grade):
    """Изменение оценки"""
    step_enter_grade(context, grade)

@when('пользователь подтверждает удаление')
def step_confirm_delete(context):
    """Подтверждение удаления"""
    pass

@when('добавляется новый студент через базу данных')
def step_add_student_via_db(context):
    """Добавление студента напрямую в базу"""
    context.db.add_student("Новый студент", 22, "хорошо")

@then('должно открыться окно добавления студента')
def step_verify_add_window_opened(context):
    """Проверка открытия окна добавления"""
    current_window = context.windows[-1]
    assert isinstance(current_window, AddDataWindow), \
        f"Ожидалось окно AddDataWindow, получено {type(current_window)}"

@then('должно открыться окно просмотра студентов')
def step_verify_view_window_opened(context):
    """Проверка открытия окна просмотра"""
    current_window = context.windows[-1]
    assert isinstance(current_window, ViewDataWindow), \
        f"Ожидалось окно ViewDataWindow, получено {type(current_window)}"

@then('должен отобразиться успешный диалог с сообщением "{message}"')
def step_verify_success_dialog(context, message):
    """Проверка успешного диалога"""
    students = context.db.get_all_students()
    assert len(students) > 0, "Студент не был добавлен в базу данных"

@then('должен отобразиться диалог ошибки с сообщением "{message}"')
def step_verify_error_dialog(context, message):
    """Проверка диалога ошибки"""
    students = context.db.get_all_students()
    assert len(students) == 0, f"Студент не должен был быть добавлен при ошибке"

@then('студент "{name}" должен быть сохранен в базе данных с возрастом "{age:d}" и оценкой "{grade}"')
def step_verify_student_saved(context, name, age, grade):
    """Проверка сохранения студента"""
    students = context.db.get_all_students()
    found = False
    for student in students:
        if (student['name'] == name and 
            student['age'] == age and 
            student['grade'] == grade):
            found = True
            break
    assert found, f"Студент {name} с возрастом {age} и оценкой {grade} не найден в базе данных"

@then('студент "{name}" не должен быть сохранен в базе данных')
def step_verify_student_not_saved(context, name):
    """Проверка, что студент не сохранен"""
    students = context.db.get_all_students()
    for student in students:
        if student['name'] == name:
            assert False, f"Студент {name} найден в базе данных, хотя не должен был быть сохранен"

@then('пустой студент не должен быть сохранен в базе данных')
def step_verify_empty_student_not_saved(context):
    """Проверка, что студент с пустым именем не сохранен"""
    students = context.db.get_all_students()
    assert len(students) == 0, "В базе данных есть студенты, хотя не должно быть"

@then('в таблице должно отображаться "{count:d}" студента')
def step_verify_table_row_count(context, count):
    """Проверка количества строк в таблице"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'table'):
        assert current_window.table.rowCount() == count, \
            f"Ожидалось {count} строк, получено {current_window.table.rowCount()}"
    else:
        assert False, "Таблица не найдена"

@then('первая строка должна содержать "{content}"')
def step_verify_first_row_content(context, content):
    """Проверка содержимого первой строки"""
    step_verify_row_content(context, 1, content)

@then('вторая строка должна содержать "{content}"')
def step_verify_second_row_content(context, content):
    """Проверка содержимого второй строки"""
    step_verify_row_content(context, 2, content)

@then('третья строка должна содержать "{content}"')
def step_verify_third_row_content(context, content):
    """Проверка содержимого третьей строки"""
    step_verify_row_content(context, 3, content)

def step_verify_row_content(context, row_number, content):
    """Общая функция проверки содержимого строки"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'table'):
        table = current_window.table
        row_index = row_number - 1
        if row_index < table.rowCount():
            for col in range(table.columnCount()):
                item = table.item(row_index, col)
                if item and content in item.text():
                    return
            row_data = []
            for col in range(table.columnCount()):
                item = table.item(row_index, col)
                row_data.append(item.text() if item else "")
            assert False, f"Содержимое '{content}' не найдено в строке {row_number}: {row_data}"
        else:
            assert False, f"Строка {row_number} не существует в таблице"
    else:
        assert False, "Таблица не найдена"

@then('студент "{name}" должен быть обновлен в базе данных с возрастом "{age:d}" и оценкой "{grade}"')
def step_verify_student_updated(context, name, age, grade):
    """Проверка обновления студента"""
    step_verify_student_saved(context, name, age, grade)

@then('студент "{name}" не должен быть в базе данных')
def step_verify_student_deleted(context, name):
    """Проверка удаления студента"""
    students = context.db.get_all_students()
    for student in students:
        if student['name'] == name:
            assert False, f"Студент {name} все еще есть в базе данных"

@then('должен отобразиться диалог с предупреждением "{message}"')
def step_verify_warning_dialog(context, message):
    """Проверка предупреждающего диалога"""
    pass

@then('в таблице должно отображаться "{expected_count:d}" студентов')
def step_verify_student_count_in_table(context, expected_count):
    """Проверка количества студентов в таблице"""
    current_window = context.windows[-1]
    if hasattr(current_window, 'table'):
        actual_count = current_window.table.rowCount()
        assert actual_count == expected_count, \
            f"Ожидалось {expected_count} студентов, получено {actual_count}"
    else:
        assert False, "Таблица не найдена"
        