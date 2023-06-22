def is_unique(integer_list) -> bool:
     # if the length changes, there is a duplicate element
    return len(set(integer_list)) == len(integer_list)


def is_unique_row(integer_matrix) -> bool:
    for row in integer_matrix:
        if not is_unique(row):
            return False
    return True
#
import copy
def hanten(M):
    A = copy.copy(M)
    for i in range(len(M)):
        for j in range(len(M)):
            A[j][i] = M[i][j]
    return A

def is_unique_col(M) -> bool:
    M = hanten(M)
    return is_unique_row(M)

def sudoku(M) -> bool:
    if not is_unique_row(M):
        return False
    if not is_unique_col(M):
        return False
    if not is_unique_masu(M):
        return False
    return True

def is_unique_masu(M) -> bool:
    for i, j in itertools.product([0, 3, 6]):
        #if not check_square(M, shift_i, shift_j):
            return False
    return True
import itertools
def check_square(M, i, j):
    return is_unique(M[k+i][j+l] for k, l in itertools.product(i, j))