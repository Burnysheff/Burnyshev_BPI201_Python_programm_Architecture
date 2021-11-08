import random

from Matrix import *

class squareMatrix(Matrix):
    def __init__(self):
        self.element = [[]]
        self.size = 0

    def Enter(self, arraySymbols, position):
        if position < len(arraySymbols):
            self.size = int(arraySymbols[position])
            position += 1
        for i in range (self.size):
            self.element.append([])
            for j in range (self.size):
                self.element[i].append(0)
        for i in range (self.size):
            for j in range (self.size):
                if position < len(arraySymbols):
                    self.element[i][j] = int(arraySymbols[position])
                    position += 1
                else:
                    self.element[i][j] = 0
        return position

    def EnterRandom(self):
        self.size = random.randint(3, 20)
        for i in range(self.size):
            self.element.append([])
            for j in range(self.size):
                self.element[i].append(0)
        for i in range(self.size):
            for j in range(self.size):
                self.element[i][j] = random.randint(1, 100)

    def Print(self, outfile):
        outfile.write("This is a square matrix!\n")
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
