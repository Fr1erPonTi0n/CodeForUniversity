def quaters(*args):
    output_dict = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
    for element in args:
        if not(element[0] == 0) and not(element[1] == 0):
            if element[0] >= 1 and element[1] >= 1:
                output_dict['I'] += 1
            elif element[0] < 1 <= element[1]:
                output_dict['II'] += 1
            elif element[0] < 1 and element[1] < 1:
                output_dict['III'] += 1
            elif element[0] >= 1 > element[1]:
                output_dict['IV'] += 1
    return output_dict