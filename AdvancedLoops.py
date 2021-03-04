"""Assignment 6-board game similar to tic-tac-toe"""


def boardGame(rows, columns):
    max_terminal_column = 120  # this sets the max terminal width
    max_terminal_rows = 30  # # this sets the max terminal width
    """the variables above were realised by running the get_terminal_size() in py cmd"""
    if rows < max_terminal_rows and columns < max_terminal_column:  # if both columns and rows are greater than the
        # terminal size,the function returns false.otherwise next line is executed and function returns True
        for r in range(rows):
            if r % 2 == 0:  # for each row if its an even number start looping through the colunm,else if odd go to
                # line 19 and print line
                for c in range(1, columns + 1):
                    if c % 2 == 1:  # for each column if its odd number print space
                        if c != columns:  # if end of the column is not reached continue printing on the same line
                            print(" ", end=" ")
                        else:
                            print(" ")  # if end on line is reached print space and go to next time
                    else:
                        print("/", end=" ")  # after the / always continue on the same time
            else:
                print("--" * columns)  # the dashes are printed according to the number of columns
        return True
    else:
        return False


"""
sample data:
    row-columns-function result
        19-19-True
        119-119-False

"""

board_rows = 19
board_columns = 20
print(boardGame(board_rows, board_columns))
""" i tried importing os and using using get_terminal_size() but i was getting an error
OSError: [WinError 6] The handle is invalid.how can i solve this.How else can a function return true/false ?
"""