import pdb

class Matrix:
    def __init__(self, matrix_string):
        self.data = []

        index = 0
        length = len(matrix_string)
        row = 0
        col = 0
        while index < length:
            char = matrix_string[index]
            if char == " ":
                col += 1
            elif char == "\n":
                row += 1
                col  = 0
            else:
                next_space   = matrix_string.find( " ", index)
                next_newline = matrix_string.find("\n", index)
                next_space   = next_space   if next_space   != -1 else length
                next_newline = next_newline if next_newline != -1 else length
                number_end = min(next_space, next_newline)
                number = matrix_string[index:number_end]
                self._commit_number(number, row, col)
                index += max(0, len(number) - 1)
            index += 1

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
