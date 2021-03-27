"""
@Author  : Lord_Bao
@Date    : 2021/3/27

"""
import pylab
from scipy import integrate
import random


def gaussian(x, mu, sigma):
    factor1 = 1 / (sigma * (2 * pylab.pi) ** 0.5)
    factor2 = pylab.e ** (- (x - mu) ** 2 / (2 * sigma ** 2))
    return factor1 * factor2


def check_empirical_rule():
    mu_list = [i for i in range(-10, 11)]
    sigma_list = [i for i in range(1, 10)]
    for mu in mu_list:
        for sigma in sigma_list:
            print("mu:" + str(mu) + ",sigma:" + str(sigma))
            for std in [1, 1.96, 2, 3]:
                # gaussion(x,mu,sigma),x是自变量 ,mu - std * sigma, mu + std * sigma是针对此的积分上下限。
                # (mu, sigma) 相当于是赋常量值。 这里是为了验证 经验法则独立于 mu 和 sigma
                # integrate.quad 会返回一个元组,第一个元素是积分值,第二个元素是绝对误差
                # http://scipy.github.io/devdocs/generated/scipy.integrate.quad.html#scipy.integrate.quad
                print(
                    "fraction within " + str(std) + " std:" + str(
                        integrate.quad(gaussian, mu - std * sigma, mu + std * sigma, (mu, sigma))[0])
                )


if __name__ == '__main__':
    check_empirical_rule()
