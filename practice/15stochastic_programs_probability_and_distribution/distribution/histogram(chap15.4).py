"""
@Author  : Lord_Bao
@Date    : 2021/3/23

"""
import pylab
import random

vals = []

for i in range(1001):
    num_1 = random.choice(range(101))
    num_2 = random.choice(range(101))
    vals.append(num_1 + num_2)

pylab.hist(vals, bins=100)
pylab.show()
