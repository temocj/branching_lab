import pdb

class Matrix:
    def __init__(self, matrix_string):
        self.data = []

        index = 0
        length = len(matrix_string)
        number = ""
        row = 0
        col = 0
        while index < length:
            char = matrix_string[index]
            if char == " ":
                self._commit_number(number, row, col)
                number = ""
                col += 1
            elif char == "\n":
                self._commit_number(number, row, col)
                number = ""
                row += 1
                col = 0
            else:
                number = number + char
            index += 1
        self._commit_number(number, row, col)

    def _commit_number(self, number, row, col):
        if number != "":
            if row >= len(self.data):
                self.data.append([int(number)])
            else:
                self.data[row].append(int(number))

    def row(self, index):
        row = []
        for el in self.data[index-1]:
            row.append(el)
        return row

    def column(self, index):
        col = []
        for i in range(0, len(self.data)):
            col.append(self.data[i][index-1])
        return col
