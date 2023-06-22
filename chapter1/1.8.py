'''

1 0 3 4 5 
6 7 8 9 10
11 12 13 14 15 

0 0 0 0 0
6 0 8 9 10
11 0 13 14 15 

'''

def zero_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0

    return matrix


print(zero_matrix([[1,0,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))