"""
@Author  : Lord_Bao
@Date    : 2021/3/20

"""
import random


def same_date(num_people, num_same):
    """
    :param num_people: 测试人数。
    :param num_same: 测试指标,即生日相等的人数
    :return: 返回测试人数中，同一天的生日的最高人数 是否大于 测试指标、  这是采样！！！！！！
    e.g  假设num_people 为10 ，num_same 为 3。该函数返回的就是10人中，是否至少有3个人的生日在同一天。
    是的化返回True，否则返回False。

    这里的生日分布是 根据 random 和 num_people 随机模拟的。显然，可以另写一个函数，传入一个数据结构存放生日状况也行。
    假设一年366天(即包含2月29号）
    """
    birthdays = [0] * 366  # 列表是支持 * 操作的,这个目的是创建长度为366的列表
    possible_date = range(366)
    for p in range(num_people):
        # 0 - 365中任选一个,选中的称作day 那么 birthdays[day ] + 1。也就是又有一个人的生日是day +1那天
        day = random.choice(possible_date)
        birthdays[day] += 1

    return max(birthdays) >= num_same


def birthday_prob(num_people, num_same, num_trials):
    """

    :param num_people: 测试人数
    :param num_same: 测试指标(num_people中，至少有num_same人共享生日）
    :param num_trials: 测试次数
    :return: 调用 same_date 函数num_trials次,返回 num_people中，至少有num_same人共享生日的次数/num_trials

    其中 至少有num_same人共享生日的次数 用 num_hits存储。

    测试人数的生日分布随机产生。

    当num_trials  足够大时，就可以模拟正常的概率。当然这里的生日数据是随机模拟的，可能反而不太准确。
    比如灾年出生率低，受影响的因素很大。可能不同的date的权重不一样。
    """
    num_hits = 0
    for trial in range(num_trials):
        if same_date(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials


def same_date_with_different_weight(num_people, num_same):
    #  实际情况是 不同天数生小孩的概率是不一样的。举个例子,女性怀孕40周分娩
    #  那么是9个月10天左右。而春节这种长假夫妻聚的时间长一点。那么我估计 10月 --12月的孩子估计
    #  更多吧。

    # 按照4年来算,2月29号比较奇葩，只有1天,单独拎出来
    # 4 * list(range(180, 270)) 是因为 6月到9月出生的人数的更多,这里理解为加权。
    # 具体参照从MIT Lecture4 的PPT,照片见common_birthday.png
    possible_date = 4 * list(range(0, 57)) + [58] \
                    + 4 * list(range(59, 366)) \
                    + 4 * list(range(180, 270))

    birthdays = [0] * 366
    for p in range(num_people):
        # 0 - 365中任选一个,选中的称作day 那么 birthdays[day ] + 1。也就是又有一个人的生日是day +1那天
        day = random.choice(possible_date)
        birthdays[day] += 1

    return max(birthdays) >= num_same


def birthday_prob_with_different_weight(num_people, num_same, num_trials):
    num_hits = 0
    for trial in range(num_trials):
        if same_date_with_different_weight(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials
