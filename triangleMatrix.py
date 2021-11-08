import random

from Matrix import *


class triangleMatrix(Matrix):
    def __init__(self):
        self.element = [[]]
        self.size = 0
        self.step = 0

    def Enter(self, arraySymbols, position):
        if position < len(arraySymbols) - 1:
            self.size = int(arraySymbols[position])
            self.step = int(arraySymbols[position])
            position += 2
        for i in range(self.size):
            self.element.append([])
            for j in range(self.size):
                self.element[i].append(0)
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    if position < len(arraySymbols):
                        self.element[i][j] = int(arraySymbols[position])
                        position += 1
                    else:
                        self.element[i][j] = 1
                elif i > j:
                    self.element[i][j] = self.element[j][j] + self.step * (i - j)
        return position

    def EnterRandom(self):
        self.size = random.randint(3, 20)
        self.step = random.randint(1, 20)
        for i in range(self.size):
            self.element.append([])
            for j in range(self.size):
                self.element[i].append(0)
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    self.element[i][j] = random.randint(1, 100)
                elif i > j:
                    self.element[i][j] = self.element[j][j] + self.step * (i - j)

    def Print(self, outfile):
        outfile.write("This is a triangle matrix!\n")
        for i in range(self.size):
            for j in range(self.size):
                outfile.write(str(self.element[i][j]))
                outfile.write(" ")
            outfile.write("\n")
        outfile.write("\nAverage is ")
        outfile.write(str(self.Average()))
        outfile.write("\n\n\n")

    def Average(self):
        result = 0.
        for i in range(self.size):
            for j in range(self.size):
                result += self.element[i][j]
        return result / (self.size * self.size)
