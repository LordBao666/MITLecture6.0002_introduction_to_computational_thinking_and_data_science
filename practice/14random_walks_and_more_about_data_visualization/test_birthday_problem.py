"""
@Author  : Lord_Bao
@Date    : 2021/3/20

"""
import pylab
from unittest import TestCase
from birthday_problem import *
import math


class Test(TestCase):
    def test_same_date(self):
        print(same_date(100, 3))

    def test_birthday_prob(self):
        print(birthday_prob(60, 3, 100000))

    def test_birthday_prob2(self):
        num_trial = 10000
        num_same = 2
        for elt in [2, 3, 10, 20, 30, 40, 50, 60]:
            # 计算公式参考 math_birthday.png
            math_prob = 1 - (math.factorial(366) / ((366 ** elt) * (math.factorial(366 - elt))))
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天实际概率:" + str(birthday_prob(elt, num_same, num_trial)))
            # 这里num_same为2才能这样计算（如果num > 2,那么实际的数学公式将非常复杂)
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天数学概率:" + str(math_prob))

    def test_birthday_prob3(self):
        num_trial = 10000
        num_same = 2
        for elt in [2, 3, 10, 20, 30, 40, 50, 60]:
            # 计算公式参考 math_birthday.png
            math_prob = 1 - (math.factorial(366) / ((366 ** elt) * (math.factorial(366 - elt))))
            print(
                str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天实际不加劝概率:" + str(birthday_prob(elt, num_same, num_trial)))
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天实际加劝概率:" + str(
                birthday_prob_with_different_weight(elt, num_same, num_trial)))
            # 这里num_same为2才能这样计算（如果num > 2,那么实际的数学公式将非常复杂)
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天数学概率:" + str(math_prob))

    def test_birthday_prob_with_grpah(self):
        num_trial = 10000  # 实验次数
        num_same = 2  # 相等人数为两人
        num_range = [2, 3, 10, 20, 30, 40, 50, 60]
        prob_math = []  # 数学计算的概率
        prob_ex_weight = []  # 实验的加权概率(根据实际情况模拟)
        prob_ex_without_weight = []  # 实验的不加权概率(不考虑实际情况)
        for elt in num_range:
            # 计算公式参考 math_birthday.png
            math_prob = 1 - (math.factorial(366) / ((366 ** elt) * (math.factorial(366 - elt))))
            prob_math.append(math_prob)
            prob_ex_weight.append(birthday_prob_with_different_weight(elt, num_same, num_trial))
            prob_ex_without_weight.append(birthday_prob(elt, num_same, num_trial))

        pylab.title("Probability of Math,Norm,Weighted under" + str(num_trial) + "trials")
        pylab.xlabel("The number of People")
        pylab.ylabel("Probability")
        pylab.plot(num_range, prob_math, label="Probability of Math")
        pylab.plot(num_range, prob_ex_weight, label="Probability of Weighted")
        pylab.plot(num_range, prob_ex_without_weight, label="Probability of Norm")
        pylab.legend(loc="best")
        pylab.show()

    def test_birthday_prob_with_grpah2(self):
        num_trial = 10000  # 实验次数
        num_same = [2, 4, 8, 16, 32, 64]

        prob_for_100 = []
        prob_for_200 = []
        prob_for_400 = []
        for elt in num_same:
            prob_for_100.append(birthday_prob_with_different_weight(100, elt, num_trial))
            prob_for_200.append(birthday_prob_with_different_weight(200, elt, num_trial))
            prob_for_400.append(birthday_prob_with_different_weight(400, elt, num_trial))

        pylab.title("Probability of 100,200,400 people under " + str(num_trial) + " trials")
        pylab.xlabel("The number of the same birthday")
        pylab.ylabel("Probability")
        # pylab.semilogx(base=2)
        pylab.plot(num_same, prob_for_100, label="Probability of 100")
        pylab.plot(num_same, prob_for_200, label="Probability of 200")
        pylab.plot(num_same, prob_for_400, label="Probability of 400")
        pylab.legend(loc="best")
        pylab.show()
