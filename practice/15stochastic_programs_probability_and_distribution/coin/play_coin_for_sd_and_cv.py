"""
@Author  : Lord_Bao
@Date    : 2021/3/24

"""
import random
import pylab
import math

"""
查看ratio_mean_head_over_tail.png 和 ratio_sd_head_over_tail.png
可以得出,随着num_flips次数增加,head/tail 逐渐倾向于 1.0，而标准差逐步在下降。
这说明一件事情,也就是在num_flip增加后, 不同次实验之间的head/tail的数据都接近1，也就是离散程度
不高.从这一层面通过标准差来评估  mean是不是值得信赖的。

查看 mean_head_minus_tails.png 和 sd_head_minus_tails.png
标准差不能孤立来看，要结合均值。 上面那个ratio 的mean 和 std能分析的原因是 mean趋于平稳而std下降，并且std的
级别比mean小得多,显然说明 mean的可信度越来越高。

在mean 和 std都变动的情况下，不能仅仅看std的变化情况。
这个时候要介入变异系数cv ,当mean经常变化的时候，变异系数比 标准差更加可靠。cv越小，数据越集中。
具体可以参考右边的 ratio_cv_head_over_tail.png  和 cv_head_minus_tails.png

ratio的cv  和 std表明的结果是差不多的,而 diff 的 cv  和 std表明则是不一样的，从某种程度而言,std把我们误导了。
书上将trial扩大到1000,发现cv仍然是上下波动的,而且控制在0.74到0.78.
这说明两个事情,
1.head - tails的分散程度  和 num_flips无关。 
2. 当cv在1之间，都视作是低方差，即cv在1之间是head-tails的离散程度低的必要条件,注意是必要条件。

还有cv的优势是  可以忽略 量纲（kg，m)  和 不同mean之间的 离散程度。
缺点是  如果mean比较小的话,那么mean微弱的变化 都能导致cv很大的变化,而且当mean为0的时候是没有定义的。
标准差可以构建置信水平,而cv是不行的。
"""


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


def flip(num_flips):
    """
    :param num_flips:   次数
    :return: 二元组 head数 和 tail数

    """
    head = 0
    for flip in range(num_flips):
        if 'H' == random.choice(["H", "T"]):
            head += 1

    tail = num_flips - head
    return head, tail


def make_plot(x_vals, y_vals, title, x_label, y_label, style, logx=False, logy=False):
    pylab.figure()
    pylab.plot(x_vals, y_vals, style)
    pylab.title(title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    if logx:
        pylab.semilogx()
    if logy:
        pylab.semilogy()


def flip_plot(min_exp, max_exp, num_trials):
    """
     由min_exp,max_exp生成 一系列 2 ** min_exp, 2**(min_exp+1) ....  2 ** max_exp。
     这些序列将作为 num_flips的实际参数

    """
    ratio_mean, diff_mean, ratio_sd, diff_sd, x_axis = [], [], [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flip in x_axis:
        diffs, ratios = [], []
        for trial in range(num_trials):
            num_heads, num_tails = flip(num_flip)
            try:
                ratios.append(num_heads / num_tails)
                diffs.append(abs(num_heads - num_tails))
            except ZeroDivisionError:
                continue

        # 求得num_trials次下,num_flip次的  ratio 的均值标准差 diff的均值 标准差
        ratio_mean.append(sum(ratios) / len(ratios))
        ratio_sd.append(std_dev(ratios))
        diff_mean.append(sum(diffs) / len(diffs))
        diff_sd.append(std_dev(diffs))

    title = "Mean Heads/Tails Ratios(" + str(num_trials) + ") Trials"
    make_plot(x_axis, ratio_mean, title, "number of flips", "Mean heads/tails", 'ok', logx=True)
    title = "SD Heads/Tails Ratios(" + str(num_trials) + ") Trials"
    make_plot(x_axis, ratio_sd, title, "number of flips", "SD heads/tails", 'ok', logx=True, logy=True)

    title = "Mean abs(Heads-Tails) (" + str(num_trials) + ") Trials"
    make_plot(x_axis, diff_mean, title, "number of flips", "Mean abs(Heads-Tails)", 'ok', logx=True, logy=True)
    title = "SD  abs(Heads-Tails) (" + str(num_trials) + ") Trials"
    make_plot(x_axis, diff_sd, title, "number of flips", "SD  abs(Heads-Tails)", 'ok', logx=True, logy=True)
    pylab.show()


def flip_plot2(min_exp, max_exp, num_trials):
    """
     由min_exp,max_exp生成 一系列 2 ** min_exp, 2**(min_exp+1) ....  2 ** max_exp。
     这些序列将作为 num_flips的实际参数

    """
    ratio_mean, diff_mean, ratio_sd, diff_sd, ratio_cvs, diff_cvs, x_axis = [], [], [], [], [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flip in x_axis:
        diffs, ratios = [], []
        for trial in range(num_trials):
            num_heads, num_tails = flip(num_flip)
            try:
                ratios.append(num_heads / num_tails)
                diffs.append(abs(num_heads - num_tails))
            except ZeroDivisionError:
                continue

        # 求得num_trials次下,num_flip次的  ratio 的均值 方差 变异系数 diff的均值 方差 变异系数
        ratio_mean.append(sum(ratios) / len(ratios))
        ratio_sd.append(std_dev(ratios))
        ratio_cvs.append(cv(ratios))
        diff_mean.append(sum(diffs) / len(diffs))
        diff_sd.append(std_dev(diffs))
        diff_cvs.append(cv(diffs))

    title = "Mean Heads/Tails Ratios(" + str(num_trials) + ") Trials"
    make_plot(x_axis, ratio_mean, title, "number of flips", "Mean heads/tails", 'ok', logx=True)
    title = "SD Heads/Tails Ratios(" + str(num_trials) + ") Trials"
    make_plot(x_axis, ratio_sd, title, "number of flips", "SD heads/tails", 'ok', logx=True, logy=True)
    title = "CV Heads/Tails Ratios(" + str(num_trials) + ") Trials"
    make_plot(x_axis, ratio_cvs, title, "number of flips", "CV heads/tails", 'ok', logx=True, logy=True)

    title = "Mean abs(Heads-Tails) (" + str(num_trials) + ") Trials"
    make_plot(x_axis, diff_mean, title, "number of flips", "Mean abs(Heads-Tails)", 'ok', logx=True, logy=True)
    title = "SD  abs(Heads-Tails) (" + str(num_trials) + ") Trials"
    make_plot(x_axis, diff_sd, title, "number of flips", "SD  abs(Heads-Tails)", 'ok', logx=True, logy=True)
    title = "CV  abs(Heads-Tails) (" + str(num_trials) + ") Trials"
    make_plot(x_axis, diff_cvs, title, "number of flips", "CV abs(Heads-Tails)", 'ok', logx=True, logy=True)

    pylab.show()


# random.seed(0)
# flip_plot(4, 20, 20)
flip_plot2(4, 20, 20)