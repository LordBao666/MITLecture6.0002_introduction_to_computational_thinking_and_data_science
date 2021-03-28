"""
@Author  : Lord_Bao
@Date    : 2021/3/28

"""
import pylab


def gaussian(x, mu, sigma):
    """
    均值为 mu, 标准差为sigma的正态分布的概率密度函数
    """
    factor1 = 1 / (sigma * (2 * pylab.pi) ** 0.5)
    factor2 = pylab.e ** (- (x - mu) ** 2 / (2 * sigma ** 2))
    return factor1 * factor2


def make_plot(mu, sigma, gap, start, end):
    """
       绘制局部正态分布概率密度函数。
       start 起始点  end 终止点
       gap表示间距
    """
    x_val = [start]
    y_val = [gaussian(start, mu, sigma)]
    pointer = start
    while pointer <= end:
        pointer += gap
        x_val.append(pointer)
        y_val.append(gaussian(pointer, mu, sigma))

    pylab.title("The probability of normal distribution of \n mu=" + str(mu) + ";sigma=" + str(sigma))
    pylab.xlabel("x")
    pylab.ylabel("probability")
    pylab.plot(x_val, y_val)
    pylab.show()


make_plot(0, 1, 0.005, -10, 10)
