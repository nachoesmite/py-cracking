import unittest
import copy
def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(element[i] for element in reversed(matrix))) 
    return new_matrix

def rotate_matrix_2(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix


def the_nacho_way(matrix):
    levels = len(matrix) // 2
    cardinality_index = len(matrix) - 1
    for level in range(levels):
        for i in range(level, cardinality_index - level):
            # we need to store one to avoid loosing it
            top_row = level
            top_column = i
            bottom_row = cardinality_index - level
            bottom_column = cardinality_index - i
            left_row = cardinality_index - i
            left_column = level
            right_row = i
            right_column = cardinality_index - level


            top = matrix[top_row][top_column]
            matrix[top_row][top_column] = matrix[left_row][left_column]
            matrix[left_row][left_column] = matrix[bottom_row][bottom_column]
            matrix[bottom_row][bottom_column] = matrix[right_row][right_column]
            matrix[right_row][right_column] = top
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

    def test_rotate_matrix_2(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix_2(copy.deepcopy(test_matrix))
            self.assertEqual(actual, expected)

    def test_the_nacho_way(self):
        for [test_matrix, expected] in self.data:
            actual = the_nacho_way(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
