
""" A program to solve a Suoku square """

from Sudoku import sudoku
from Square import Square


class SudokuSolver:
    """ Main class to call everything """
    def __init__(self):
        self.load_sudoku()

    def load_sudoku(self):
        """ Load sudoku from file """
        self.sudoku = sudoku
        # create SudokuSquare from the sudoku file
