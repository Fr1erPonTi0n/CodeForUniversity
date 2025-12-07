import os
import pytest


class TestDatabase:
    def test_database_initialization(self, temp_db):
        """Тест инициализации базы данных"""
        assert temp_db.db_path is not None
        assert os.path.exists(temp_db.db_path)
        students = temp_db.get_all_students()
        assert isinstance(students, list)
        assert len(students) == 0

    @pytest.mark.parametrize("name,age,grade", [
        ("Иван Иванов", 20, "Отлично"),
        ("Мария Петрова", 19, "Хорошо"),
        ("Алексей Сидоров", 21, "Удовлетворительно"),
        ("Елена Ковалева", 18, "Отлично")
    ])
    def test_add_student_parameterized(self, temp_db, name, age, grade):
        """Параметризованный тест добавления записей"""
        student_id = temp_db.add_student(name, age, grade)
        assert student_id is not None
        assert isinstance(student_id, int)
        assert student_id > 0
        students = temp_db.get_all_students()
        assert len(students) == 1
        added_student = students[0]
        assert added_student["id"] == student_id
        assert added_student["name"] == name
        assert added_student["age"] == age
        assert added_student["grade"] == grade

    def test_add_multiple_students(self, temp_db):
        """Тест добавления нескольких студентов"""
        test_students = [
            {"name": "Первый Студент", "age": 18, "grade": "Отлично"},
            {"name": "Второй Студент", "age": 19, "grade": "Хорошо"},
            {"name": "Третий Студент", "age": 20, "grade": "Удовлетворительно"},
        ]
        added_ids = []
        for student in test_students:
            student_id = temp_db.add_student(student["name"], student["age"], student["grade"])
            added_ids.append(student_id)
        assert len(added_ids) == len(set(added_ids))
        students = temp_db.get_all_students()
        assert len(students) == len(test_students)
        for i, student in enumerate(students):
            assert student["id"] == added_ids[i]
            assert student["name"] == test_students[i]["name"]
            assert student["age"] == test_students[i]["age"]
            assert student["grade"] == test_students[i]["grade"]

    def test_get_all_students(self, db_with_data, sample_data):
        """Тест получения всех записей"""
        students = db_with_data.get_all_students()
        assert isinstance(students, list)
        assert len(students) == len(sample_data)
        for student in students:
            assert "id" in student
            assert "name" in student
            assert "age" in student
            assert "grade" in student
            assert isinstance(student["id"], int)
            assert isinstance(student["name"], str)
            assert isinstance(student["age"], int)
            assert isinstance(student["grade"], str)
        for i, student in enumerate(students):
            assert student["name"] == sample_data[i]["name"]
            assert student["age"] == sample_data[i]["age"]
            assert student["grade"] == sample_data[i]["grade"]

    def test_get_nonexistent_student(self, temp_db):
        """Тест получения несуществующего студента"""
        student = temp_db.get_student(999)
        assert student is None

    def test_update_student(self, db_with_data):
        """Тест изменения записей"""
        students = db_with_data.get_all_students()
        original_student = students[0]
        updated_data = {
            "name": "Обновленное Имя",
            "age": 25,
            "grade": "Хорошо"
        }
        success = db_with_data.update_student(
            original_student["id"],
            updated_data["name"],
            updated_data["age"],
            updated_data["grade"]
        )
        assert success is True
        updated_student = db_with_data.get_student(original_student["id"])
        assert updated_student["name"] == updated_data["name"]
        assert updated_student["age"] == updated_data["age"]
        assert updated_student["grade"] == updated_data["grade"]
        assert updated_student["id"] == original_student["id"]

    def test_update_nonexistent_student(self, temp_db):
        """Тест изменения несуществующего студента"""
        success = temp_db.update_student(999, "Несуществующий", 30, "Отлично")
        assert success is False

    def test_delete_student(self, db_with_data):
        """Тест удаления записей"""
        students_before = db_with_data.get_all_students()
        initial_count = len(students_before)
        assert initial_count > 0
        student_to_delete = students_before[0]
        success = db_with_data.delete_student(student_to_delete["id"])
        assert success is True
        students_after = db_with_data.get_all_students()
        assert len(students_after) == initial_count - 1
        remaining_ids = [student["id"] for student in students_after]
        assert student_to_delete["id"] not in remaining_ids
        deleted_student = db_with_data.get_student(student_to_delete["id"])
        assert deleted_student is None

    def test_delete_nonexistent_student(self, temp_db):
        """Тест удаления несуществующего студента"""
        success = temp_db.delete_student(999)
        assert success is False

    def test_empty_database_operations(self, temp_db):
        """Тест операций с пустой базой данных"""
        students = temp_db.get_all_students()
        assert students == []
        assert len(students) == 0
        success = temp_db.delete_student(1)
        assert success is False
        success = temp_db.update_student(1, "Имя", 20, "Оценка")
        assert success is False
