import unittest

def zero_matrix(mtx):
    rows_to_zero = set([])
    cols_to_zero = set([])
    for row in range(len(mtx)):
        for col in range(len(mtx[row])):
            if mtx[row][col] == 0:
                rows_to_zero.add(row)
                cols_to_zero.add(col)
    for row in rows_to_zero:
        mtx[row] = [0] * len(mtx[row])
    for col in cols_to_zero:
        for row in range(len(mtx)):
            mtx[row][col] = 0

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected_matrix] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual,expected_matrix)

if __name__ == "__main__":
    unittest.main()