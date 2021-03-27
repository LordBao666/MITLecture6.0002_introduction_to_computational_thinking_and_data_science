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


def cv(sequence):
    """
    返回变异系数
    """
    mean = sum(sequence) / len(sequence)
    std = std_dev(sequence)
    try:
        return std / mean
    except ZeroDivisionError:
        return float("nan")


def flip(num_flip):
    """
    :param num_flip:  投掷 硬币次数
    :return: head / 投掷硬币次数。  也就是出现head的概率。
    """
    head = 0
    for i in range(num_flip):
        if "H" == random.choice(["H", "T"]):
            head += 1
    return head / num_flip


def sim_flip(num_flip_per_trials, trials):
    head_ratio = []
    for trial in range(trials):
        head_ratio.append(flip(num_flip_per_trials))

    mean = sum(head_ratio) / len(head_ratio)
    sd = std_dev(head_ratio)

    return head_ratio, mean, sd


def label_plot(num_flips, num_trials, mean, sd):
    pylab.title(str(num_trials) + 'trials of ' + str(num_flips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    # xycoords 放的方法 xy=(0.67, 0.5) 表示距离 left 0.67 bottom 0.5 的图示距离 size 应该是文本大小？？？
    pylab.annotate('Mean = ' + str(round(mean, 4)) +
                   '\nSD= ' + str(round(sd, 4)), size='x-large',
                   xycoords='axes fraction', xy=(0.67, 0.5))


def make_plot(num_flip1, num_flip2, num_trial):
    val1, mean1, sd1 = sim_flip(num_flip1, num_trial)
    label_plot(num_flip1, num_trial, mean1, sd1)
    pylab.hist(val1, bins=20)
    x_min, x_max = pylab.xlim()

    # 另外创建一个新的figure
    pylab.figure()
    # 两幅图的 x 坐标的range保持一样.
    pylab.xlim(x_min, x_max)
    val2, mean2, sd2 = sim_flip(num_flip2, num_trial)
    label_plot(num_flip2, num_trial, mean2, sd2)
    # 根据val的范围划分20个bin。注意这句话。这与xlim没有关系
    pylab.hist(val2, bins=20)
    pylab.show()


make_plot(100, 1000, 10000)
