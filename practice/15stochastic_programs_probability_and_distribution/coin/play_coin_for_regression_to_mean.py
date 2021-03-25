"""
@Author  : Lord_Bao
@Date    : 2021/3/24

"""
import random
import pylab

"""
这里不探究当次数接近于无穷时,投掷到正面（也是是head）的概率是不是1/2，这个可以参考roulette。
这里探究均值回归问题。

均值回归描述的是 ，如果极端事件发生后，下一次的事件将不那么极端。比如连续5次出现head，那么下面连续5次
中出现head的次数可能小于5次。但这也是一种可能性，并不是说这种极端事件就绝不再次发生。
具体可以参看regression_to_mean.png

而且这张图还说明一个问题，即赌徒谬误。可能极端事件发生以后，比如head的概率高于2/3。而下个trial不能说明 tail的概率就
高于1/2。
"""


def flip(num_flip):
    """
    :param num_flip: 投掷次数
    :return: 头/投掷次数
    """
    head_count = 0
    for i in range(num_flip):
        if 'H' == random.choice(["H", "T"]):
            head_count += 1

    return head_count / num_flip


def flip_for_trials(trials, num_flip):
    """
    :param trials: 实验次数
    :param num_flip: 每次实验的投掷次数
    :return: 返回trials次下的平均 头/投掷次数
    """
    head_hit = []
    for trial in range(trials):
        head_hit.append(flip(num_flip))
    return sum(head_hit) / len(head_hit)


def regression_to_mean(trials, num_flip):
    """
    :param trials:
    :param num_flip:
    假定一次Trial中，如果概率小于等于2/3 或是大于等于1/3，那么就将其视作极端事件.当然，怎样才算极端事件是你决定的，
    """
    total_head_ratio = []
    for trial in range(trials):
        total_head_ratio.append(flip(num_flip))
    extreme = []
    event_after_extreme = []

    for index in range(len(total_head_ratio) - 1):  # 不考虑最后一项
        ratio = total_head_ratio[index]
        if ratio <= (1/3) or ratio >= (2/3):
            extreme.append(ratio)
            event_after_extreme.append(total_head_ratio[index + 1])
    pylab.plot(range(len(extreme)), extreme, "oy", label="Extreme Ratio")
    pylab.plot(range(len(event_after_extreme)), event_after_extreme, 'xb', label="Event After Extreme Ratio")
    # 下面三个命令有点印象即可
    pylab.axhline(0.5)  # 水平画一条 y = 0.5的线
    pylab.xlim(-1, len(extreme) + 1)  # 水平限制在 -1 到 len(extreme) +1
    pylab.ylim(-1, 1)  # 垂直限制在 -1 到 1之间
    pylab.title("Regression to Mean")
    pylab.xlabel("Extreme and next trial")
    pylab.ylabel("Fraction Head")
    pylab.legend(loc="best")
    pylab.show()


if __name__ == '__main__':
    regression_to_mean(40, 15)
