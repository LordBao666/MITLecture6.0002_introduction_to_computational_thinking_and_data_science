"""
@Author  : Lord_Bao
@Date    : 2021/3/27

"""
import pylab
import random

"""
参考ratio_mean_for_head_prob.png
 每一次trial就是对 head的概率的统计,当这样的trial取无限次的时候,trial的平均概率将接近于head的真实概率p。

2.当然.准确来讲   每次  trial 的 num_flip是不一样的。针对每次trial下,说的是 head/num_flip的概率。那么多次trial的平均概率指的是，
在num_flip次下,head/num_flip的概率 将接近num_flip次下,head_num_flip的真实概率p。

所谓随机抽样的样本性质可以估计整体样本的性质,前提是随机。
若要满足随机，只有样本足够多才能保证随机，从而避免偶然误差。比如增加Trials,即重复随机抽样。比如增加单次Trial的样本。
需要注意我们这里研究的是 head的出现概率,所以增加Trial或单次Trial的样本都是允许的。但是如果研究的是
投掷num_flip 100次,head出现的概率。那么增加单次样本就不允许了,因为这里的事件变了,研究对象也变了。

或许举个另外的例子,
不放回从黑盒中抽取白球,假设6次抽取白球的概率。 像这种 限定死了次数的明确事件,只能通过增加trial来满足大数定律。
"""


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


def flip_by_trial(num_flip_per_trial, num_trials):
    """
    :param num_flip_per_trial:  单次实验投掷硬币次数
    :param num_trials: 实验次数
    :return: num_trial下的 平均 head 出现的概率
    """
    head_ratio = []
    for trial in range(num_trials):
        head_ratio.append(flip(num_flip_per_trial))
    return sum(head_ratio) / len(head_ratio)


def print_trace(num_flip_per_trial, num_trials, head_ratio):
    print("Flip " + str(num_flip_per_trial) + " times each trial,for " + str(num_trials) + " Trials")
    print("The mean of head ratio is " + str(head_ratio))


def sim_flip_with_graph(num_flip_per_trial_tuple, num_trials_tuple, to_print, log_x=False):
    """
    :param log_x: x轴是否取对数,意思是让x轴的呈现更加是指数的形式，调间距用的。比如 flip为 10,100,1000.取log 那么x轴之间就是 10^1,10^2,10^3
    :param num_flip_per_trial_tuple: e.g ( 1, 10,100)
    :param num_trials_tuple: e.g(1,10,100,1000,10000)
    :param to_print: 如果为True,打印num_trial下的 平均 head出现次数

    """
    for num_trials in num_trials_tuple:
        head_ratio_for_diff_num_flip = []
        for num_flip in num_flip_per_trial_tuple:
            ratio = flip_by_trial(num_flip, num_trials)
            head_ratio_for_diff_num_flip.append(ratio)
            # 打印num_trials次实验下,head出现的平均概率
            if to_print:
                print_trace(num_flip, num_trials, ratio)
        label = str(num_flip_per_trial_tuple) + " for " + str(num_trials) + " Trials"
        pylab.plot(num_flip_per_trial_tuple, head_ratio_for_diff_num_flip, "o", label=label)

    pylab.axhline(0.5)  # axhline(y=0, xmin=0, xmax=1, **kwargs) 画一条水平线,y表示起始y坐标,xmin 和 xmax表示水平覆盖的区间范围。--1之间
    pylab.ylim(0.0, 1.0)  # y轴的显示范围 0.0 - 1.0
    pylab.xlabel("Num Flip for each trial")
    pylab.ylabel("The mean ratio of head/num_flip")
    pylab.title("The mean ratio of head/num_flip for different num_flip and trials")
    pylab.legend(loc="best")
    if log_x:
        pylab.semilogx()  # 默认是以10为base
    pylab.show()


if __name__ == '__main__':
    # num_flip_tuple1 = (1, 10)
    # num_trial_tuple1 = (1, 10)
    # to_print = True
    # sim_flip_with_graph(num_flip_tuple1, num_trial_tuple1, to_print, True)
    num_flip_tuple1 = (1, 10, 100, 1000)
    num_trial_tuple1 = (1, 10, 100, 1000, 10000)
    to_print = True
    sim_flip_with_graph(num_flip_tuple1, num_trial_tuple1, to_print, True)
