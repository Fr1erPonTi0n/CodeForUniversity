from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List


class Student:
    def __init__(self, first_name: str, last_name: str, average_score: float) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._average_score = average_score

    def __repr__(self) -> str:
        return f"{self._first_name} {self._last_name} (средний балл: {self._average_score})"


class StudentGroupIterator(Iterator):
    def __init__(self, students: List[Student]) -> None:
        self._students = students
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class StudentGroup(Iterable):
    def __init__(self, students: List[Student] | None = None) -> None:
        self._students = students or []

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def __iter__(self) -> StudentGroupIterator:
        return StudentGroupIterator(self._students)


if __name__ == "__main__":
    group = StudentGroup()
    group.add_student(Student("Иван", "Иванов", 4.5))
    group.add_student(Student("Пётр", "Петров", 3.8))
    group.add_student(Student("Светлана", "Смирнова", 4.9))

    print("Список студентов в группе:")
    for student in group:
        print(student)
        
