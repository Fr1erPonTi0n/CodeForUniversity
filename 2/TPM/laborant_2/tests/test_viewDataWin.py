from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QPushButton, QLabel


class TestViewDataWindow:
    def test_window_initialization(self, view_data_window):
        """Тест инициализации окна просмотра"""
        assert view_data_window.windowTitle() == "SRM-Система про студентов"
        assert isinstance(view_data_window.title_label, QLabel)
        assert view_data_window.title_label.text() == "Таблица студентов"
        assert isinstance(view_data_window.table, QTableWidget)
        assert isinstance(view_data_window.edit_button, QPushButton)
        assert isinstance(view_data_window.delete_button, QPushButton)
        assert isinstance(view_data_window.refresh_button, QPushButton)
        assert isinstance(view_data_window.close_button, QPushButton)

    def test_table_structure(self, view_data_window):
        """Тест структуры таблицы"""
        assert view_data_window.table.columnCount() == 4
        headers = [view_data_window.table.horizontalHeaderItem(i).text()
                   for i in range(view_data_window.table.columnCount())]
        assert headers == ["ID", "Имя", "Возраст", "Оценка"]

    def test_data_loading_with_fixture(self, view_data_window_with_data, sample_data):
        """Тест загрузки данных с использованием фикстуры с данными"""
        window = view_data_window_with_data
        assert window.table.rowCount() == len(sample_data)
        for row in range(window.table.rowCount()):
            assert (window.table.item(row, 1).text() ==
                    sample_data[row]["name"])
            assert (window.table.item(row, 2).text() ==
                    str(sample_data[row]["age"]))
            assert (window.table.item(row, 3).text() ==
                    sample_data[row]["grade"])

    def test_empty_database_fixture(self, view_data_window):
        """Тест с пустой базой данных используя фикстуру"""
        assert view_data_window.table.rowCount() == 0

    def test_selection_changed_handler(self, view_data_window_with_data):
        """Тест обработчика изменения выбора строки"""
        window = view_data_window_with_data
        assert window.selected_student_id is None
        window.table.selectRow(0)
        student_id = int(window.table.item(0, 0).text())
        assert window.selected_student_id == student_id
        window.table.clearSelection()
        assert window.selected_student_id is None

    def test_selection_edited_handler(self, view_data_window_with_data):
        """Тест обработчика изменения данных после редактирования"""
        window = view_data_window_with_data
        original_row_count = window.table.rowCount()
        window.table.selectRow(0)
        new_name = "Измененное Имя"
        new_age = int(window.table.item(0, 2).text()) + 1
        new_grade = "Отлично"
        success = window.db.update_student(window.selected_student_id, new_name, new_age, new_grade)
        assert success is True
        window.load_data()
        assert window.table.rowCount() == original_row_count
        assert window.table.item(0, 1).text() == new_name
        assert window.table.item(0, 2).text() == str(new_age)
        assert window.table.item(0, 3).text() == new_grade
        assert window.selected_student_id is None

    def test_selection_deleted_handler(self, view_data_window_with_data):
        """Тест обработчика удаления данных после удаления студента"""
        window = view_data_window_with_data
        original_row_count = window.table.rowCount()
        window.table.selectRow(0)
        student_to_delete_id = window.selected_student_id
        success = window.db.delete_student(student_to_delete_id)
        assert success is True
        window.load_data()
        assert window.table.rowCount() == original_row_count - 1
        for row in range(window.table.rowCount()):
            current_student_id = int(window.table.item(row, 0).text())
            assert current_student_id != student_to_delete_id
        assert window.selected_student_id is None

    def test_refresh_button_click(self, qtbot, view_data_window):
        """Тест клика по кнопке обновления"""
        window = view_data_window
        with qtbot.waitSignal(window.refresh_button.clicked):
            qtbot.mouseClick(window.refresh_button, Qt.MouseButton.LeftButton)

    def test_refresh_functionality(self, view_data_window_with_data):
        """Тест функциональности обновления"""
        window = view_data_window_with_data
        initial_row_count = window.table.rowCount()
        window.db.add_student("Масяня", 18, "Удовлетворительно")
        window.load_data()
        assert window.table.rowCount() == initial_row_count + 1

    def test_edit_button_click(self, qtbot, view_data_window_with_data):
        """Тест клика по кнопке изменения"""
        window = view_data_window_with_data
        window.table.selectRow(0)
        with qtbot.waitSignal(window.edit_button.clicked):
            qtbot.mouseClick(window.edit_button, Qt.MouseButton.LeftButton)

    def test_delete_button_click(self, qtbot, view_data_window_with_data):
        """Тест клика по кнопке удаления"""
        window = view_data_window_with_data
        window.table.selectRow(0)
        with qtbot.waitSignal(window.delete_button.clicked):
            qtbot.mouseClick(window.delete_button, Qt.MouseButton.LeftButton)

    def test_close_button_click(self, qtbot, view_data_window):
        """Тест клика по кнопке закрытия"""
        window = view_data_window
        with qtbot.waitSignal(window.close_button.clicked):
            qtbot.mouseClick(window.close_button, Qt.MouseButton.LeftButton)

    def test_close_buton_functionality(self, qtbot, view_data_window):
        """Тест функциональности закрытия"""
        window = view_data_window
        with qtbot.waitSignal(window.close_button.clicked):
            qtbot.mouseClick(window.close_button, Qt.MouseButton.LeftButton)
        assert not window.isVisible()
