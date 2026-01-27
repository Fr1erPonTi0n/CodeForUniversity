from sortuna import sortuna
from stars import stars
from nearby import nearby


def main():
    data = [
        ("abc", 123, "zxc"),
        ("sdf", 456, "nmb"),
        ("yui", 987, "plk")
    ]
    print(sortuna(data), end='\n\n')

    text = 'Expanding the space available for living'
    print(stars(text), end='\n\n')

    data = ['100100011',
            '0001100001',
            '100001001',
            '1110010111']
    print(*nearby(data, places=4), sep='\n', end='\n\n')

    data = ['111', '101101', '11000']
    print(*nearby(data), sep='\n')

if __name__ == '__main__':
    main()