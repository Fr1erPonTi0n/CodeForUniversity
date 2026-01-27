#  1 ЗАДАНИЕ


def trafarets():
    nums = set()
    for i in range(int(input())):
        nums = nums.union(set(input()))
    print(len(nums))


#  2 ЗАДАНИЕ


def set_words():
    string1, string2, string3 = input(), input(), input()
    print(''.join((set(string1) & set(string2)) | (set(string1) & set(string3)) | (set(string2) & set(string3))))


#  3 ЗАДАНИЕ


def find_num():
    print(' '.join(set('0123456789') - set(input())))


#  4 ЗАДАНИЕ


def posled_nums():
    nums = set()
    while (n := int(input())) != 0:
        nums.add(n)
    print([num for num in nums if num % len(nums) == 0])


#  5 ЗАДАНИЕ


def flags():
    flags = [input() for i in range(int(input()))]
    print('\n'.join([flags[i % len(flags)] for i in range(int(input()))]))


#  6 ЗАДАНИЕ


def era_dinozavrov():
    season, ers = {
        "Proterozoic": range(635 * 10 ** 6, 2800 * 10 ** 6),
        "Cenozoic": range(0, 145 * 10 ** 6),
        "Mesozoic": range(145 * 10 ** 6, 300 * 10 ** 6),
        "Paleozoic": range(300 * 10 ** 6, 635 * 10 ** 6)
        }, []
    while True:
        x = input()
        if not x:
            break
        ers.append(next((key for key, value in season.items() if int(x) * 1000 in value), "Archaea"))
    print('\n'.join(ers))


#  7 ЗАДАНИЕ


def angry_birds():
    output = {}
    while (bird := input()) != '':
        name, count = bird.split(':')
        output[name] = output.get(name, 0) + int(count)
    print(output)


#  8 ЗАДАНИЕ


def binary_n_sys():
    print([{'digits': len(b := bin(int(n))[2:]), 'units': b.count('1'), 'zeros': b.count('0')} for n in input().split()])
