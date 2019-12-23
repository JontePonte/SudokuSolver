
""" A program to solve a Suoku """

from Sudoku import sudoku
from Square_class import Square


class SudokuSolver:
    """ Main class to call everything """
    def __init__(self):
        # Load the sudoku from "Sudoku.py" to squares
        self.squares = self.load_sudoku()

        # Print the sudoku output
        self.print_sudoku()

    def check_finished(self):
        """ Check if the win or fail conditions has ben met """
        pass

    def load_sudoku(self):
        """ Load sudoku from file and put the inforation in squares-list"""
        # Create the list that will be returned
        squares = []

        # loop through the sudoku rows
        y = 0
        id_num = 0
        for row in sudoku:
            square_row = []                 # Create row of Squares-objects that will be stored in squares
            x = 0
            for number in row:
                square = Square()           # Create a Square-object
                square.number = number      # Save the number in the Square-object
                square.id_num = id_num
                square.x_cor = x            # Save the coordinates in Square-object
                square.y_cor = y

                # Call a method that calculates the box number
                square.box = self.set_box_number(square.x_cor, square.y_cor)

                id_num += 1
                x += 1
                square_row.append(square)   # Save the Square-object in the row-list
            squares.append(square_row)      # and save the row in the squares-list
            y += 1
        return squares

    def print_sudoku(self):
        """ A method that prints the current squares-list """
        output = []
        # Create list in lists for all square numbers
        for row in self.squares:
            output_row = []
            for square in row:
                output_row.append(square.number)
            output.append(output_row)

        # Print the numbers in output-list
        for row in output:
            print(row)

    def remove_simple_possibilities(self):
        """ A method that checks the rows, coloms and boxes and removes any simple possibilities for the Squares"""
        pass

    def set_box_number(self, x, y):
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

    def set_numbers(self):
        """ A method that check if there is just one number left in square.possible and set number there after """
        pass


run = SudokuSolver()
