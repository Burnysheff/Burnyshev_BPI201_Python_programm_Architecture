import sys
import os.path
from Container import *
import time

start_time = time.time()
#----------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect command line!")
        exit()
    else:
        if sys.argv[1] != "file" and sys.argv[1] != "auto":
            print("Incorrect command line (few arguments)!")
            exit()
        else:
            if sys.argv[1] == "file":
                if os.path.exists(sys.argv[2]):
                    inputFileName = sys.argv[2]
                else:
                    print("File do not exist!")
                    exit()
            else:
                if not sys.argv[2].isdigit():
                    print("Enter a number please!")
                    exit()
                else:
                    number_generated = int(sys.argv[2])
            if len(sys.argv) == 3:
                outputFileName_first = "output1.txt"
                outputFileName_second = "output2.txt"
            elif len(sys.argv) == 4:
                outputFileName_first = sys.argv[3]
                outputFileName_second = "output2.txt"
            elif len(sys.argv) == 5:
                outputFileName_first = sys.argv[3]
                outputFileName_second = sys.argv[4]
            else:
                print("Incorrect command line!")
                exit()

    container = Container()
    if sys.argv[1] == "file":
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        strArray = str.replace("\n", " ").split(" ")
        container.PutIn(strArray)
    else:
        container.PutInRandom(number_generated)

    print('==> Start')

    ofile = open(outputFileName_first, 'w')
    container.Write(ofile)
    ofile.close()

    container.Sort()
    ofile = open(outputFileName_second, 'w')
    container.Write(ofile)
    ofile.close()

    print('==> Finish')
    print("--- %s seconds ---" % (time.time() - start_time))
