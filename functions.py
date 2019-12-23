""" All the functions in the sudoku solver """


def set_box_number(x, y):
    """ Get the number of the box the hard way... """
    box_number = 0
    if y <= 2:
        if x <= 2:
            box_number = 0
        elif 3 <= x <= 5:
            box_number = 1
        elif 6 <= x <= 8:
            box_number = 2
    elif 3 <= y <= 5:
        if x <= 2:
            box_number = 3
        elif 3 <= x <= 5:
            box_number = 4
        elif 6 <= x <= 8:
            box_number = 5
    elif 6 <= y <= 8:
        if x <= 2:
            box_number = 6
        elif 3 <= x <= 5:
            box_number = 7
        elif 6 <= x <= 8:
            box_number = 8
    return box_number           # not pretty but it works
