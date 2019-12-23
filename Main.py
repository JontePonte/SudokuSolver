
""" A program to solve a Suoku """

from Sudoku import sudoku
from Square_class import Square
from functions import set_box_number


class SudokuSolver:
    """ Main class to call everything """
    def __init__(self):
        # Load the sudoku from "Sudoku.py" to squares
        self.squares = self.load_sudoku()
        self.tries = 0
        self.max_tries = 10000

        # Try to solve as long as the sudoku is not finnished
        while not self.is_finished():
            # Remove the squares possibilities base on rows, columns, and boxes
            self.remove_possibilities_simple()

            self.tries += 1

        # Print the sudoku output
        self.print_sudoku()

    def is_finished(self):
        """ Check if the win or fail conditions has ben met """
        check = False

        # check if the maximum allowed tries has been done
        if self.tries >= self.max_tries:
            check = True

        return check

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
                square.box = set_box_number(square.x_cor, square.y_cor)

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

    def remove_possibilities_simple(self):
        """ A method that checks the rows, columns and boxes and removes any simple possibilities for the Squares"""
        # Loop through the squares to check them
        for row in self.squares:
            for square in row:
                # The square has to not defined
                if square.number == 0:
                    pass


# Run the program
run = SudokuSolver()
