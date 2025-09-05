#  1 ЗАДАНИЕ


def count_str():
    lens = []
    text = input()
    while text != '':
        lens.append(str(len(text)))
        text = input()
    return ', '.join(lens)


#  2 ЗАДАНИЕ


def count_num():
    num = float(input())
    count = 0
    while num < 36.6:
        if num < 0:
            count += 1
        num = float(input())
    return count


#  3 ЗАДАНИЕ


def second_max(lista=[]):
    n_max = max(lista)
    lista.remove(max(lista))
    return max(lista)


#  4 ЗАДАНИЕ


def min_num(n=str):
    lista = n.split(' ')
    maxa = 0
    for i in range(len(lista)):
        if int(lista[i]) > maxa:
            maxa = int(lista[i])
    return maxa


#  5 ЗАДАНИЕ


def check_num(n=int):
    if (n % 7 == 0) and (n % 2 == 0):
        return 'Караул!'
    elif n % 2 == 0:
        return 'несчастливое'
    elif n % 7 == 0:
        return 'опасное'
    else:
        return 'нормальное'


#  6 ЗАДАНИЕ


def is_prime(n=int):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def sum_num():
    n = 0
    for i in range(2, 10001):
        if is_prime(i):
            n += i
    return n


#  7 ЗАДАНИЕ


def comparison(x1, y1, z1):
    while True:
        x2 = int(input())
        y2 = int(input())
        z2 = int(input())
        if x1 < x2 and y1 < y2 and z1 < z2:
            print('Нет')
            break
        print('Да')


#  8 ЗАДАНИЕ


def read_str():
    text = input()
    min_text = ''
    while text != 'стоп':
        if min_text == '' or len(text) < len(min_text):
            min_text = text[:]
        text = input()
    return min_text


#  9 ЗАДАНИЕ


def calculator():
    nums = input().split(', ')
    count = 0
    for i in range(len(nums)):
        if i == 0:
            count = int(nums[i])
        elif nums[i] is int:
            continue
        else:
            if nums[i] == '+':
                count += int(nums[i + 1])
            elif nums[i] == '-':
                count -= int(nums[i + 1])
            elif nums[i] == '*':
                count *= int(nums[i + 1])
            elif nums[i] == '/':
                if count == 0 or int(nums[i + 1]) == 0:
                    return 'Ошибка'
                else:
                    count /= int(nums[i + 1])
    return count


#  10 ЗАДАНИЕ


def text():
    nums = input().split()
    texta = []
    output = []
    while nums[-1] != 'стоп':
        nums += input().split()
    nums.pop(-1)
    for i in range(len(nums)):
        if '!' in nums[i]:
            texta.append(nums[i][:-1])
            output.append(f'{" ".join(texta)}{"!"}')
            texta = []
        else:
            texta.append(nums[i])
    return '\n'.join(output)
