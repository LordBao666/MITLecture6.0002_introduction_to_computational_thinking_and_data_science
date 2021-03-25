"""
@Author  : Lord_Bao
@Date    : 2021/3/24

"""
import random


class FairRoulette(object):
    """
    一种赌博游戏--转盘赌。
    该玩法很多,比如奇偶，颜色(黑红),某个数值 或 某个序列。
    比如球转到 红1号格子 ,那么赌奇数,红色,1号，1到10号的就赢了。
    不过不同赌法的赔率肯定是不一样的。

    FairRoulette 没有 绿00 和 绿0则两种格子

    下面仅涉及赌某个数值的情况
    下面的一些词语：
    pocket ：格子(pocket本意就有口袋意思),每种格子对应一种号码
    ball : 小球
    pocket_odds : 格子的机会（详细看后面吧）
    spin :  旋转（表示进行一轮）
    bet ：下注，赌注
    """

    def __init__(self):
        # 转盘的格子 分为 1到36号
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        # 球
        self.ball = None
        # 格子的机会（但我理解而言是赔率）
        self.pocket_odds = len(self.pockets) - 1

    def spin(self):
        # 转动一次，小球随机进入某个格子
        self.ball = random.choice(self.pockets)

    def bet_pocket(self, pocket, bet):
        """
        下注
        :param pocket: 下注到那个格子
        :param bet: 赌注大小
        :return: 返回净利润
        """
        if self.ball == pocket:
            return bet * self.pocket_odds
        else:
            return -bet

    def __str__(self):
        return "Fair Roulette"


class EuropeanRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        # European Roulette 多了个绿0 ,实际上就是多了一个号码而已(使其为37）,但是这个号码不能选,而且赔率也不包含从部分。
        self.pockets.append(37)

    def __str__(self):
        return "European Roulette"


class AmericanRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        # European Roulette 多了个绿0 和绿00,实际上就是多了两个号码而已(使其为37,38）但是这个号码不能选。而且赔率也不包含从部分。
        self.pockets.append(37)
        self.pockets.append(38)

    def __str__(self):
        return "American Roulette"
