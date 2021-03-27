"""
@Author  : Lord_Bao
@Date    : 2021/3/27

"""
import random
import pylab


def flip(num_flip):
    """
    返回num_flip次数下，每个面出现的概率
    """
    # 代表 1--6号出现次数 。index =0 对应1号
    die_req = [0, 0, 0, 0, 0, 0]
    for i in range(num_flip):
        die = random.choice(range(1, 6 + 1))
        die_req[die - 1] += 1

    die_prob = []
    for elt in die_req:
        die_prob.append(elt / num_flip)
    print(die_prob)
    return die_prob


def sim_flip(num_flip_per_trial, trials):
    final_die_prob = [0, 0, 0, 0, 0, 0]
    for trial in range(trials):
        die_prob = flip(num_flip_per_trial)
        for index in range(len(final_die_prob)):
            final_die_prob[index] += die_prob[index]
    for index in range(len(final_die_prob)):
        # 求平均概率
        final_die_prob[index] = final_die_prob[index] / trials
    print(final_die_prob)
    return final_die_prob


def make_plot(num_flip_per_trial, trials):
    final_die_prob = sim_flip(num_flip_per_trial, trials)
    pylab.plot(range(1, 6 + 1), final_die_prob, 'y', label="probability in practice")
    pylab.axhline(1 / 6, label="probability in theory")
    pylab.title("probability for die," + str(num_flip_per_trial) + " flip for " + str(trials) + " trials")
    pylab.ylabel("probability")
    pylab.xlabel("die")
    pylab.legend(loc="best")
    pylab.show()


make_plot(10, 100000)
