"""
@Author  : Lord_Bao
@Date    : 2021/3/24

"""

from roulette_entity import *
import pylab

"""
参看 play_fair_roulette.png

从 Trial 1 来看（相当于一个人）,从1把  到 1000把来看，净利率波动很大
也就是说一个人到底挣不挣钱，那么还真是一个随机的活儿。但是到后面1000把,和Trial1  10000的10000把很接近。
其实这里也是满足大数定律了。 只要 Trial 次数 *  单次Trial 足够大,那么玩一把的净利率可以近似等于 真实玩一把的概率p。

从 Trial 10000来看 ,此时基本算符合大数定律了,
无论是玩 1次 10次 还是 100次,1000次,平均净利率都接近于0.
这与数学计算。

   （35/36 * -bet   + 1/36  *  35/bet) / bet = 0 其实是很贴切的。

参看  play_different_roulette_for_10000trials.png
注意这个是在 10000次实验下的数据。
可以看出最终三种游戏的都趋于一个不同的值。
事实上, European Roulette 的 概率是
（36/37 * -bet   + 1/37  *  35/bet) / bet = -1/37。 因为我规定的绿0不能下注而且不能算作
PocketOdds,也就是赔率。所以显然它要低一些。
同理 American Roulette 更低。

看来Fair Roulette 是真的Fair。


"""


def play_roulette(game, num_spins, pocket, bet, to_print=False):
    """
     假设 num_spins次游戏下,下的注 bet  和 赌的pocket都是不变的。也就是说
     类似于我玩  5局，每局都是下注2美元,都下7号。
    :param game: Roulette 及其子类实例对象
    :param num_spins: 转几次
    :param pocket: 投的格子 比如投 2号
    :param bet: 下注 比如下注3美元
    :param to_print: 是否打印 ，辅助用的
    :return:  玩num_spins下的净利率  净利润/投入成本
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


def play_roulette_for_trials(num_trials, game, num_spins, pocket, bet, to_print=False):
    """
       假设 num_spins次游戏下,下的注 bet  和 赌的pocket都是不变的
      :param num_trials: 实验次数
      :param game: Roulette 及其子类实例对象
      :param num_spins: 转几次
      :param pocket: 投的格子 比如投 2号
      :param bet: 下注 比如下注3美元
      :param to_print: 是否打印，辅助用的
      :return  重复num_trials次实验,num_spins下的平均净利润率
      """
    net_profit = []
    for trial in range(num_trials):
        net_profit.append(play_roulette(game, num_spins, pocket, bet, to_print))

    return sum(net_profit) / len(net_profit)


def sim_play_roulette_for_different_trials_and_spins(num_trials_tuple, game, num_spins_tuple, pocket, bet,
                                                     to_print=False):
    """

    :param num_trials_tuple: 元组  实验次数  比如 1 10  100次
    :param game: FairRoulette 及其 子类的实例
    :param num_spins_tuple: 在一次实验下，投掷多少次

    为了方便展示，横轴为 num_spins,纵轴为净利率，不同的线代表不同的trials。
    """
    for trial in num_trials_tuple:
        net_profit_list = []
        for spin in num_spins_tuple:
            # 重复trial下,投掷spin次下的，平均净利率
            net_profit = play_roulette_for_trials(trial, game, spin, pocket, bet, to_print)
            net_profit_list.append(net_profit)
        label = "Trial " + str(trial)
        pylab.plot(num_spins_tuple, net_profit_list, 'o', label=label)


def sim_play_different_roulette(num_trial, game_tuple, num_spins_tuple, pocket, bet,
                                to_print=False):
    """
    :param num_trial:  实验次数
    :param game_tuple:  不同的转轮赌
    :param num_spins_tuple:
    :param pocket:
    :param bet:
    :param to_print:
    """
    for game in game_tuple:
        net_profit_list = []
        for spin in num_spins_tuple:
            net_profit = play_roulette_for_trials(num_trial, game, spin, pocket, bet, to_print)
            net_profit_list.append(net_profit)
        label = "Game " + str(game)
        pylab.plot(num_spins_tuple, net_profit_list, 'o', label=label)


if __name__ == '__main__':
    # num_trials = (1, 10000)
    # num_spins = (1, 10, 100, 1000)
    # fr = FairRoulette()
    # pocket = 2
    # bet = 1
    # sim_play_roulette_for_different_trials_and_spins(num_trials, fr, num_spins, pocket, bet, False)
    # pylab.xlabel("num spins")
    # pylab.ylabel("net profit ratio")
    # pylab.title("For different trials and  spins,the average net profit ratio")
    # pylab.semilogx()
    # pylab.legend(loc="best")
    # pylab.show()
    num_trials = 10000
    num_spins = (1, 10, 100, 1000)
    game = (FairRoulette(), EuropeanRoulette(), AmericanRoulette())
    pocket = 2
    bet = 1
    sim_play_different_roulette(num_trials, game, num_spins, pocket, bet, False)
    pylab.xlabel("num spins")
    pylab.ylabel("net profit ratio")
    pylab.title("For different games and  spins,the average net profit ratio")
    pylab.semilogx()
    pylab.legend(loc="best")
    pylab.show()
