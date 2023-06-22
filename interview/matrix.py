def is_unique(interger_list) -> bool:
	return len(set(interger_list)) == len(interger_list)


import copy
def hanten(matrix):
    new_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
            
    return new_matrix

def is_unique_col(matrix) -> bool:
	M = hanten(matrix)
	for row in M:
		if not is_unique(row):
			return False
	return True

def is_unique_row(row_matrix) -> bool:
	for row in row_matrix:
		if not is_unique(row):
			return False
	return True

def is_unique_masu(matrix):
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			sub_grid = []
			for x in range(3):
				for y in range(3):
					sub_grid.append(matrix[i + x][j + y])
			if not is_unique(sub_grid):
				return False
	return True
	

def check_suudo(matrix):
	if not is_unique_row(matrix):
		return False
	if not is_unique_col(matrix):
		return False
	if not is_unique_masu(matrix):
		return False
	return True
	

sudoku_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

not_sudoku_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 7]  
]


print(check_suudo(sudoku_board))
print(check_suudo(not_sudoku_board))

