import typing

T = typing.TypeVar('T')  # Тип для идентификатора задачи
U = typing.TypeVar('U')  # Тип для описания задачи
V = typing.TypeVar('V')  # Тип для приоритета задачи


class TaskManager(typing.Generic[T, U, V]):
    def __init__(self):
        self._tasks: typing.List[typing.Tuple[T, U, V]] = []

    def add_task(self, id: T, description: U, priority: V) -> None:
        self._tasks.append((id, description, priority))

    def get_highest_priority_task(self) -> str:
        if not self._tasks:
            return f'Нету задач'

        if isinstance(self._tasks[0][2], bool):
            return str(max(self._tasks, key=lambda task: task[2]))
        else:
            return str(max(self._tasks, key=lambda task: task[0]))

    def __str__(self) -> str:
        if not self._tasks:
            return f'Нету задач'
        return '\n'.join(f'{task[0]}, {task[1]}, {task[2]}' for task in self._tasks)

