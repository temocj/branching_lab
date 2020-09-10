import unittest, pdb

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    # Tests
    def setUp(self):
        self.matrix_1 = Matrix("9 8 7\n5 3 2\n6 6 7")        # square matrix
        self.matrix_2 = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6") # tall matrix
        self.matrix_3 = Matrix("1 2 3 4\n5 6 8 8\n9 8 7 6")  # wide matrix
        self.matrix_4 = Matrix("89 1903 3\n18 3 1\n9 4 800") # irregular matrix

    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual([1], matrix.row(1))

    # Test can extract a given row
    def test_extract_row(self):
        self.assertEqual([9, 8, 7], self.matrix_1.row(1))

    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20
    def test_extract_row_variable_digits(self):
        self.assertEqual([1, 2], Matrix("1 2\n10 20").row(1))

    # Test can extract row from non-square matrix
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6
    def test_extract_row__non_square_matrix(self):
        self.assertEqual([8, 7, 6], self.matrix_2.row(4))

    # Test can extract a column
    def test_extract_column(self):
        self.assertEqual([9, 5, 6], self.matrix_1.column(1))

    # Test can extract column from a one number matrix
    def test_extract_column_from_one_number_matrix(self):
        self.assertEqual([4], Matrix("4").column(1))

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6
    def test_extract_column__non_square_matrix(self):
        self.assertEqual([4, 8, 6], self.matrix_3.column(4))

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800
    def test_extract_column__irregular_matrix(self):
        self.assertEqual([1903, 3, 4], self.matrix_4.column(2))
