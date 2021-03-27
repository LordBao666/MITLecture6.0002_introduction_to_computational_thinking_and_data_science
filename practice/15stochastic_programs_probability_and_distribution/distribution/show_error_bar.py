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


def show_error_baes(min_exp, max_exp, num_trials):
    means, sds, x_vals = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_vals.append(2 ** exp)

    for x in x_vals:
        head_ratio, mean, sd = sim_flip(x, num_trials)
        means.append(mean)
        sds.append(sd)
    print(sds)
    print(means)
    pylab.errorbar(x_vals, means, yerr=1.96 * pylab.array(sds))
    pylab.semilogx(base=2)
    pylab.title('Mean Fraction of Heads ( '
                + str(num_trials) + ' trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')
    pylab.show()


show_error_baes(3, 10, 100)
