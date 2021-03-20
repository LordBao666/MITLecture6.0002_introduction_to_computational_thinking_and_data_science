"""
@Author  : Lord_Bao
@Date    : 2021/3/20

"""
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
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天实际不加劝概率:" + str(birthday_prob(elt, num_same, num_trial)))
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天实际加劝概率:" + str(birthday_prob_with_different_weight(elt, num_same, num_trial)))
            # 这里num_same为2才能这样计算（如果num > 2,那么实际的数学公式将非常复杂)
            print(str(elt) + "人中至少有" + str(num_same) + "人的生日在同一天数学概率:" + str(math_prob))
