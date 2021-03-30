"""
@Author  : Lord_Bao
@Date    : 2021/3/30

"""

import random


def genNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a * x ** 2 + b * x + c
        yVals.append(theoreticalVal \
                     + random.gauss(0, 35))
    f = open(fName, 'w')
    f.write('x        y\n')
    for i in range(len(yVals)):
        f.write(str(yVals[i]) + ' ' + str(xVals[i]) + '\n')
    f.close()


xVals = [i for i in range(-16, -5)] + [i for i in range(6, 17)]
file_name1 = "Dataset 3.txt"
file_name2 = "Dataset 4.txt"
a, b, c = 3, 0, 0
genNoisyParabolicData(a, b, c, xVals, file_name1)
genNoisyParabolicData(a, b, c, xVals, file_name2)
