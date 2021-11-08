from squareMatrix import *
from diagonalMatrix import *
from triangleMatrix import *


class Container:
    def __init__(self):
        self.warehouse = []

    def PutIn(self, ArraySymbols):
        quantity = 0
        i = 0
        while i < len(ArraySymbols):
            if quantity == 10000:
                print("Matrices number cur at 10000!\n")
                break
            key = ArraySymbols[i]
            i += 1
            if key == '1':
                matrix = squareMatrix()
                i = matrix.Enter(ArraySymbols, i)
            elif key == '2':
                matrix = diagonalMatrix()
                i = matrix.Enter(ArraySymbols, i)
            elif key == '3':
                matrix = triangleMatrix()
                i = matrix.Enter(ArraySymbols, i)
            else:
                continue
            self.warehouse.append(matrix)

    def PutInRandom(self, number):
        for i in range(number):
            key = random.randint(1, 3)
            if key == 1:
                matrix = squareMatrix()
                matrix.EnterRandom()
            elif key == 2:
                matrix = diagonalMatrix()
                matrix.EnterRandom()
            elif key == 3:
                matrix = triangleMatrix()
                matrix.EnterRandom()
            else:
                continue
            self.warehouse.append(matrix)

    def Write(self, outfile):
        outfile.write("It is ")
        outfile.write(str(len(self.warehouse)))
        outfile.write(" matrices in container\n")
        outfile.write("Their average is ")
        outfile.write(str(self.Average()))
        outfile.write("\n")
        outfile.write("\n\n")
        for Matrix in self.warehouse:
            Matrix.Print(outfile)

    def Average(self):
        average = 0.
        for Matrix in self.warehouse:
            average += Matrix.Average()
        return average / len(self.warehouse)

    def Sort(self):
        for i in range(len(self.warehouse)):
            for j in range(0, len(self.warehouse) - 1):
                if self.warehouse[j].Average() > self.warehouse[j + 1].Average():
                    matrix = self.warehouse[j]
                    self.warehouse[j] = self.warehouse[j + 1]
                    self.warehouse[j + 1] = matrix
