import os

class Singleton(type):

    """Приватное поле для хранения единственного экземпляра"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Возвращает единственный экземпляр класса"""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        self.logs = []

    def write_logs(self, logs: str):
        print(f'Записываем логи ({logs}) в переменную класса')
        self.logs.append(logs)

    def view_logs(self):
        print('Что храниться в переменной класса', ' '.join(map(str, self.logs)))

    def save_logs(self):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(project_dir, 'logs.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(' '.join(map(str, self.logs)))


if __name__ == "__main__":
    s1 = Logger()
    print('Создаем первый экземпляр класса и пишем лог в него.')
    s1.write_logs('1')
    s1.view_logs()
    print('-------')
    print('Создаем второй экземпляр класса, который с помощью паттерна одиночки')
    print('будет ссылаться на первый (предыдущий) объект.')
    s2 = Logger()
    print('-------')
    print('Проверяем значение классов, они должны совпадать')
    s1.view_logs()
    s2.view_logs()
    print('-------')
    print('Для доп проверки привязанности второго класса к первому, мы добавим ко второму еще один лог')
    s2.write_logs('2')
    print('-------')
    print('При добавление лога во второй экземпляр, лог должен перенаправиться к оригинальному первому классу.')
    print('Значение в этом случае будут одинаковые.')
    s1.view_logs()
    s2.view_logs()
    print('-------')
    print('При проверки id классов, они должны совпадать.')
    if id(s1) == id(s2):
        print("Синглтон работает, обе переменные содержат один и тот же экземпляр.")
    else:
        print("Синглтон не удался, переменные содержат разные экземпляры.")
    print('-------')
    print('Сохраняем логи в файл')
    s1.save_logs()

