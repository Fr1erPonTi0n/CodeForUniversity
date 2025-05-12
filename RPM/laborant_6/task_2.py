class StudentRegistry:
    students = []

    @staticmethod
    def add_student(name: str):
        StudentRegistry.students.append(name)

    @staticmethod
    def get_student_count():
        return len(StudentRegistry.students)

    @staticmethod
    def get_all_students():
        return StudentRegistry.students.copy()

    @classmethod
    def clear_registry(cls):
        cls.students.clear()


StudentRegistry.add_student('Анастасия')
StudentRegistry.add_student('Матвей')
StudentRegistry.add_student('Александр')

print(StudentRegistry.get_student_count())
print(StudentRegistry.get_all_students())

StudentRegistry.clear_registry()

print(StudentRegistry.get_student_count())

