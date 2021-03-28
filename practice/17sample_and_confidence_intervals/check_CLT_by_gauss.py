"""
@Author  : Lord_Bao
@Date    : 2021/3/28

"""
import random
import pylab

#  参看clt.png
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


def make_plot(num_per_trial, trials, mu, sigma, bins):
    means = []
    for each_trial in range(trials):
        result_list = []
        for num in range(num_per_trial):
            result = random.gauss(mu, sigma)
            result_list.append(result)
        # 记录每次trial 的 mean 和  variance
        means.append(sum(result_list) / len(result_list))
    # hatch 代表直方图的填充线
    # 参考 https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch
    label = "In  practice,mu:" + str(round(sum(means) / len(means), 4)) + ",variance:" + str(round(variance(means),4))
    # edge color 表示每条边的分隔线颜色
    pylab.hist(means, bins, color="orange", label=label, edgecolor='black', hatch="//")
    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.title("In theory,mu :" + str(mu) + ",variance/sample_size:" + str(sigma ** 2 / num_per_trial))
    pylab.legend(loc="best")
    pylab.show()


make_plot(10000, 1000, 1, 3, 100)
