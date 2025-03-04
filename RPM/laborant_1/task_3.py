import random

n = 7
nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(f'1 массив чисел:\n{nums}')

"""Бинарный поиск - тип поискового алгоритма, который 
   последовательно делит пополам заранее отсортированный 
   массив данных, чтобы обнаружить нужный элемент."""

def binary_search_iterative(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2 # сред индекс
        if numbers[mid] == target:
            return mid # элемент найден
        elif numbers[mid] < target:
            left = mid + 1 # ищем в правой половине
        else:
            right = mid - 1 # ищем в левой половине
    return None # элемент не найден


def binary_search_recursive(numbers, target, left=None, right=None):
    # Инициализация границ при первом вызове функции
    if left is None:
        left = 0
    if right is None:
        right = len(numbers) - 1

    # Базовый случай: если границы пересеклись, элемент не найден
    if left > right:
        return None

    # Находим середину текущего диапазона
    mid = (left + right) // 2

    # Если элемент найден, возвращаем его индекс
    if numbers[mid] == target:
        return mid

    # Если элемент меньше целевого, ищем в правой половине
    elif numbers[mid] < target:
        return binary_search_recursive(numbers, target, mid + 1, right)

    # Если элемент больше целевого, ищем в левой половине
    else:
        return binary_search_recursive(numbers, target, left, mid - 1)


output1 =binary_search_iterative(nums, n)
print(f'Бинарный поиск числа {n} в 1 списке, итерацией:\n{output1}')

output2 = binary_search_recursive(nums, n)
print(f'Бинарный поиск числа {n} в 2 списке, рекурсией:\n{output2}')