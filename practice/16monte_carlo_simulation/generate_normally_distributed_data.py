"""
@Author  : Lord_Bao
@Date    : 2021/3/27

"""

import random
import pylab


def make_plot(num, mu, sigma):
    """
    :param num:  通过random.gauss按照高斯分布,产生num个数字
    :param mu:   mean 均值
    :param sigma:  标准差

    """
    vals = []
    for i in range(num):
        val = random.gauss(mu, sigma)
        vals.append(val)
    # 权重 weights 是个大小为num的列表。它们将按照bin的划分到不同的bin去
    # 但是纵轴不再是出现的次数相加，而是原来每个数字 * 权重。 (这里的目的是得到频率）
    weights = [1 / num] * num
    bins = 400

    v = pylab.hist(vals, bins=bins, weights=weights)
    pylab.xlabel('x')
    pylab.axvline(mu + sigma, color="g")
    pylab.axvline(mu - sigma, color="g")
    pylab.ylabel("Relative Frequency")
    pylab.title("mu:" + str(mu) + ",sigma:" + str(sigma) + "samples" + str(num))

    # 计算 整个统计图相加
    print(sum(v[0][:]))
    # 计算 1.96 sigma之内的概率 (根据经验原则是95.00%）
    max_val = max(vals)
    min_val = min(vals)
    each_bin_length = (max_val - min_val) / bins
    start_bin = int((mu - 1.96 * sigma - min_val) / each_bin_length)
    print(start_bin)
    end_bin = int((mu + 1.96 * sigma - min_val) / each_bin_length)
    print(end_bin)
    print(sum(v[0][start_bin: end_bin + 1]))

    # 计算 2 sigma之内的概率 (根据经验原则是95.44%）
    start_bin = int((mu - 2 * sigma - min_val) / each_bin_length)
    print(start_bin)
    end_bin = int((mu + 2 * sigma - min_val) / each_bin_length)
    print(end_bin)
    print(sum(v[0][start_bin: end_bin + 1]))

    # 计算 3 sigma之内的概率 (根据经验原则是99.7%）
    start_bin = int((mu - 3 * sigma - min_val) / each_bin_length)
    print(start_bin)
    end_bin = int((mu + 3 * sigma - min_val) / each_bin_length)
    print(end_bin)
    print(sum(v[0][start_bin: end_bin + 1]))

    pylab.show()


if __name__ == '__main__':
    num = 1000000
    make_plot(num, 0, 100)
