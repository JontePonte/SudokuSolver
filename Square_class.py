

class Square:
    """ Class for single square in the sudoku """
    def __init__(self):
        self.x_cor = 0      # x-coordinate
        self.y_cor = 0      # y-coordinate
        self.box = 0        # the box number the square belongs to

        self.number = 0                                 # 0 means not defined
        self.id_num = 0                                 # ID-number for all the squares
        self.possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # Array with all possible values for the square
