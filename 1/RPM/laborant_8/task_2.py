from abc import ABC, abstractmethod
from dataclasses import dataclass


class Person(ABC):
    @abstractmethod
    def full_name(self):
        pass

    @abstractmethod
    def get_id(self):
        pass


@dataclass
class Student(Person):
    first_name: str
    last_name: str
    student_id: int

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_id(self):
        return self.student_id


@dataclass
class Teacher(Person):
    first_name: str
    last_name: str
    employee_id: int
    courses: list

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_id(self):
        return self.employee_id


def print_person(person):
    if isinstance(person, Teacher | Student):
        return f'{person.full_name()}, ID: {person.get_id()}'
    return 'Ничего'


if __name__ == '__main__':
    list_student = [
        Student("Дамир", "Губнов", 228),
        Student("Андрей", "Тихий", 69),
        Student("Олег", "Грибной", 52)
    ]
    
    list_teacher = [
        Teacher("Сергей", "Губнов", 42, ["Геометрия", "Алгебра"]),
        Teacher("Анастасия", "Шалих", 1488, ["Программирование"]),
        Teacher("Гордей", "Жавелий", 911, ["Рисование", "Лепка из глины"])
    ]
    
    print("Студенты:")
    for person in list_student:
        print(print_person(person))
    
    print("Учителя:")
    for person in list_teacher:
        print(print_person(person))
