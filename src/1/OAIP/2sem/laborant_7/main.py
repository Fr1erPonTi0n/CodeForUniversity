from factorial import factorial
from fibonacci import fibonacci
from vowels import vowels
from simple_number import simple_number
from max_n import max_n


def main():
    print(factorial(4), end='\n')
    print(fibonacci(10), end='\n')
    print(vowels('Hello uOu hi hi hi'), end='\n')
    print(simple_number(5), end='\n')
    print(max_n([1, 2, 3, 4, 5, 6, 7]))


if __name__ == "__main__":
    main()
