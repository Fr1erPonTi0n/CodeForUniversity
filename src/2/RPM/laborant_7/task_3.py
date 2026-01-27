class Component:
    def delete_user(self) -> str:
        pass


class DeleteUserComponent(Component):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def delete_user(self) -> str:
        return f"Пользователь с ID {self.user_id} успешно удален."


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def delete_user(self) -> str:
        return self._component.delete_user()


class AdminDecorator(Decorator):
    def delete_user(self) -> str:
        if current_user_role != 'admin':
            raise PermissionError("Доступ запрещен: для выполнения этого действия требуется роль администратора.")
        return self.component.delete_user()


def client_code(component: Component) -> None:
    print(f"Результат:\n{component.delete_user()}", end="")


current_user_role = None

if __name__ == "__main__":
    simple_component = DeleteUserComponent(123)

    # 1. Попытка вызвать операцию с ролью 'user' (должна быть ошибка)
    current_user_role = 'user'
    print(f"Текущая роль пользователя: {current_user_role}")
    decorated_component = AdminDecorator(simple_component)
    try:
        client_code(decorated_component)
    except PermissionError as e:
        print(f"Ошибка: {e}")
    print("\n")

    # 2. Вызов операции с ролью 'admin' (должно работать)
    current_user_role = 'admin'
    print(f"Текущая роль пользователя: {current_user_role}")
    try:
        client_code(decorated_component)
    except PermissionError as e:
        print(f"Ошибка: {e}")
    print("\n")

    # 3. Попытка с другой ролью, например, 'moderator' (должна быть ошибка)
    current_user_role = 'moderator'
    print(f"Текущая роль пользователя: {current_user_role}")
    try:
        client_code(decorated_component)
    except PermissionError as e:
        print(f"Error: {e}")
    print("\n")

    # Для сравнения: вызов простого компонента без декоратора (всегда работает)
    print("Клиент: Простой компонент без декоратора:")
    client_code(simple_component)
    print("\n")
