"""
@Author  : Lord_Bao
@Date    : 2021/3/24

"""

from roulette_entity import *
import pylab

"""
参看 play_fair_roulette.png
(Trial10  和 Trial 100可以无视)

从 Trial 1 来看（相当于一个人）,从1把  到 10000把来看，净利率波动很大（毕竟不是大数)。
也就是说一个人到底挣不挣钱，那么还真是一个随机的活儿。

从 Trial 1000 来看,除了1把(也不是大数）而言，其他都是正的。

按照大数定律 总的次数 为 trials * num_spins ,假设这个乘积很大 
那么真实回报率将趋于 真实p。从图中可以发现,这门游戏竟然有赚头,因为最终的概率比0高（
当然前提是你没日没夜，有资本情况下，玩超多次）

"""


def play_roulette(game, num_spins, pocket, bet, to_print=False):
    """
     假设 num_spins次游戏下下,下的注 bet  和 赌的pocket都是不变的
    :param game: Roulette 及其子类实例对象
    :param num_spins: 转几次
    :param pocket: 投的格子
    :param bet: 柱子
    :param to_print: 是否打印
    :return:  净利率  净利润/投入成本
    """
    # 投入成本
    total_bet = num_spins * bet
    # 净利润
    total_net_profit = 0
    for i in range(num_spins):
        game.spin()
        net_profit = game.bet_pocket(pocket, bet)
        total_net_profit += net_profit
    if to_print:
        print("num of spins :", num_spins, "of", game)
        print("total_net_profit_ratio:", 100 * (total_net_profit / total_bet), "%")
    return total_net_profit / total_bet


def sim_roulette_for_different_num_pins(num_trials, game, num_spins, pocket, bet, to_print=False):
    """
       假设 num_spins次游戏下,下的注 bet  和 赌的pocket都是不变的
      :param num_trials: 实验次数
      :param game: Roulette 及其子类实例对象
      :param num_spins: 转几次,此为元组 (10,100,1000)
      :param pocket: 投的格子
      :param bet: 柱子
      :param to_print: 是否打印
      :return  返回 num_trials下,不同num_spins下的平均净利润率
      """
    # 不同 num spin下，在相同trials的平均净利率
    total_net_profit_ratio = []
    for elt in num_spins:
        net_profit_ratio_for_this_num_pin = []
        for i in range(num_trials):
            net_profit_ratio_for_this_num_pin.append(play_roulette(game, elt, pocket, bet, False))
        total_net_profit_ratio.append(sum(net_profit_ratio_for_this_num_pin) / len(net_profit_ratio_for_this_num_pin))
    return total_net_profit_ratio


if __name__ == '__main__':
    # fr = FairRoulette()
    # play_roulette(game=fr, num_spins=100, pocket=2, bet=1, to_print=True)
    fr = FairRoulette()
    # 不同num_trials
    num_trials = (1, 10, 100, 1000)
    num_spins = (1, 10, 100, 1000, 10000)
    for trial in num_trials:
        net_ratio = sim_roulette_for_different_num_pins(trial, fr, num_spins, 2, 1, False)
        pylab.plot(num_spins, net_ratio, "o", label="Trial " + str(trial) + " for " + str(num_spins) + " spins")

    pylab.xlabel("num spins")
    pylab.ylabel("net profit ratio")
    pylab.title("For different trials and  spins,the average net profit ratio")
    pylab.semilogx()
    pylab.legend(loc="best")
    pylab.show()
