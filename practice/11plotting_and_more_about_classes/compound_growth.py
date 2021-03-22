"""
@Author  : Lord_Bao
@Date    : 2021/3/20

"""

import pylab

principal = 10000
interest_rate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interest_rate

pylab.title("5% Growth,Compounded Annually")
pylab.xlabel("Years of Compounding")
pylab.ylabel('Value of Principal ($)')
# [marker][line][color]
# 不传入line,那么就没有连线
pylab.plot(values, 'ok') # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
pylab.show()
