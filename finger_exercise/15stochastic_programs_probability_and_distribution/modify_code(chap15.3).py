"""
@Author  : Lord_Bao
@Date    : 2021/3/24

"""
import random
import pylab

"""
这道题的主要作用就是 
1.默认的划线容易误导,所以根据需要去掉线。
2.自己调整x轴或y轴的间距

"""


def flip_plot(min_exp, max_exp):
    """
     由min_exp,max_exp生成 一系列 2 ** min_exp, 2**(min_exp+1) ....  2 ** max_exp。
     这些序列将作为 num_flips的实际参数
    """
    ratios, diffs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flip in x_axis:
        num_heads = 0
        for flip in range(num_flip):
            if 'H' == random.choice(["H", "T"]):
                num_heads += 1
        num_tails = num_flip - num_heads
        try:
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    pylab.figure(1)

    pylab.semilogx(base=2)  # 修改代码
    pylab.semilogy()  # 修改代码
    pylab.title(" Difference Between Heads and Tails")
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(x_axis, diffs, 'ko')  # 修改代码
    pylab.figure(2)
    pylab.semilogx(base=2)  # 修改代码
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips ')
    pylab.ylabel(' Heads/ #Tails')
    pylab.plot(x_axis, ratios, 'ko')  # 修改代码
    pylab.show()


random.seed(0)
flip_plot(4, 20)
