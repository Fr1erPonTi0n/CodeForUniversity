import random

nums1 = [random.randint(-100, 100) for _ in range(random.randint(5, 30))]
print(f'1 массив чисел:\n{nums1}')

nums2 = [random.randint(-100, 100) for _ in range(random.randint(5, 30))]
print(f'2 массив чисел:\n{nums2}')

"""Cортировка вставками (Insertion Sort) — это алгоритм сортировки,
   на каждом шаге которого массив постепенно перебирается слева направо.
   При этом каждый последующий элемент размещается так, чтобы он
   оказался между ближайшими элементами с минимальным и максимальным значением."""

def insertion_sort_iterative(numbers):
    n = len(numbers)  # Получаем длину массива
    for i in range(1, n):
        x = numbers[i]  # Элемент списка
        j = i  # Индекс элемента
        while j > 0 and numbers[j - 1] > x:
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = x
    return numbers


def insertion_sort_recursive(numbers, n=None):
    # Если длина массива не передана, вычисляем её
    if n is None:
        n = len(numbers)

    # Базовый случай: если массив пуст или состоит из одного элемента, он уже отсортирован
    if n <= 1:
        return numbers

    # Рекурсивно сортируем первые n-1 элементов
    insertion_sort_recursive(numbers, n - 1)

    # Последний элемент, который нужно вставить в отсортированную часть
    last_element = numbers[n - 1]
    j = n - 2  # Индекс предпоследнего элемента

    # Перемещаем элементы больше last_element вправо
    while j >= 0 and numbers[j] > last_element:
        numbers[j + 1] = numbers[j]
        j -= 1

    # Вставляем last_element на правильное место
    numbers[j + 1] = last_element
    return numbers


insertion_sort_iterative(nums1)
print(f'Отсортированный 1 список, итерацией:\n{nums1}')

insertion_sort_recursive(nums2)
print(f'Отсортированный 2 список, рекурсией:\n{nums2}')