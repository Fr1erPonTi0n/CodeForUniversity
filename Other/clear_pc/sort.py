import os
from pathlib import Path


def sort_files_by_extension(var='1', create_common_folder=False):
    # Получаем путь
    desktop_path = Path.home() / 'Desktop'
    documents_path = Path.home() / 'Documents'
    downloads_path = Path.home() / 'Downloads'

    if var == '1':
        target_path = desktop_path
    elif var == '2':
        target_path = documents_path
    elif var == '3':
        target_path = downloads_path
    else:
        print('Выбран не правильный вариант')
        return

    # Если нужно создать общую папку, задаем её имя
    common_folder = target_path / 'Папка с отсортированными файлами' if create_common_folder else target_path

    # Если общая папка не существует и нужно её создать, создаем
    if create_common_folder and not common_folder.exists():
        print(f'Создание общей папки: {common_folder}')
        common_folder.mkdir()

    # Проходим по всем файлам в целевой папке
    for file in target_path.iterdir():
        # Проверяем, является ли это файлом
        if file.is_file():
            # Получаем расширение файла (без точки)
            extension = file.suffix[1:]  # Убираем точку из расширения

            if extension:  # Проверяем, что расширение не пустое
                # Создаем путь к папке с названием расширения внутри общей папки
                folder_path = common_folder / extension if create_common_folder else target_path / extension
            else:
                folder_path = common_folder / 'Файлы без расширения' if create_common_folder else \
                    target_path / 'Файлы без расширения'

                # Проверяем, существует ли папка
                if not folder_path.exists():
                    print(f'Создание папки: {folder_path}')
                    folder_path.mkdir()  # Создаем папку, если она не существует

                # Перемещаем файл в соответствующую папку
                print(f'Перемещение файла {file} в папку {folder_path}')
                file.rename(folder_path / file.name)

# Пример использования
if __name__ == "__main__":
    sort_files_by_extension('2', False)