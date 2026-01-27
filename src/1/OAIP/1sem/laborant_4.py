#  1 ЗАДАНИЕ


def eight_print():
    for i in range(8):
        print(i)


#  2 ЗАДАНИЕ


def order_of_people():
    for i in range(1, int(input()) + 1):
        print(i, input())


#  3 ЗАДАНИЕ


def timbykto():
    for i in range(int(input()), 31, int(input())):
        print(i)


#  4 ЗАДАНИЕ


def max_letter():
    a, count, max_count = input(), 0, 0
    for _ in range(int(input())):
        if input() == a:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    else:
        if count > max_count:
            max_count = count
    print(max_count)


#  5 ЗАДАНИЕ


def div():
    n, summ = int(input()), 0
    for i in range(1, n + 1):
        if n % i == 0:
            summ += i
    print(summ)


#  6 ЗАДАНИЕ


def russia_lang():
    text, count = input(), 0
    for i in range(len(text)):
        if text[i] in 'аяоёэеуюыи':
            count += 1
    print(count)


#  7 ЗАДАНИЕ


def n_words():
    word = input()
    for i in range(1, int(input()) + 1):
        print(f'{i}. {word}')


#  8 ЗАДАНИЕ


def nomer():
    number = input()
    for i in range(len(number)):
        if number[i] not in '+1234567890':
            print('Неправильно номер телефона!')
    print('Bce ok!')


#  9 ЗАДАНИЕ


def russia_password():
    vowels, consonants, login, output = 'аеёиоуыэюя', 'бвгджзйклмнпрстфхцчшщъь', input().lower(), ''
    for i in login:
        if i in vowels:
            output += '0'
        elif i in consonants:
            output += '1'
    print(output)


#  10 ЗАДАНИЕ


def debug_text():
    message = input()
    for i in range(0, len(message), 2):
        print(message[i], end='')
