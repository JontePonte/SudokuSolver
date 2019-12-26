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
        self.max_tries = 100
        self.print_sudoku()

        # Try to solve as long as the sudoku is not finnished
        while not self.is_finished():
            # Remove the squares possibilities base on rows, columns, and boxes
            self.remove_possibilities_simple()

            # Set numbers if they are possible just ones in a row, column or box
            self.check_possibilities_simple()

            # Remove the square possibilities base on combinations of other combinations
            self.remove_possibilities_combinations()

            self.tries += 1       # Count the number of iterations

        # Print the sudoku output
        self.print_sudoku()

    def check_possibilities_simple(self):
        """ Set numbers if they are possible just ones in a row, column or box"""

        """ Check if a possibility appears just once i the rows """
        for row_number in range(9):
            # Save all possibilities for one row
            row_possibilities = []
            for square in self.squares:
                if square.y_cor == row_number:
                    row_possibilities.append(square.possible)

            # Count the number of times each number exists in row_possibilities
            for number in range(1, 10):

                number_counter = 0      # The number of times a number appears in row_possibilities
                right_x_cor = 0         # The right x coordinate for the number

                # Do the counting, if a number appears once ==> number_counter == 1
                for possibility, x_cor in zip(row_possibilities, range(len(row_possibilities))):
                    if number in possibility:
                        number_counter += 1
                        right_x_cor = x_cor

                # Put the number in the right place if it appears just once
                if number_counter == 1:
                    for square in self.squares:
                        if square.y_cor == row_number and square.x_cor == right_x_cor:
                            square.number = number
                            square.possible = [number]

        """ Check if a possibility appears just once i the columns """
        for column_number in range(9):
            # Save all possibilities for one column
            column_possibilities = []
            for square in self.squares:
                if square.x_cor == column_number:
                    column_possibilities.append(square.possible)

            # Count the number of times each number exists in column_possibilities
            for number in range(1, 10):

                number_counter = 0      # The number of times a number appears in column_possibilities
                right_y_cor = 0         # The right y coordinate for the number

                # Do the counting, if a number appears once ==> number_counter == 1
                for possibility, y_cor in zip(column_possibilities, range(len(column_possibilities))):
                    if number in possibility:
                        number_counter += 1
                        right_y_cor = y_cor

                # Put the number in the right place if it appears just once
                if number_counter == 1:
                    for square in self.squares:
                        if square.x_cor == column_number and square.y_cor == right_y_cor:
                            square.number = number
                            square.possible = [number]

        """ Check if possibilities appears just once in the boxes """
        for row_number in range(9):
            # Save possibilities for one box
            box_poss = []
            for square in self.squares:
                if square.box == row_number:
                    box_poss.append([square.possible, square.x_cor, square.y_cor])

            # Count the number of times the number exists in box_possibilities
            for number in range(1, 10):

                box_counter = 0
                box_x_cor = 0
                box_y_cor = 0

                # Do the counting, if a number appears once ==> number_counter == 1
                for possibility in box_poss:
                    if number in possibility[0]:
                        box_counter += 1
                        box_x_cor = possibility[1]      # Save coordinates for the right box
                        box_y_cor = possibility[2]

                # Put the number in the right place if it appears just once
                if box_counter == 1:
                    for square in self.squares:
                        if square.x_cor == box_x_cor and square.y_cor == box_y_cor:
                            square.number = number
                            square.possible = [number]


    def is_finished(self):
        """ Check if the win or fail conditions has ben met """

        # Check if all squares have numbers
        check = True
        counter = len(self.squares)
        for square in self.squares:
            if square.number == 0:
                check = False
                counter -= 1

        # Print happy statement if the sudoku is solved
        if counter == len(self.squares):
            print("The sudoku was solved after", self.tries, "iterations")

        # Check if the maximum allowed tries has been done
        if self.tries >= self.max_tries:
            check = True
            print("The sudoku could not be solved after", self.tries, "iterations...")

        return check

    def load_sudoku(self):
        """ Load sudoku from file and put the inforation in squares-list"""
        # Create the list that will be returned
        squares = []

        # loop through the sudoku rows
        y = 0
        id_num = 0
        for row in sudoku:
            x = 0
            for number in row:
                square = Square()                   # Create a Square-object
                square.number = number              # Save the number in the Square-object
                if number != 0:                     # If the number is known
                    square.possible = [number]      # then the number is the only possibility
                square.id_num = id_num
                square.x_cor = x                    # Save the coordinates in Square-object
                square.y_cor = y

                # Call a method that calculates the box number
                square.box = set_box_number(square.x_cor, square.y_cor)

                id_num += 1
                x += 1
                squares.append(square)  # Save the Square in the squares-list
            y += 1
        return squares

    def print_sudoku(self):
        """ A method that prints the current squares-list """
        output = []
        output_row = []
        # Create list in lists for all square numbers
        for square in self.squares:
            output_row.append(square.number)
            if square.x_cor == 8:
                output.append(output_row)
                output_row = []

        # Print the numbers in output-list
        for row in output:
            print(row)
        print(" ")

    def remove_possibilities_combinations(self):
        """ Remove possibilities based on combination of the other squares combinations """
        pass

    def remove_possibilities_simple(self):
        """ A method that checks the rows, columns and boxes and removes any simple possibilities for the Squares"""
        # Loop through the squares to check them
        for square_check in self.squares:
            # The square has to not be defined
            if square_check.number == 0:
                # loop through all the other squares
                for square_loop in self.squares:
                    # Check if looped square is in the same row, column or box as the cecked square
                    if (square_check.x_cor == square_loop.x_cor
                            or square_check.y_cor == square_loop.y_cor
                            or square_check.box == square_loop.box):
                        # Check so that the square does not interact with it self
                        if not square_check.id_num == square_loop.id_num:
                            # Remove the looped squares number if it is in the possible number for square_check
                            if square_loop.number in square_check.possible:
                                square_check.possible.remove(square_loop.number)
                            # Set the right number if there is just one possibility
                            if len(square_check.possible) == 1:
                                square_check.number = square_check.possible[0]


# Run the program
run = SudokuSolver()
