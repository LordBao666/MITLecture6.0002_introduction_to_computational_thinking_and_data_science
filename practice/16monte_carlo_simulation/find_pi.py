"""
@Author  : Lord_Bao
@Date    : 2021/3/27

"""
import pylab
import random


def variance(sequence):
    """
    :param sequence:  有序序列 list tuple ，元素为数字
    :return:方差
    """
    mean = sum(sequence) / len(sequence)
    total = 0
    for elt in sequence:
        total += (elt - mean) ** 2
    return total / len(sequence)


def std_dev(sequence):
    """
    返回标准差
    """
    return variance(sequence) ** 0.5

