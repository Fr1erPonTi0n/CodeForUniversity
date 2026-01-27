from groundhog_day import groundhog_day
from gears import gears
from brackets import brackets


def main():
    data = ['Groundhog Festival in Punxsutawney.',
            'Groundhog Festival in Punksutawney.',
            'Groundhog Festivel in Punxsutowney.']
    print(groundhog_day(data))
    data = ['February 2 Groundhog Day',
            'february 2 Groundhog Day',
            'February 2 Groundhag Day',
            'February 2 Groundhog Day']
    print(groundhog_day(data))
    print('')
    data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
    print(gears(data, 30, 7))
    print('')
    line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
    print(brackets(line))
    line = "1{2 + [3}45 - 6] * (7 - 8) 9"
    print(brackets(line))


if __name__ == '__main__':
    main()