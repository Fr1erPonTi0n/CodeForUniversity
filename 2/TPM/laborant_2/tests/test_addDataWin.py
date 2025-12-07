from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel


class TestAddDataWindow:
    def test_add_window_add_initialization(self, add_data_window):
        """Тест инициализации окна добавления"""
        assert "SRM-Система про студентов" in add_data_window.windowTitle()
        assert isinstance(add_data_window.title_label, QLabel)
        assert add_data_window.title_label.text() == "Добавить нового студента"
        assert isinstance(add_data_window.name_input, QLineEdit)
        assert isinstance(add_data_window.age_input, QLineEdit)
        assert isinstance(add_data_window.grade_input, QLineEdit)
        assert isinstance(add_data_window.save_button, QPushButton)
        assert isinstance(add_data_window.cancel_button, QPushButton)
        assert add_data_window.name_input.placeholderText() == "Введите имя студента"
        assert add_data_window.age_input.placeholderText() == "Введите возраст студента"
        assert add_data_window.grade_input.placeholderText() == "Введите оценку студента"

    def test_add_window_edit_initialization(self, edit_data_window):
        """Тест инициализации окна изменения"""
        assert "SRM-Система про студентов" in edit_data_window.windowTitle()
        assert isinstance(edit_data_window.title_label, QLabel)
        assert edit_data_window.title_label.text() == "Изменить данные студента"
        assert isinstance(edit_data_window.name_input, QLineEdit)
        assert isinstance(edit_data_window.age_input, QLineEdit)
        assert isinstance(edit_data_window.grade_input, QLineEdit)
        assert isinstance(edit_data_window.save_button, QPushButton)
        assert isinstance(edit_data_window.cancel_button, QPushButton)
        assert edit_data_window.name_input.text() != ""
        assert edit_data_window.age_input.text() != ""
        assert edit_data_window.grade_input.text() != ""

    def test_save_data_validation_empty_name(self, add_data_window):
        """Тест валидации при пустом имени"""
        add_data_window.name_input.setText("")
        add_data_window.age_input.setText("20")
        add_data_window.grade_input.setText("Отлично")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count

    def test_save_data_validation_invalid_age(self, add_data_window):
        """Тест валидации при неверном возрасте"""
        add_data_window.name_input.setText("Тестовый Студент")
        add_data_window.age_input.setText("не число")
        add_data_window.grade_input.setText("Отлично")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count

    def test_save_data_validation_negative_age(self, add_data_window):
        """Тест валидации при отрицательном возрасте"""
        add_data_window.name_input.setText("Тестовый Студент")
        add_data_window.age_input.setText("-5")
        add_data_window.grade_input.setText("Отлично")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count

    def test_save_data_validation_zero_age(self, add_data_window):
        """Тест валидации при нулевом возрасте"""
        add_data_window.name_input.setText("Тестовый Студент")
        add_data_window.age_input.setText("0")
        add_data_window.grade_input.setText("Отлично")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count

    def test_save_data_validation_empty_grade(self, add_data_window):
        """Тест валидации при пустой оценке"""
        add_data_window.name_input.setText("Тестовый Студент")
        add_data_window.age_input.setText("20")
        add_data_window.grade_input.setText("")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count

    def test_save_data_success_add(self, add_data_window):
        """Тест успешного добавления студента"""
        add_data_window.name_input.setText("Новый Студент")
        add_data_window.age_input.setText("22")
        add_data_window.grade_input.setText("Хорошо")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count + 1
        assert not add_data_window.isVisible()

    def test_save_data_success_edit(self, edit_data_window):
        """Тест успешного редактирования студента"""
        new_name = "Измененное Имя"
        edit_data_window.name_input.setText(new_name)
        edit_data_window.age_input.setText("25")
        edit_data_window.grade_input.setText("Отлично")
        edit_data_window.save_data()
        updated_student = edit_data_window.db.get_student(edit_data_window.student_id)
        assert updated_student['name'] == new_name
        assert updated_student['age'] == 25
        assert updated_student['grade'] == "Отлично"
        assert not edit_data_window.isVisible()

    def test_save_data_with_whitespace(self, add_data_window):
        """Тест сохранения данных с пробелами"""
        add_data_window.name_input.setText("  Студент с пробелами  ")
        add_data_window.age_input.setText("  19  ")
        add_data_window.grade_input.setText("  Удовлетворительно  ")
        initial_count = len(add_data_window.db.get_all_students())
        add_data_window.save_data()
        final_count = len(add_data_window.db.get_all_students())
        assert final_count == initial_count + 1

    def test_cancel_button(self, qtbot, add_data_window):
        """Тест кнопки отмены"""
        with qtbot.waitSignal(add_data_window.cancel_button.clicked):
            qtbot.mouseClick(add_data_window.cancel_button, Qt.MouseButton.LeftButton)

    def test_cancel_functionality(self, qtbot, add_data_window):
        """Тест функциональности отмены"""
        add_data_window.name_input.setText("Тестовый Студент")
        add_data_window.age_input.setText("20")
        add_data_window.grade_input.setText("Отлично")
        qtbot.mouseClick(add_data_window.cancel_button, Qt.MouseButton.LeftButton)
        assert not add_data_window.isVisible()

    def test_edit_student_data_persistence(self, edit_data_window):
        """Тест сохранения изменений при редактировании"""
        original_student = edit_data_window.db.get_student(edit_data_window.student_id)
        original_name = original_student['name']
        new_name = "Полностью новое имя"
        edit_data_window.name_input.setText(new_name)
        edit_data_window.save_data()
        updated_student = edit_data_window.db.get_student(edit_data_window.student_id)
        assert updated_student['name'] == new_name
        assert updated_student['name'] != original_name
