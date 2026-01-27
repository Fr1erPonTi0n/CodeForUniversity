def groundhog_day(strings):
    for i in range(1, len(strings)):
        current_string, previous_string = strings[i], strings[i - 1]
        differences = 0
        for j in range(len(current_string)):
            if current_string[j] != previous_string[j]:
                differences += 1
        if differences > 2:
            differing_indices = [index for index in range(len(current_string)) if
                                 current_string[index] != previous_string[index]]
            return i, *differing_indices
    return 0, 0
