from z3 import *
import itertools
# bool variables
B = []


###########################################################################
# Helper functions
# TODO: if you wish to define helper functions (not mandatory)
#       define them below (within the hashes)

###########################################################################


def warm_up():
    # example
    # Instantiate solver
    s = Solver()

    # Defining Boolean variables
    x1 = Bool('x1')
    x2 = Bool('x2')

    # Logic expressions
    and_exp = And(x1, x2)
    or_exp = Or([x1, x2])  # Can also take list of literals as argument
    not_exp = Not(x1)
    complex_exp = And([not_exp, or_exp])  # x1' and (x1 or x2)
    # Assert constraints into the solver
    s.add(complex_exp)

    if s.check() == unsat:
        print('No solution')
    else:
        m = s.model()
        print(m)
        x1_val = m.eval(x1)  # Use this function to evaluate the assignment of a given literal
        print(x1_val)


def solve_n_queens(n):
    # Instantiate solver
    s = Solver()
    # define Bool literal for each cell in the chessboard
    global B
    B = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(Bool('r_%d_c_%d' % (i, j)))
        B.append(row)
    ###########################################################################
    # TODO: add constraints
    raise NotImplementedError
    ###########################################################################
    return s


def generate_display_chessboard(n, s):
    # Generates alternating color chessboard as nested lists of rows
    colors = itertools.cycle(["\033[0;40m  \033[00m", "\033[0;47m  \033[00m"])
    chessboard = []
    for i in range(n):
        chessboard.append([next(colors) for _ in range(n)])
        if not n % 2: next(colors)
    chessboard = itertools.cycle(chessboard)
    chessboard = [next(chessboard) for _ in range(n)]
    chessboard = list(reversed(chessboard))
    # add queens to chessboard
    global B
    if s.check() == unsat:
        print('No solution')
    else:
        m = s.model()
        for i in range(n):
            for j in range(n):
                if m.eval(B[i][j]):
                    chessboard[i][j] = ' Q'
        display_chessboard(chessboard)
    return chessboard


def display_chessboard(chessboard):
    print('\033[1m' + '\033[4m' + '\033[94m' + f'Solution to {len(chessboard)}-Queens Problem:' + '\033[0m')
    for i in chessboard:
        out = ""
        for j in i:
            out += j
        # Print each sub list as a row
        print(out)


if __name__ == "__main__":
    warm_up()
    n = 4
    s = solve_n_queens(n)
    generate_display_chessboard(n, s)
