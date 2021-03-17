"""
@Author  : Lord_Bao
@Date    : 2021/3/17

"""
import random


class Item(object):
    """
        Item : a class which has 3 attributes,name(string),value(number),weight(number)
    """

    def __init__(self, name, value, weight):
        """
        :param name:  string
        :param value: number
        :param weight: number
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


def build_item_list(name_list, value_list, weight_list):
    """
        name_list,value_list,weight_list are of same length
    :param name_list: a list of string
    :param value_list: a list of number
    :param weight_list: a list of number
    :return: a list of Item
    """
    item_list = []
    for i in range(len(name_list)):
        item_list.append(Item(name_list[i], value_list[i], weight_list[i]))
    return item_list


def max_val(to_consider_items, avail):
    """

    :param to_consider_items:  将要考虑的物品
    :param avail: 背包剩余空间
    :return: 二元组 (best_value,list_to_be_taken)
    best_value表示在将要考虑的物品中，挑选出不大于背包容量的最大价值
    list_to_be_taken 表示的就是从to_consider_items挑选的物品 ,他们能创造最好的best_value
    """
    # base_case: 没要考虑的物品 或是 背包容量为0
    if len(to_consider_items) == 0 or avail == 0:
        return 0, []

    if to_consider_items[0].get_weight() > avail:
        return max_val(to_consider_items[1:], avail)
    else:
        item_value = to_consider_items[0].get_value()
        # 探索左子树
        value1, list1 = max_val(to_consider_items[1:], avail - to_consider_items[0].get_weight())
        value_with_item = value1 + item_value
        list1.append(to_consider_items[0])

        # 探索右子树
        value_without_item, list2 = max_val(to_consider_items[1:], avail)

        if value_with_item > value_without_item:
            return value_with_item, list1
        else:
            return value_without_item, list2


def max_val_with_memo(to_consider_items, avail, memo={}):
    """
      :param to_consider_items:  将要考虑的物品
      :param avail: 背包剩余空间
      :param memo:  字典  key 为二元组 第一个元素是len(考虑列表的长度），第二个元素为背包剩余容量
                          value 为二元组，第一个元素 在可考虑列表和背包剩余容量下，带来的最大价值best_value
                                        第二个元素是将带走的物品,用元组表示
      :return: 二元组 (best_value,list_to_be_taken)
      best_value表示在将要考虑的物品中，挑选出不大于背包容量的最大价值
      list_to_be_taken 表示的就是从to_consider_items挑选的物品 ,他们能创造最好的best_value
      这里是用二元组存储的list_to_be_taken

      这个需要注意一点, 字典的Key 是一个二元组(x,y),x和y都是整数,这很好(key最好不要用浮点)
                           字典的Value 也是一个二元组(x,y)  x是数字,而y是一组元素,推荐y用元组而不是列表。
                           因为你有可能不小心就破坏了y的结构！！！！
      """
    result = None  # python中可以不这样做,但是我习惯java了
    # 如果在memo中存在
    if (len(to_consider_items), avail) in memo:
        result = memo[len(to_consider_items), avail]

    elif len(to_consider_items) == 0 or avail == 0:
        result = (0, ())
    elif to_consider_items[0].get_weight() > avail:
        result = max_val_with_memo(to_consider_items[1:], avail, memo)
    else:
        item = to_consider_items[0]

        # 探索左子树
        value1, tuple1 = max_val_with_memo(to_consider_items[1:], avail - item.get_weight(), memo)
        value_with_item = value1 + item.get_value()

        # 探索右子树
        value_without_item, tuple2 = max_val_with_memo(to_consider_items[1:], avail, memo)

        if value_with_item > value_without_item:
            result = value_with_item, tuple1 + (item,)
        else:
            result = value_without_item, tuple2

        memo[len(to_consider_items), avail] = result
    return result


def build_many_items(item_num, max_value, max_weight):
    items = []
    for i in range(1, item_num + 1):
        items.append(Item(str(i), random.randint(1, max_value), random.randint(1, max_weight)))
    return items


if __name__ == '__main__':
    # # ##############################当item的数量较小时 ###################
    # names = ['a', 'b', 'c', 'd']
    # values = [6, 7, 8, 9]
    # weights = [3, 3, 2, 5]
    # item_list = build_item_list(names, values, weights)
    #
    # knapsack_weight = 5
    # best_value, items_to_be_taken = max_val(item_list, knapsack_weight)
    # print("best value -->" + str(best_value))
    # for elt in items_to_be_taken:
    #     print(elt)
    # ##############################当item的数量较小时 ###################

    # ###########################当item的数量较大时 ####################
    # item_list = build_many_items(25, 10, 10)
    # knapsack_weight = 50
    # best_value, items_to_be_taken = max_val(item_list, knapsack_weight)
    # print(best_value)
    # for elt in items_to_be_taken:
    #     print(elt)
    # ###########################当item的数量较大时 ####################

    # ###########################当item的数量较小时,采用memo ####################
    # names = ['a', 'b', 'c', 'd']
    # values = [6, 7, 8, 9]
    # weights = [3, 3, 2, 5]
    # item_list = build_item_list(names, values, weights)
    #
    # knapsack_weight = 5
    # best_value, items_to_be_taken = max_val_with_memo(item_list, knapsack_weight)
    # print("best value -->" + str(best_value))
    # for elt in items_to_be_taken:
    #     print(elt)
    # ###########################当item的数量较小时,采用memo ####################

    # ###########################当item的数量较大时,采用memo 和 普通比较 ####################
    item_list = build_many_items(100, 10, 10)
    knapsack_weight = 50
    # best_value, items_to_be_taken = max_val(item_list, knapsack_weight)
    # print(best_value)
    # for elt in items_to_be_taken:
    #     print(elt)
    print("#########################华丽分割线################################")
    best_value, items_to_be_taken = max_val_with_memo(item_list, knapsack_weight)
    print(best_value)
    for elt in items_to_be_taken:
        print(elt)
