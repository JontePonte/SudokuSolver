""" Input for the sudoku """

# 0 equals an empty square

""" Easy sudoku """
sudoku_e = [[0, 9, 8, 4, 5, 1, 0, 0, 2],
            [7, 2, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 3, 7, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 4, 2, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 0, 0, 4],
            [0, 0, 5, 0, 1, 7, 0, 0, 9],
            [2, 8, 0, 1, 0, 9, 4, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 8, 5, 0, 9, 7]]

""" Medium sudoku """
sudoku_m = [[2, 0, 0, 0, 9, 0, 0, 5, 1],
            [0, 0, 6, 8, 0, 5, 3, 0, 0],
            [5, 0, 3, 0, 4, 0, 0, 0, 0],
            [4, 7, 0, 0, 0, 8, 0, 0, 2],
            [0, 0, 0, 9, 0, 0, 0, 3, 0],
            [0, 6, 0, 0, 7, 0, 0, 4, 0],
            [0, 9, 4, 7, 0, 6, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 9, 0, 3],
            [0, 0, 0, 2, 0, 9, 0, 0, 7]]

""" Hard sudoku """
sudoku_h = [[0, 0, 0, 0, 0, 9, 3, 8, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 2],
            [6, 8, 0, 7, 0, 3, 0, 0, 0],
            [0, 0, 7, 0, 0, 0, 0, 2, 6],
            [8, 0, 1, 9, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 7, 0, 1, 0, 0],
            [0, 2, 0, 0, 3, 0, 8, 0, 1],
            [4, 7, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 3, 0]]

""" Very hard sudoku """
sudoku_v = [[0, 0, 0, 0, 9, 0, 4, 0, 0],
            [0, 0, 0, 7, 3, 0, 0, 0, 0],
            [4, 0, 3, 0, 0, 0, 0, 2, 0],
            [0, 4, 0, 6, 0, 0, 8, 0, 0],
            [0, 7, 0, 8, 0, 0, 0, 9, 0],
            [5, 0, 0, 0, 4, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 0],
            [0, 1, 0, 0, 5, 7, 0, 0, 0],
            [0, 0, 2, 4, 0, 1, 0, 0, 6]]

""" Empty sudoku """
sudoku_x = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

""" Test sudoku """
sudoku_t = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


""" Decide which one to use """
sudoku = sudoku_m
