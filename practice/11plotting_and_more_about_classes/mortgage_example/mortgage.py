"""
@Author  : Lord_Bao
@Date    : 2021/3/22

"""
import pylab

"""
The point of this exercise is to provide some experience in the incremental
development of a set of related classes, not to make you an expert on mortgages.


这部分详情见笔记中的具体分析,我觉得这个案例很有意思。
"""


def find_payment(loan, r, m):
    """
    :param loan: 按揭
    :param r: 固定的月利率
    :param m: 预计几月完成按揭付款
    :return: 每个月支付金额
    """
    # 具体公式推算 查看 formula.png
    # 提示假设一个月付完loan 。那么 x = loan(1+r)
    # 假设两个月付完loan。那么 x(1+r) + x = loan(1+r） ** 2
    # 假设 m 个月付完loan。那么 x(1+r) ** m-1  ....  +x = loan (1+r) ** m
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage(object):
    def __init__(self, loan, ann_rate, months):
        """
        :param loan: 按揭
        :param ann_rate: 年利率
        :param months: 月份
        """
        self.loan = loan
        self.rate = ann_rate / 12
        self.months = months
        self.paid = [0.0]  # 每月初的付款金额 (第一月初未付款,所以为0)
        self.outstanding = [loan]  # 月初的待还款金额 (第一月初未付款,所以为loan)
        self.payment = find_payment(loan, self.rate, months)  # 每月预计付款
        self.legend = None  # 描述信息

    def make_payment(self):
        """
        每月付款 更新paid 和 outstanding
        """
        self.paid.append(self.payment)
        self.outstanding.append(self.outstanding[-1] * (1 + self.rate) - self.payment)

    def get_total_paid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plot_payments(self, style):
        # FixedWithPts 的self.paid[0]  并不是0.0
        pylab.plot(self.paid[1:], style, label=self.legend)

    def plot_balance(self, style):
        pylab.plot(self.outstanding, style, label=self.legend)

    def plot_tot_pd(self, style):
        """
        画 每个月的付款累积量
        """
        tot_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            tot_pd.append(tot_pd[-1] + self.paid[i])
        pylab.plot(tot_pd, style, label=self.legend)

    def plot_net(self, style):
        tot_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            tot_pd.append(tot_pd[-1] + self.paid[i])

        # self.outstanding 的金额一直是相对最开始的价格,求出来的equity_acquired 是 每个月累积交的钱(相对于开始的价格)
        equity_acquired = pylab.array([self.loan] * len(self.outstanding))
        equity_acquired = equity_acquired - pylab.array(self.outstanding)

        # net  就是 实际的累积交的钱 - 换算成开始交的钱的累积。画出来的图,也就是累积多交的钱。
        net = pylab.array(tot_pd) - equity_acquired
        pylab.plot(net, style, label=self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = "Fixed ," + str(round(r * 100, 2)) + "%"


class FixedWithPoints(Mortgage):
    """
     相比 Fixed, 这个方案在最初会付款 loan * (pts / 100),而适当的 r 会比Fixed的低
    """

    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100)]
        self.legend = "Fixed ," + str(round(r * 100, 2)) + "%, " + str(pts) + " points"


class TwoRate(Mortgage):
    """
     相比Fixed Rate 这种是两个Rate。 初始rate为teaser_rate，相比fixed_rate要低得多。后面的rate为rate,相比fixed_rate那要高得多
    """

    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        self.teaser_rate = teaser_rate
        self.teaser_months = teaser_months
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.next_rate = r / 12

        self.legend = str(teaser_rate * 100) + '% for ' + str(self.teaser_months) \
                      + ' months, then ' + str(round(r * 100, 2)) + '%'

    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:  # 假设teaser1个月,初始self.paid = [0.0] 所以需要+1
            self.rate = self.next_rate
            self.payment = find_payment(self.outstanding[-1], self.rate, self.months - self.teaser_months)
        Mortgage.make_payment(self)


def compare_mortgage(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    total_months = years * 12
    fixed1_mortgage = Fixed(amt, fixed_rate, total_months)
    fixed2_pts_mortgage = FixedWithPoints(amt, pts_rate, total_months, pts)
    var_mortgage = TwoRate(amt, var_rate2, total_months, var_rate1, var_months)
    morts = [fixed1_mortgage, fixed2_pts_mortgage, var_mortgage]
    for month in range(total_months):
        for mort in morts:
            mort.make_payment()

    for mort in morts:
        print(mort)
        print("Total payment = $" + str(int(mort.get_total_paid())))


def compare_mortgage_with_graph(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    total_months = years * 12
    fixed1_mortgage = Fixed(amt, fixed_rate, total_months)
    fixed2_pts_mortgage = FixedWithPoints(amt, pts_rate, total_months, pts)
    var_mortgage = TwoRate(amt, var_rate2, total_months, var_rate1, var_months)
    morts = [fixed1_mortgage, fixed2_pts_mortgage, var_mortgage]
    for month in range(total_months):
        for mort in morts:
            mort.make_payment()

    plot_mortgages(morts, amt)


def plot_mortgages(morts, amt):
    def label_plot(figure, title, x_label, y_label):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(x_label)
        pylab.ylabel(y_label)
        pylab.legend(loc="best")

    styles = ['-', '--', '-.']
    # 给figure命名
    payments, cost, balance, net_cost = 0, 1, 2, 3
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plot_payments(styles[i])
        pylab.figure(cost)
        morts[i].plot_tot_pd(styles[i])
        pylab.figure(balance)
        morts[i].plot_balance(styles[i])
        pylab.figure(net_cost)
        morts[i].plot_net(styles[i])

    label_plot(payments, 'Monthly Payments of $' + str(amt) +
               'Mortgages', 'Months', ' Monthly Payments')
    label_plot(cost, 'Cash outlay of $' + str(amt) + 'Mortgages', 'Months',
               'Total Payments')
    label_plot(balance, 'Balance Remaining of $' + str(amt) + 'Mortgages', 'Months',
               'Remaining    Loan Balance of $')
    label_plot(net_cost, 'Net Cost of $' + str(amt) + ' Mortgages',
               'Months', 'Payments - Equity $')

    pylab.figure(payments)
    pylab.savefig("payments")
    pylab.figure(cost)
    pylab.savefig("cost")
    pylab.figure(balance)
    pylab.savefig("balance")
    pylab.figure(net_cost)
    pylab.savefig("net_cost")
    pylab.show()


if __name__ == '__main__':
    compare_mortgage_with_graph(amt=200000, years=30, fixed_rate=0.07, pts=3.25, pts_rate=0.05, var_rate1=0.045,
                                var_rate2=0.095,
                                var_months=48)
