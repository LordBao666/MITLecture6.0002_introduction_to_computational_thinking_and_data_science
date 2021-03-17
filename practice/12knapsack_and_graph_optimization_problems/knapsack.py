"""
@Author  : Lord_Bao
@Date    : 2021/3/16

"""

"""
背包问题是最优解问题的一个代表,它至少有两个变种问题，即 0/1背包问题 和 连续性或部分性背包问题
连续性背包问题是很简单的问题 : 
假如你有一个桶 ,你面前有一堆金子沙 ,一堆银子沙。
那么我肯定是装金子,如果装不满,再装银子。
而连续性背包问题采用贪心算法 总是能找到最优解。


假设我们的最优解指的是 总价值最优,
那么采用不同的贪心策略得到的结果可能是不同的

举个极端的例子,比如我的背包是 3kg
1个1kg物品 的价值 3元, 1个3kg物品 的价值6元。
如果采用 每kg价值最高为贪心的标准,那么我们只能装1kg,价值才3元,
而显然如果将单个物品的价值最高 为贪心的标准,其实能得到更高的价值，即6元。

而如果1个1kg的是7元呢?那么每kg价值最高 为贪心的标准,反而却是更好的。
所以说，贪心算法并不能保证最优解,但是只要为我们接受就行。


0/1背包问题采用贪心算法就不一定能获取到最优解:
但是仍然采用贪心算法的原因是是 它的时间复杂度是 O(nlogn),
而0/1背包问题天生就是指数型的复杂度，如果采用暴力解决，那么效率很低。
其次以外,只要0/1背包产生的解只要我们能够接受即可，并不一定是最优解。
"""


class Item(object):
    """
        Item : a class which has 3 attributes,name(string),value(float),weight(float)
    """

    def __init__(self, name, value, weight):
        """
        :param name:  string
        :param value: float
        :param weight: float
        """
        self.name = name
        self.value = value
        self.weight = weight

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.name + ":<value:" + str(self.value) + ",weight:" + str(self.weight) + ">"


def weight_inverse(item):
    """
    :param item: Item
    :return: 1.0 / item.get_weight()
    """
    return 1.0 / item.get_weight()


def value(item):
    return item.get_value()


def density(item):
    return item.get_value() / item.get_weight()


def build_item_list(name_list, value_list, weight_list):
    """
        name_list,value_list,weight_list are of same length
    :param name_list: a list of string
    :param value_list: a list of float
    :param weight_list: a list of float
    :return: a list of Item
    """
    item_list = []
    for i in range(len(name_list)):
        item_list.append(Item(name_list[i], value_list[i], weight_list[i]))
    return item_list


def greedy(item_list, max_weight, value_standard_func):
    f"""

    :param item_list:  a list of items
    :param max_weight : the max weight that a knapsack can hold ,surely max_weight >= 0
    :param value_standard_func: a function ,which determines the value standard ,
           e.g less weight ,higher value or higher value / weight .
           it maps item to number(float)
           see more about #{density} #{value} #{weight_inverse} 
    :return: a tuple(result,total_value)
             result : a list of items  in desc order by value_standard_func
             total_value : the sum of  items' value of the result
             
         time complexity : O(nlogn)   ,主要是花费在排序上 
    """
    # 最好不要修改传入的item_list  算法复杂度 O(nlogn)
    # item_list的每个元素将作为value_standard_func的参数,并产生一个新的值。
    # 而 sorted将生产item_list的副本，并根据这些值对 item_list副本的元素进行重排。
    # 也就是说sorted函数并未破化item_list的结构，默认情况下是按照升序排序。
    # reverse=True的作用是降序排序
    item_list_copy = sorted(item_list, key=value_standard_func, reverse=True)
    result = []
    total_value = 0.0
    total_weight = 0.0
    # 算法复杂度 O(n)
    for elt in item_list_copy:
        if elt.get_weight() + total_weight <= max_weight:
            result.append(elt)
            total_value += elt.get_value()
            total_weight += elt.get_weight()

    return result, total_value


def test_greedy(item_list, max_weight, value_standard_func):
    f"""
       test greedy  algorithm   
       see more about #{greedy}
    """
    result, total_value = greedy(item_list, max_weight, value_standard_func)
    print("the total value is " + str(total_value))
    print("the items ", end=":")
    for elt in result:
        print(elt, end=" ")
    print("\n----------------------------------")


if __name__ == '__main__':
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    values = [175, 90, 20, 50, 10, 200]
    weight = [10, 9, 4, 2, 1, 20]

    item_list = build_item_list(names, values, weight)

    # ######## test case1   将最小的重量作为贪心准则 ########
    test_greedy(item_list, 20.0, weight_inverse)

    # ######## test case2   将最大的价值作为贪心准则 ########
    test_greedy(item_list, 20.0, value)

    # ######## test case3   将最大的单价作为贪心准则 ########
    test_greedy(item_list, 20.0, density)
