import pdb

class Matrix:
    def __init__(self, matrix_string):
        self.data = []

        index = 0
        for row in matrix_string.split("\n"):
            self.data.append([])
            for number in row.split(" "):
                self.data[index].append(int(number))
            index += 1

    def row(self, index):
        return self.data[index-1]

    def column(self, index):
        return [el[index-1] for el in self.data]
