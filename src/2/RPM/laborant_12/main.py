import re
import time
import os
import random
from collections import Counter
from functools import lru_cache


def measure_time(func, *args, **kwargs):
    """Измеряет время выполнения функции"""
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    print(f"Функция '{func.__name__}' выполнилась за {elapsed_time:.6f} секунд")
    return result, elapsed_time


class TestOne:
    """Задания 1-3"""
    @staticmethod
    def original_count_words(file_path):
        """Оригинальная функция задания 1 для рефакторинга"""
        file = open(file_path, 'r')
        content = file.read()
        words = content.split()
        unique_words = {}
        for word in words:
            if word in unique_words:
                unique_words[word] += 1
            else:
                unique_words[word] = 1
        file.close()
        return unique_words

    @staticmethod
    def refactoring_count_words(file_path):
        """Изменённая функция"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                words = re.findall(r'\b\w+\b', content.lower())
                word_count = {}
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
                return word_count
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return {}
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return {}

    @staticmethod
    def count_words_with_counter(file_path):
        """Измененная функция с библиотекой подсчёта"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                words = re.findall(r'\b\w+\b', content.lower())
                return dict(Counter(words))
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return {}
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return {}

class TestTwo:
    """Задание 4"""
    @staticmethod
    def fibonacci_recursive(n):
        """Рекурсивная реализация Фибоначчи"""
        if n <= 1:
            return n
        return TestTwo.fibonacci_recursive(n - 1) + TestTwo.fibonacci_recursive(n - 2)
    
    @staticmethod
    @lru_cache(maxsize=None)
    def fibonacci_memo(n):
        """Рекурсивная реализация с кэшированием"""
        if n <= 1:
            return n
        return TestTwo.fibonacci_memo(n - 1) + TestTwo.fibonacci_memo(n - 2)
    
    @staticmethod
    def fibonacci_iterative(n):
        """Итеративная реализация Фибоначчи"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
class TestThree:
    """Задание 5"""
    @staticmethod
    def filter_numbers():
        """Оригинальная функция фильтрации чисел"""
        numbers = []
        for i in range(input(), input()):
            if i % 3 == 0 or i % 5 == 0:
                numbers.append(i)

    @staticmethod
    def filter_numbers_optimized(start, end):
        """Оптимизированная функция фильтрации чисел"""
        if start >= end:
            return 0
        total = 0
        for i in range(start, end):
            if i % 3 == 0 or i % 5 == 0:
                total += i
        return total

class TestFour:
    """Задание 6"""
    @staticmethod
    def bubble_sort(numbers):
        """Классическая пузырьковая сортировка"""
        numbers_copy = numbers.copy()
        for i in range(len(numbers_copy)):
            for j in range(len(numbers_copy) - 1):
                if numbers_copy[j] > numbers_copy[j + 1]:
                    numbers_copy[j], numbers_copy[j + 1] = numbers_copy[j + 1], numbers_copy[j]
        return numbers_copy
    
    @staticmethod
    def bubble_sort_optimized(numbers):
        """Оптимизированная пузырьковая сортировка"""
        numbers_copy = numbers.copy()
        n = len(numbers_copy)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if numbers_copy[j] > numbers_copy[j + 1]:
                    numbers_copy[j], numbers_copy[j + 1] = numbers_copy[j + 1], numbers_copy[j]
                    swapped = True
            if not swapped:
                break
        return numbers_copy


if __name__ == "__main__":
    # Тесты всех функции по времени
    project_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_dir, 'text.txt')
    
    measure_time(TestOne.original_count_words, file_path)
    measure_time(TestOne.refactoring_count_words, file_path)
    measure_time(TestOne.count_words_with_counter, file_path)

    measure_time(TestTwo.fibonacci_recursive, 5)
    measure_time(TestTwo.fibonacci_memo, 5)
    measure_time(TestTwo.fibonacci_recursive, 5)

    try:
        print("Введите 2 числа через каждую строку")
        measure_time(TestThree.filter_numbers)
    except Exception as e:
        print("Ошибка фильтрации чисел из-за строчного типа данных. Время функции 'filter_numbers' не измеримо")
    measure_time(TestThree.filter_numbers_optimized, 100, 500)

    arr = [random.randint(0, 1000) for _ in range(1000)]
    measure_time(TestFour.bubble_sort, arr)
    measure_time(TestFour.bubble_sort_optimized, arr)
    