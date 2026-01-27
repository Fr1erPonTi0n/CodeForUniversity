from quaters import quaters
from future import future
from circuit_resistance import circuit_resistance


def main():
    data = [(1, 1), (-1, 2), (-3, -1)]
    for k, v in sorted(quaters(*data).items()):
        print(f'{k}:\t{v}')
    print()
    data = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
    for k, v in sorted(quaters(*data).items()):
        print(f'{k}:\t{v}')
    print('-----')
    VIN = 3
    mass = [1, 2, 3, 4]
    const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
    print(future(VIN, *mass, **const))
    print()
    VIN = 540
    mass = [1, 2, 3, 4, 5]
    const = {'e0': 9, 'mu0': 4}
    print(future(VIN, *mass, **const))
    print('-----')
    data = [10, 20, 30]
    print(circuit_resistance(*data))
    print()
    data = [30, 30, 30]
    print(circuit_resistance(*data, connection='parallel'))


if __name__ == '__main__':
    main()