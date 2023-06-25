'''

% # # # &      @ # # # %
# # # # #      # # # # #
# # # # #  ->  # # # # #
# # # # #      # # # # #
@ # # # !      ! # # # &


'''

def rotate(matrix):
    n = len(matrix)
    print(n)
    print(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        print(n/2)
        for j in range(int(n /2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n- 1 - j]
            matrix[i][n- 1 - j] = temp

    return matrix


# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            # matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            matrix[i][j] = matrix[j][i]

    print(matrix)

    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix

print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# def rotate_matrix2(matrix):
