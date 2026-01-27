import os 

def main():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'words.txt')

        with open(file_path, 'r', encoding='UTF8') as file:
            lines = [line.strip() for line in file.readlines()]

        #  Находим максимальную длину слов
        max_length = max(len(word) for word in lines)

        #  Находим все слова с максимальной длиной
        longest_words = [word for word in lines if len(word) == max_length]

        #  Выводим результат
        print("Слово(а) максимальной длины:",
              longest_words[0] if len(longest_words) == 1 else ', '.join(longest_words))

    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    main()
