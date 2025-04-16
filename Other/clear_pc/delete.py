import os
from datetime import datetime
from pathlib import Path


def delete_old_files(extension, cutoff_date, var='1'):
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

    # Преобразуем строку даты в объект datetime
    cutoff_date = datetime.strptime(cutoff_date, '%Y-%m-%d')

    # Проходим по всем файлам на рабочем столе
    for file in target_path.iterdir():
        # Проверяем, является ли это файлом и имеет ли нужное расширение
        if file.is_file() and file.suffix == extension:
            # Получаем время создания файла
            creation_time = datetime.fromtimestamp(file.stat().st_ctime)
            # Если файл был создан до указанной даты, удаляем его
            if creation_time < cutoff_date:
                print(f'Удаление файла: {file}')
                os.remove(file)


# Пример использования
if __name__ == "__main__":
    # Укажите расширение файла и дату
    file_extension = input("Введите расширение файла (например, .txt): ")
    date_input = '2024-09-01'

    delete_old_files(file_extension, date_input)