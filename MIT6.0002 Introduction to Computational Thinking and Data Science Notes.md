

# MIT6.0002 Introduction to Computational Thinking and Data Science Notes

# Preface

&emsp;&emsp;文章目录大致分为Preface，Notes，Summary，Pset和Reference。由于我的数学不太好，第5--7章暂时没有整理笔记，待以后补充。详细的目录章节如下：

- [MIT6.0002 Introduction to Computational Thinking and Data Science Notes](#mit60002-introduction-to-computational-thinking-and-data-science-notes)
- [Preface](#preface)
- [Notes](#notes)
  * [1.贪心算法和背包问题](#1---------)
    + [1.1最优化模型](#11-----)
    + [1.2背包问题](#12----)
    + [1.3Lambda表达式](#13lambda---)
    + [1.4贪心算法](#14----)
  * [2.动态规划](#2----)
    + [2.1动态规划性质](#21------)
    + [2.2斐波拉契数列案例](#22--------)
    + [2.3动态规划解决0/1背包问题](#23------0-1----)
  * [3.图论基础和最短路径问题](#3-----------)
    + [3.1图论基础](#31----)
    + [3.2最短路径问题](#32------)
      - [3.2.1构建图模型](#321-----)
      - [3.2.2深度优先搜索](#322------)
      - [3.2.3广度优先搜索](#323------)
  * [4.随机游走和数据可视化](#4----------)
    + [4.1BirthdayProblem](#41birthdayproblem)
    + [4.2随机游走](#42----)
    + [4.3数据可视化](#43-----)
      - [4.3.1关于plot()](#431--plot--)
      - [4.3.2关于figure()](#432--figure--)
      - [4.3.3MIT的lecture风格代码](#433mit-lecture----)
  * [5.蒙特卡罗模拟](#5------)
  * [6.置信区间](#6----)
  * [7.采样和标准误差](#7-------)
  * [8.依据实验数据构建模型](#8----------)
    + [8.1Spring Demo](#81spring-demo)
      - [8.1.1目标函数](#811----)
      - [8.1.2Polyfit & Polyval](#812polyfit---polyval)
      - [8.1.3考虑实际情况](#813------)
    + [8.2Mystery Data Demo](#82mystery-data-demo)
      - [8.2.1Mystery Data 来源](#821mystery-data---)
      - [8.2.2如何看待模型好坏](#822--------)
      - [8.2.3过拟合问题&为何构建模型](#823------------)
      - [8.2.4交叉验证](#824----)
      - [8.2.5回到MyStery Data Demo](#825--mystery-data-demo)
      - [8.2.6小总结](#826---)
  * [9.机器学习导论](#9------)
    + [9.1机器学习基础知识](#91--------)
      - [9.1.1机器学习概念](#911------)
      - [9.1.2机器学习常识](#912------)
      - [9.1.3机器学习方法](#913------)
    + [9.2特征工程](#92----)
    + [9.3距离度量](#93----)
    + [9.4监督和无监督学习](#94--------)
    + [9.5性能度量](#95----)
  * [10.聚类问题](#10----)
    + [10.1性能度量](#101----)
    + [10.2层次聚类](#102----)
    + [10.3K-Mean](#103k-mean)
      - [10.3.1基本思想](#1031----)
      - [10.3.2K-Mean存在问题](#1032k-mean----)
      - [10.3.3一个Demo](#1033--demo)
  * [11.分类问题](#11----)
    + [11.1NN](#111nn)
    + [11.2KNN](#112knn)
    + [11.2Titanic Demo](#112titanic-demo)
      - [11.2.1性能度量](#1121----)
      - [11.2.2测试方法](#1122----)
      - [11.2.3KNN方案](#1123knn--)
      - [11.2.4逻辑回归方案](#1124------)
        * [11.2.4.1逻辑回归思想](#11241------)
        * [11.2.4.2分析模型权重](#11242------)
        * [11.2.4.3修改参数P](#11243----p)
        * [11.2.4.4一些困惑](#11244----)
  * [12.统计需要注意问题](#12--------)
    + [12.1Statistical Measure Don't tell the whole story](#121statistical-measure-don-t-tell-the-whole-story)
    + [12.2Pictures can be deceiving](#122pictures-can-be-deceiving)
    + [12.3Garbage In Garbage Out](#123garbage-in-garbage-out)
    + [12.4Sampling Bias](#124sampling-bias)
    + [12.5Beware of Extrapolation](#125beware-of-extrapolation)
    + [12.6The Texas Sharpshooter Fallacy](#126the-texas-sharpshooter-fallacy)
    + [12.7Context Matters](#127context-matters)
- [Summary](#summary)
- [Pset](#pset)
  * [Pset1](#pset1)
    + [1.运输母牛](#1----)
    + [2.挑选金蛋](#2----)
  * [Pset2](#pset2)
  * [Pset3](#pset3)
  * [Pset4](#pset4)
  * [Pset5](#pset5)
- [Reference](#reference)

<br>

# Notes

## 1.贪心算法和背包问题

### 1.1最优化模型

&emsp;&emsp;最优化模型是针对特定的最优解问题构建的一个模型，该模型具有两个特点：

1. 最优化模型有一个函数，该函数能根据问题求出最优解。

   > 比如该模型能求出从Boston 到 New York 最短时间

2. 最优化模型通常受到一定的限制。

   > 比如从Boston 到 New York的花费不能超过100美元;必须在下午5:00前到达New York

<br>

&emsp;&emsp;毕竟最优化模型是针对特定的问题而构建的，它只是一个理论概念，并不是一个特定的方法，所以为了了解如何构建最优化模型，我们可以先从经典的背包问题入手。

<br>

### 1.2背包问题

&emsp;&emsp;背包问题是常见的求最优解问题，它的基本描述是：**如何在有限的背包承重下，装下更高价值的物品**。背包问题具有很多变种，其中两个是：

1. 连续性或部分背包问题

   > 这类问题比较简单，假设物品的重量叫做 w，价值叫做v。因为可以装载部分，那么按照v/w 从高到底依次装下物品即可。这类背包问题总是能通过贪心算法找到最优解。

2. 0/1背包

   > 这类问题是说物品要么不装，要么装，问怎样才能在有限的背包承重下，装下更高价值的物品。

<br>

&emsp;&emsp;从理论上讲，0/1背包问题是一个天然的指数型问题，因为针对若干物品，它们只有选择和不选择的情况，那么总的来说就有2<sup>n</sup>种可能性。即使可以通过背包承重限制删除掉一些可能性，在worst_case的情况下(比如刚好就有一两件物品放不下)，它的时间复杂度仍然是O(2<sup>n</sup>)。所以如果想通过暴力求解，计算出每种可能性的total_value，然后比较出最好的best_total_value几乎是不可能的。

&emsp;&emsp;那么0/1背包问题就无解了吗？并不是。因为我们在实际生活中都有自己的预算，即可承受解，并不一定要求是最优解。所以0/1背包问题可以通过贪心算法来解决，不过在介绍如何通过贪心算法来解决0/1背包问题之前，要先看看Lambda表达式（当然也可以跳过，在贪心算法中涉及到了一个sorted函数，所以可能需要看看Lambda表达式）。

<br>

### 1.3Lambda表达式

&emsp;&emsp;在讲Lambda函数之前，需要讲一下python内置的函数`map(function,argument2,....argumentn)`。该函数能返回一个map的数据结构，但是这并不重要，重要的是map函数能通过function实现映射，产生新的对象，然后可以通过循环遍历map来对这些对象进行访问。

&emsp;&emsp;这里要注意的是，argument2....argumentn都是具有相同长度的有序的集合；而function的形式参数个数和argument2...argumentn的个数是相同的。map做的事是每次分别从.argument2...argumentn取出一个对象作为function的参数，从而产生一个新的对象并存储到map里面。

案例如下:

```python
if __name__ == '__main__':
    list1 = [3, -6, 2]
    list2 = [2, 4, 7]

    # abs
    temp_list = []
    for elt in map(abs, list1):
        temp_list.append(elt)
    assert temp_list == [3, 6, 2]
    print(temp_list)

    # max
    temp_list = []
    for elt in map(max, list1, list2):
        temp_list.append(elt)
    assert temp_list == [3, 4, 7]
    print(temp_list)
```

结果是

>[3,6,2]
>
>[3,5,7]

<br>

&emsp;&emsp;而Lambda表达式是干什么的呢？它的作用就是构建一个匿名函数，具体用法是`lambda <sequence of variable names>: <expression>`。简单来说，该匿名函数的形式参数是`<sequence of variable names>`,函数体返回值是`<expression>`。

案例如下：

```python
if __name__ == '__main__':
    list1 = [3, -6, 2]
    list2 = [2, 4, 7]
    # lambda  power
    temp_list = []
    for elt in map(lambda x, y: x ** y, list1, list2):
        temp_list.append(elt)
    assert temp_list == [9, 1296, 128]
    print(temp_list)
```

结果是:

> [9, 1296, 128]

<br>

### 1.4贪心算法

&emsp;&emsp;贪心算法的基本思想是在每一步都做出在当时看来最好的抉择，以期望在所有步骤结束后能收取一个不错的结果。就0/1背包问题而言，所谓的每一步做出当时最好的抉择指的是在背包剩余容量支持的情况下，选择物品value最大的，或是value/weight最大的，或是weight最小的。这样的结果会根据你自己对于最好的定义采取的不同策略而不同。不过这些方法并不一定能保证最优解，因为就0/1背包而言，贪心算法只是1种可能性的结果，并不一定是所有的2<sup>n</sup>中可能性最好的。

![0/1背包问题直观解释](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210317105955119.png)

&emsp;&emsp;上面的图是对贪心算法的直观解释。在谷底的时候，根据某种贪心算法达到了A点，然而事实上还可能存在更高的点，即B点。

<br>

&emsp;&emsp;虽然说贪心算法不一定能保证最优解，但是仍然采用它的原因是：

1. 时间复杂度为O(nlogn),运行速度快。
2. 只要贪心算法的解是可承受解即可，并不一定要求是最优解。

<br>

具体的代码如下所示:

```python
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
```

<br><br>

## 2.动态规划

### 2.1动态规划性质

&emsp;&emsp;动态规划可以解决具有以下2种性质的问题：

1. 最优子结构

   > 即通过处理子问题的最优解可以获得父问题的最优解。

2. 重叠子问题

   > 相同的子问题不止出现一次

&emsp;&emsp;大多数的最优解问题具有上述两种性质，所以动态规划经常解决最优解问题。具体关于怎么利用动态规划去解决实际问题，可以参考下面几节的案例。

<br>

### 2.2斐波拉契数列案例

&emsp;&emsp;之所以可以用动态规划来解决斐波拉契数列的原因是:

1. 满足最优子结构性质:

   > fib(n) = fib(n-1) + fib(n-2)，明显子问题的最优解可以获得父问题的最优解

2. 满足重叠子问题性质:

   > 这个也很明显，求解fib(x)的过程中，很多重复问题被多次计算了

![image-20210317182622442](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210317182622442.png)

&emsp;&emsp;解决它们的问题就是记忆化，也就是将子问题的结果用类似于字典的数据结构存储起来，这样做的目的可以省去很多解决重复问题的时间。

&emsp;&emsp;而归并排序能不能用动态规划解决呢？答案是不能。归并排序具有最优子结构的性质，但是不就重叠子问题的性质。这个很好想，归并排序中会对两个子list进行排序后，再归并，显然这个是最优子结构的体现；但是，处理的子list不能保证他们是相同的，所以不能用动态规划来解决归并排序。

<br>

### 2.3动态规划解决0/1背包问题

&emsp;&emsp;理论上讲，0/1背包问题是天然的指数型问题，不管是什么算法在针对指数型问题上应该是没有办法的。但是，实际上由于物品呈现的某些性质，采用动态规划却是解决0/1背包问题可行的方案。既然是可行的方案，那么0/1背包问题的必须要有两个性质，即最优子结构和重叠子问题的性质。在分析这两个性质之前，需要补充一些预备知识:

**1.二叉树**

&emsp;&emsp;二叉树是无环的有向图,除此外，还满足如下性质:

1. 只有一个根节点
2. 任意节点最多有两个子节点
3. 任意节点（除了根节点以外）只有一个父亲节点

<br>

当节点a没有子节点，那么称节点a为叶子节点。

<br>

**2.决策树**

&emsp;&emsp;决策树也是无环的有向图，它和二叉树的唯一区别就是，决策树的任意节点的子节点可以是多个，这个具体是多少根据实际问题决定。

<br>

在解决0/1背包问题之前，给一个4元组下一个定义`<items_to_be_taken,items_to_consider,total_value_of_items_to_be_taken,remain_sapce>`,即

- 将要取走的物品列表
- 考虑是否取走的物品列表
- 将要取走的物品列表的总价值
- 背包剩余空间

&emsp;&emsp;严格来说，上面的4元组中，将要取走的物品列表的总价值不是必须的，因为这可以通过将要取走的物品列表计算出，背包剩余空间也不是必须的，因为可以通过背包总空间和将要取走的物品列表计算得出，但是保留它们的原因是方便分析。

<br>

&emsp;&emsp;使用动态规划解决0/1背包问题的过程就是按照左优先，深度优先的顺序构建一个节点是由上述的四元组表示的二叉树（在这里也就是决策树）的过程。所有的叶子节点即为可能的最优解。

&emsp;&emsp;现在我们开始正式分析，为什么在实际意义上可以用动态规划解决0/1背包问题。

首先，0/1背包具有最优子结构的性质:

![image-20210317203209531](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210317203209531.png)

1的局面下能带来的最大价值，必然是2和3所能带来价值中最大的那一个。

但是我们并没有发现重叠子问题性质，毕竟没有一个相同的节点，所以我们被迫像下面这样写代码

```python
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


def build_many_items(item_num, max_value, max_weight):
    items = []
    for i in range(1, item_num + 1):
        items.append(Item(str(i), random.randint(1, max_value), random.randint(1, max_weight)))
    return items


if __name__ == '__main__':
    # ##############################当item的数量较小时 ###################
    names = ['a', 'b', 'c', 'd']
    values = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    item_list = build_item_list(names, values, weights)

    knapsack_weight = 5
    best_value, items_to_be_taken = max_val(item_list, knapsack_weight)
    print("best value -->" + str(best_value))
    for elt in items_to_be_taken:
        print(elt)
    # ##############################当item的数量较小时 ###################

    # ###########################当item的数量较大时 ####################
    # item_list = build_many_items(25, 10, 10)
    # knapsack_weight = 50
    # best_value, items_to_be_taken = max_val(item_list, knapsack_weight)
    # print(best_value)
    # for elt in items_to_be_taken:
    #     print(elt)
    # ###########################当item的数量较大时 ####################

```

&emsp;&emsp;虽然有`if to_consider_items[0].get_weight() > avail:`这行代码为我们裁减掉一些探索，但是最坏情况下，算法复杂度仍为O（2<sup>n</sup>)。

事实上，这正是用动态规划解决0/1问题比较有趣的地方，如果我们拿一个明显的情况来分析：

![image-20210317204052306](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210317204052306.png)

&emsp;&emsp;如果物品有重复的情况（比如有两瓶啤酒），那么根据选择会出现上面划红线的情况，显然它们是同种情况，因为它们的背包剩余容量一样，可选物品一样。而现实生活中，可能会存在很多这种物品重复的情况，而根据不同的决策导致产生了重复的子问题。当然，即使物品不同，也存在重复子问题的情况。为什么这样？这就要思考我们的重复子问题指的是什么，事实上，我们的重复子问题指的是**在剩余容量相同下，可考虑的物品相同的情况下，所能产生的最大价值**，也就是说已经选择的物品和已经产生的价值反倒是我们不关心的。那我们重新看一下之前的那张图:

![image-20210317205450940](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210317205450940.png)

你会发现其实存在很多相同相同的子问题情况。

&emsp;&emsp;理论上，假如物品的 \<value , weight\>都是独一无二的话，那么0/1背包问题确实是指数型问题。但实际上，这种所有物品的 \<value , weight\>都是独一无二的情况不常见。实际情况的0/1背包问题的时间复杂度是伪多项式算法复杂度，至于什么是伪多项式算法复杂度，这里不值得深究，只知道它比指数型复杂度好得多就好了。

&emsp;&emsp;接下来的问题是我们怎么改造代码呢？具体来说，我们怎么构建字典存储已有解。根据书本上所提示的，KV对中的V肯定是在to_consider下的best_value和将带走的物品构成的二元组；而K是也是一个二元组，第一个元素是可考虑物品列表的长度，第二个元素是背包的剩余空间。之所以第一个是采用列表的长度，而不是列表的原因是，你想一想，第一层考虑的是n个东西，第二层考虑的是剩下的n-1个东西，第三层考虑的是剩下的n-2个东西。也就是说，我们用列表的长度就行了，不必用列表。

&emsp;&emsp;修改后的代码如下:

```python
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
    item_list = build_many_items(25, 3, 10)
    knapsack_weight = 50
    best_value, items_to_be_taken = max_val(item_list, knapsack_weight)
    print(best_value)
    for elt in items_to_be_taken:
        print(elt)
    print("#########################华丽分割线################################")
    best_value, items_to_be_taken = max_val_with_memo(item_list, knapsack_weight)
    print(best_value)
    for elt in items_to_be_taken:
        print(elt)
```

这里注意一点，请看`max_val_with_memo`函数里面提到的注意点。

另外就是我观察到一种现象，当物品很多的时候，如果价值区间很小，计算更快。

<br>

![image-20210317224926344](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210317224926344.png)

这个图可以理解为暴力解法的0/1背包和动态规划的0/1背包的效率差别。

<br><br>

## 3.图论基础和最短路径问题

### 3.1图论基础

&emsp;&emsp;这个部分并不会涉及到什么高深的概念，只是简单地引入图和树的概念。

![image-20210322152208677](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322152208677.png)

&emsp;&emsp;所谓图，其实是由一系列节点和边(边两端各含一个节点)组成的一种数据结构。节点和边都可以拥有自己的属性，具体有什么样的属性都是由实际问题抽象得来的。

&emsp;&emsp;最常见的图可以分为无向图，有向图，加权图。

- 无向图

  > 这类图的特征是边没有方向，常见的比如现实社会中的好友关系。

- 有向图

  > 这类图的特征是边没有方向，常见的比如现实社会中的公路网(有方向之分)。如果是有一条边方向是从A到B。那么称A是相对于B的源节点或父节点，B是相对于A的目标节点或子节点。

- 加权图

  > 这类图的特征是边有权重，常见的比如现实社会中的公路网(从A到B路线可能有很多条，但是距离不同，价格不同)

<br>

&emsp;&emsp;**树是一种特殊的有向图**，任意两个节点之间有且仅有一条路径。(PS:这里无需纠结是不是有向，因为有一门课叫做图论，会详细介绍概念，但这里无需深究)

![image-20210322153741531](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322153741531.png)

<br>

&emsp;&emsp;图之所以重要是因为现实中的很多问题都可以抽象成图论的问题，这些常见的问题如下：

![image-20210322155645763](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322155645763.png)

即连通问题，最短路径问题，图形划分问题，最小切和最大流问题。当然，这里有个印象就好了。

<br>

图论最早报道的问题是七桥问题，即是否能在只走每条边一次的情况下走完所有边。

![image-20210322160143416](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322160143416.png)

&emsp;&emsp;这个问题最终由欧拉解决，它的解决方法是**除了初始和结束节点，途中任意节点相关联的边的个数必须是偶数个**。而七桥问题中每个节点的相关联的边的个数都是奇数个，那么显然是不能在不重复的情况下走完所有边的。

<br>

### 3.2最短路径问题

&emsp;&emsp;所谓最短路径问题，指的是找到从节点A到节点B的最短路径。这个最短的意思需要根据实际情况来看，如果是无权图，那么通常指的是边数最少；如果是加权图，那么指的是权的累积最少。

#### 3.2.1构建图模型

&emsp;&emsp;解决最短路径问题之前，需要将上述提到的节点，边，图等数据结构具体落实到代码上来。

**节点和边的表示**

```python
class Node(object):
    def __init__(self, name):
        """
        :param name: string
        """
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """
        :param src: 源节点  Node
        :param dest: 目标节点 Node

        """
        self.src = src
        self.dest = dest

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + "->" + self.dest.get_name()

```

<br>

图的常用表达方式有两种，一种是邻接矩阵，一种是邻接列表。

&emsp;&emsp;邻接矩阵的表示可以用一个词典来表示，key可以用一个二元组(from,to)来表示，from代表源节点，to表示目标节点。具体的value根据实际情况来判断，如果是无权图，那么可以用布尔值来表示通断情况；如果是加权图，那么可以用整型值来表示权重(0表示不连通)。这种表示法大概如下:

![image-20210322162241626](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322162241626.png)

&emsp;&emsp;但是这种表示的问题就是，当边比较少的时候，很多位置是空着的，也就造成了浪费。所以下面关于图的构建采用的是另外一种方式，即邻接列表。

<br>

**图的表示**

```python
class DiGraph(object):
    def __init__(self):
        """
        nodes  即为DiGraph的 节点
        edges  即为Digraph的 边 。key 为 Node, value为 Node 的子节点集合（list)
        """
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate Node")
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_src()
        dest = edge.get_dest()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("node not in graph")
        else:
            self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        to_printed_string = ""
        for src in self.edges:
            for dest in self.edges[src]:
                to_printed_string += src.get_name() + "->" + dest.get_name() + "\n"
        return to_printed_string[:-1]  # 忽略最后一个换行符,其实无所谓


class Graph(DiGraph):
    def add_edge(self, edge):
        DiGraph.add_edge(self, edge)
        one = edge.get_src()
        another = edge.get_dest()
        DiGraph.add_edge(self, Edge(another, one))
```

&emsp;&emsp;上面需要注意到一个细节是**Graph是DiGraph的子类**，Graph和DiGraph的区别是，前者在加一条边的时候，实际加的是双边。

&emsp;&emsp;这样做的目的是代码简洁，易于扩展。根据LSP(里氏代换原则)，在客户端工作正常的父类对象替换成子类对象应该也正常工作。如果将Graph当做DiGraph的父类。假设我们给Graph新添了一条边，即AB，那么节点A和节点B互为父节点和子节点，那么调用graph 调用 `children_of(B)`是不会出现问题的。但是如果digraph调用`children_of(B)`就会出问题。所以只能是Graph是DiGraph的子类。

<br>

#### 3.2.2深度优先搜索

&emsp;&emsp;对于最短路径的解决方案，常常采用深度优先搜索。当然采用广度优先搜索也可以解决无权图的最短路径问题，这个后面会谈到。

&emsp;&emsp;在讲述深度优先搜索之前，先介绍一个辅助函数，它的作用是打印路径。

```python
def print_path(path):
    """
    :param path: path 是 一个list,元素均为node
    """
    result = ""
    for index in range(len(path)):
        result += path[index].get_name()
        if index != len(path) - 1:
            result += "->"
    return result

```

比如

```python
name_list = ["0", '1', '2', '3', '4', '5']
node_list = []
for name in name_list:
    node = Node(name)
    node_list.append(node)
```

的效果是

> 0->1->2->3->4->5

<br>

&emsp;&emsp;深度优先的基本思路是对根节点(即开始节点）按照左优先和深度优先的方式进行递归搜索，那么一次搜索的结果是要么是找到目标节点，要么是找到叶子节点。如果是找到目标节点，那么需要判断当前探索路径是否优于已经找到的最短路径，然后根据实际情况更新最短路径，并回溯到上一层继续递归搜索；如果是找到叶子节点，那么回溯到上一层继续递归搜索。

&emsp;&emsp;这里需要注意到两个问题，第一是需要避免环搜索，方法是判定下一个搜索节点是否在已搜索路径里面，这么做的原因是避免无意义的搜索。第二是判断当前搜索路径的长度是否已经超过目前已经查验的最短路径的长度，如果超过，那么就没有必要继续此次探索，应该回溯到上一层继续递归搜索其他子节点。

具体代码如下所示:

```python
def dfs(digraph, start, end, path, shortest_path, to_print=False):
    """
    针对最短路径的深度优先算法(递归方式)
    :param digraph: 整个有向图
    :param start: 此次递归探索的起始节点(和整个有向图的起始探索节点不是一个概念)
    :param end: 探索的目标节点
    :param path: 已经探索的路径 ,类型为list，存储元素类型为node。
    :param shortest_path: 目前已知的最短路径，类型为list,存储元素类型为node
    :param to_print: 是否打印探索足迹
    :return: 整个图的起始节点到目标节点的最短路径，类型为list,存储元素类型为node

    注意 已经探索的路径path 和 目前已知的最短路径的起始节点 是整个图的起始节点
                    和start不是一样的。

    这里还需要注意到如下几点：
        1.是避免探寻path已经有的点,也就是避免死循环
        2.是会判定shortest_path是不是None或 目前探索的path是不是小于 shortest_path。
           这个的目的判断是否有继续探索的必要。

           假设start节点不是end节点
           那么该算法会针对start节点的所有子节点进行判断。
              1.如果子节点已经在path里面，为了避免探索环，显然不能对它调用dfs
              2.如果子节点不在path里面，那么判断有没有探索的必要。如果shortest_path为None,那么还没找到shortest_path，
                那么就需要探索，也就是调用dfs;如果shorest_path 不为None,说明存在至少在当时来说的最短的shortest_path。
                那么需要判断现在的path的长度是不是小于shortest_path的长度,显然如果大,那就没有必要探索了。
                如果有必要探索,那么按照深度优先，最终碰到的情况要么是碰到了目标节点，要么是碰到了叶子节点。
                碰到目标节点的那条path必然是当前最短的shortest_path(或之一，比如a ->b->d;a->c->d）
                碰到叶子节点的那个，返会的肯定是传入的shortest_path。
                那么上层如何判断返回的shortest_path是否是目标呢?  只需要判断dfs返回的结果和上一个是否一样即可
                如果是一样的,那么不更新shortest_path,如果不是,那就更新。
                或者说,直接将shortest_path  = dfs(xxxx)  也行,懒得判断。
              3.这里说明我的下面注释掉的
                # tmp_shortest_path = dfs(digraph, node, end, path, shortest_path, to_print)
                # if tmp_shortest_path is not None:  # tmp_shortest_path 为None,说明没有找到目标节点。
                #     shortest_path = tmp_shortest_path
                其实本质上
                 shortest_path = dfs(digraph, node, end, path, shortest_path, to_print)
                 没区别。


    """
    path = path + [start]

    if to_print:
        print("Current DFS path:", print_path(path))

    if start == end:
        return path  # 到目标节点的path一定是到目前而言 探索到的最好的shortest_path

    for node in digraph.children_of(start):
        if node not in path:  # 避免探索环 1是没必要,2是避免死循环
            if shortest_path is None or len(path) < len(shortest_path):  # 当且仅当最短路径未探索到或是就目前已探索路径仍有必要探索
                shortest_path = dfs(digraph, node, end, path, shortest_path, to_print)
                # if tmp_shortest_path is not None:  # tmp_shortest_path 为None,说明没有找到目标节点。
                #     shortest_path = tmp_shortest_path

    return shortest_path
```

<br>

#### 3.2.3广度优先搜索

&emsp;&emsp;如果是无权图或者说权重相同的加权图可以采用广度优先搜索来最短路径。其基本思想是按照左优先，广度优先进行搜索，针对起始节点，扫描起所有子节点（并记录路径），判定是不是目标节点，如果不是，那么扫描子节点的所有子节点。如此往复下去，直到找到目标节点。

&emsp;&emsp;之所以可以采用广度优先搜索的原因是，广度优先搜索可理解为权相同的搜索。
也就是在a层到b层,它们的权重是一样的，比的是谁先找到目标节点。如果是带权图,那么bfs是没办法的。

具体代码如下：

```python
def bfs(digraph, start, end, to_print=False):
    """
       广度优先好理解得多,但是广度优先不适合带权搜索，因为广度优先搜索可理解为权相同的搜索。
       也就是在a层到b层,它们的权重是一样的，比的是谁先找到目标节点。如果是带权图,那么bfs是没办法的。
    """
    init_path = [start]
    path_queue = [init_path]  # path_queue  存储所有的路径集合

    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)  # 从path_queue中去除并返回第0个路径
        if to_print:
            print("Current BFS path:", print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path

        for elt in digraph.children_of(last_node):
            if elt not in tmp_path:
                new_path = tmp_path + [elt]
                path_queue.append(new_path)
    return None
```

<br><br>

## 4.随机游走和数据可视化

&emsp;&emsp;这个部分将涉及到Lecture4和Lecture5两课内容。将涉及到两个部分，第一个部分是用BirthdayProblem和RandWalk来讲解预估模型。第二个部分是通过Mortgage问题来引入数据可视化。

### 4.1BirthdayProblem

&emsp;&emsp;这个问题:n人中至少有m人生日相同的概率(m<=n)。

&emsp;&emsp;首先分析这个问题前，我们假定1年是366天，m>=2。那么剩下无非是这么几个情况。

- n\>366,m=2。根据鸽巢原理，概率是100%

- n\<366,m=2。那么根据如下公式可以计算出概率是:

  ![image-20210322192226103](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322192226103.png)

- n\<366,m\>3。这个情况的数学公式就相当麻烦。

<br>

&emsp;&emsp;像上面第三种这种情况，我们或许还能找出繁杂的公式来计算，但是对于一些不能很好用公式来表示的问题，就需要用大量实验来估算。

下面的是至少有两个人有相同生日的代码(部分):

```python
def test_birthday_prob_with_grpah(self):
    num_trial = 10000  # 实验次数
    num_same = 2  # 相等人数为两人
    num_range = [2, 3, 10, 20, 30, 40, 50, 60]
    prob_math = []  # 数学计算的概率
    prob_ex_weight = []  # 实验的加权概率(根据实际情况模拟)
    prob_ex_without_weight = []  # 实验的不加权概率(不考虑实际情况)
    for elt in num_range:
        # 计算公式参考 math_birthday.png
        math_prob = 1 - (math.factorial(366) / ((366 ** elt) * (math.factorial(366 - elt))))
        prob_math.append(math_prob)
        prob_ex_weight.append(birthday_prob_with_different_weight(elt, num_same, num_trial))
        prob_ex_without_weight.append(birthday_prob(elt, num_same, num_trial))

    pylab.title("Probability of Math,Norm,Weighted under"+str(num_trial) + "trials")
    pylab.xlabel("The number of People")
    pylab.ylabel("Probability")
    pylab.plot(num_range, prob_math, label="Probability of Math")
    pylab.plot(num_range, prob_ex_weight, label="Probability of Weighted")
    pylab.plot(num_range, prob_ex_without_weight, label="Probability of Norm")
    pylab.legend(loc="best")
    pylab.show()
```

效果如下:

![image-20210322194610650](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322194610650.png)

&emsp;&emsp;其中绿色和蓝色线基本重合，这说明了一个问题，当实验数目足够大时，**采样概率可以近似等于真实概率**。而黄色线是现实生活中的模拟概率。而黄色线的产生原因是由于下面的一幅图：

![image-20210322195055092](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322195055092.png)

根据这种采样情况，模拟的权重，然后设计的如下代码。

```python
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
```

&emsp;&emsp;其实这也说明了一种问题，就是我们在模拟问题的时候考虑的因素一定要符合实际情况。

<br>

&emsp;&emsp;当人数大于2个人时，数学公式已经不好用了，但是我们仍然可以在实验次数很大的情况下采用预估值。下面的代码将以实际情况为指标（即加权）的模拟当总人数分别为40人，60人，80人时，至少有2--10人生日小能通过的概率。

```python
def test_birthday_prob_with_grpah2(self):
    num_trial = 10000  # 实验次数
    num_same = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    prob_for_40 = []
    prob_for_60 = []
    prob_for_80 = []
    for elt in num_same:
        prob_for_40.append(birthday_prob_with_different_weight(40, elt, num_trial))
        prob_for_60.append(birthday_prob_with_different_weight(60, elt, num_trial))
        prob_for_80.append(birthday_prob_with_different_weight(80, elt, num_trial))

    pylab.title("Probability of 40,60,80 people under " + str(num_trial) + " trials")
    pylab.xlabel("The number of the same birthday")
    pylab.ylabel("Probability")
    pylab.plot(num_same, prob_for_40, label="Probability of 40")
    pylab.plot(num_same, prob_for_60, label="Probability of 60")
    pylab.plot(num_same, prob_for_80, label="Probability of 80")
    pylab.legend(loc="best")
    pylab.show()
```

结果是：

![image-20210322200801897](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322200801897.png)

&emsp;&emsp;这说明5人左右的时候，概率已经相当低了。如果继续测试。假设5人是极限，然后将人数提高到100,200,400。结果如下所示：

![image-20210322203541818](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322203541818.png)

&emsp;&emsp;那么说明5不是人数的极限，随着人数的增长，线出现了抖动剧烈的情况，但是这种抖动是怎样的情况，我就没有继续探讨下去了。

<br>

### 4.2随机游走

&emsp;&emsp;其实从BirthdayProblem，我感受到若干个启示：

1. 当实验次数足够大的时候，采样概率近乎等于实际概率。
2. 真实的概率考虑的情况往往是复杂的。
3. 数据可视化是个好东西。

接下来是分析随机游走问题，来进一步分析问题如何进行预估。

![image-20210322205211195](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322205211195.png)

&emsp;&emsp;简单来说，随机游走问题描述的是一个醉汉以随机的概率往各个方向游走，我们可以根据醉汉的行为预估醉汉的运动轨迹，不同步数下的终止位置，不同步数下距离起始点的距离等等。

&emsp;&emsp;为了表示这个模型，需要引入Drunk，Location，Field几个类。需要注意的是为了程序便于扩展，Drunk是作为基类，封装了`take_steps`方法随机模拟下一步行走方向和距离。Location用于记录方位和计算和另一个方位的距离。Field实现了drunk到location的映射，即用一个词典存储了drunk的位置。

具体的代码如下所示:

```python
import random

"""
这个module(即这个py文件) 主要包含的是random_walk案例的一些实体类
比如 Drunk Location Field

"""


class Drunk(object):
    """
    所有类型Drunk(如Usual)的基类
    """

    def __init__(self, name="Anonymous"):
        """
        :param name: string。 不取名的话。通通叫Anonymous
        """
        self.name = name

    def __str__(self):
        if (type(self)).__name__ == "Drunk":
            raise NotImplementedError("Drunk类不能存在实例对象,请务必子类调用__str__方法")
        else:
            return (type(self)).__name__ + ":" + self.name

    def take_steps(self):
        raise NotImplementedError("Drunk类不能存在实例对象,请务必子类实现take_steps方法")


class UsualDrunk(Drunk):
    def take_steps(self):
        x_step, y_step = random.choice([(1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -1.0)])
        return x_step, y_step


class SouthDrunk(Drunk):
    def take_steps(self):
        """
        x轴上与UsualDrunk相同。但在y轴上,向y负半轴走的距离大于y正半轴的距离。理解为倾向南方
        """
        x_step, y_step = random.choice([(1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -2.0)])
        return x_step, y_step


class OnlyXDrunk(Drunk):
    def take_steps(self):
        """
        只走X轴,不过相比于其他Drunk ，它是2倍的步距
       """
        x_step, y_step = random.choice([(2.0, 0.0), (-2.0, 0.0)])
        return x_step, y_step


class WestDrunk(Drunk):
    def take_steps(self):
        """
        y轴上与UsualDrunk相同。但在x轴上,向x负半轴走的距离大于x正半轴的距离。理解为倾向西方
       """
        x_step, y_step = random.choice([(1.0, 0.0), (-2.0, 0.0), (0.0, 1.0), (0.0, -1.0)])
        return x_step, y_step


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from(self, other):
        """
        :param other: Location
        :return: self  和 other 之间的距离
        """
        return ((self.x - other.get_x()) ** 2 + (self.y - other.get_y()) ** 2) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Field(object):
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, location):
        """
        :param location:  Location 实例
        :param drunk: Drunk的实例
        """
        if drunk in self.drunks:
            raise ValueError("Duplicate Drunk")
        else:
            self.drunks[drunk] = location

    def get_location(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("drunk not in field")
        else:
            return self.drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("drunk not in field")
        else:
            delta_x, delta_y = drunk.take_steps()
            current_loc = self.drunks[drunk]
            new_loc = current_loc.move(delta_x, delta_y)
            self.drunks[drunk] = new_loc
```

<br>

&emsp;&emsp;剩下的其实就是根据实际问题，来设计代码了。比如判断不同drunk在1000次实验下，第1步到1000步的距离原点的平均距离。

![image-20210322210430542](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322210430542.png)

&emsp;&emsp;又比如设计100次实验中，不同drunk在第100步的终点位置等。

![image-20210322210718181](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322210718181.png)

&emsp;&emsp;当然，还有设计drunk在一次实验中的运动足迹等等。

![image-20210322211140926](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322211140926.png)

&emsp;&emsp;这部分具体问题具体设计就行，课本中还提到了一种另外类型Field。我理解为传送门。看代码就好了，挺好理解的。

```python
class OddField(Field):
    """
      模拟传送门
    """

    def __init__(self, num_holes, x_range, y_range):
        """
        :param num_holes: 坑位的个数(传送门的个数)
        :param x_range:  x的范围
        :param y_range: y的范围
        """
        Field.__init__(self)
        self.worm_holes = {}
        for i in range(num_holes):
            from_x = random.randint(-x_range, x_range)
            from_y = random.randint(-y_range, y_range)
            to_x = random.randint(-x_range, x_range)
            to_y = random.randint(-y_range, y_range)
            self.worm_holes[(from_x, from_y)] = Location(to_x, to_y)

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        loc = self.get_location(drunk)
        loc_x = loc.get_x()
        loc_y = loc.get_y()
        if (loc_x, loc_y) in self.worm_holes:
            self.drunks[drunk] = self.worm_holes[loc_x, loc_y]
```

![image-20210322211910051](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322211910051.png)

<br>

### 4.3数据可视化

&emsp;&emsp;下面的只是部分讲解数据可视化需要了解的知识。

#### 4.3.1关于plot()

&emsp;&emsp;这个函数至少要传入x坐标和y坐标，如果只传入一个坐标，那么将其看作y坐标，x坐标即为range(len(y))。默认情况下，坐标之间用直线相连，这个可以直接调整。具体可以参考官方文档<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot">plot</a>。通常来说有三组可选数据，即`[marker][line][color]`。

<br>

#### 4.3.2关于figure()

&emsp;&emsp;作图都是在一张figure上的，figure()函数的作用是创建并使之为当前的figure。可以传入类型为int，或string的参数，显式创建figure。如果参数已经存在，那么作用就是切换figure。这里需要注意的是，如果没有调用figure函数，那么默认是在同一个figure上作图。

<br>

#### 4.3.3MIT的lecture风格代码

```python
    # set line width
    pylab.rcParams['lines.linewidth'] = 4
    # set font size for titles
    pylab.rcParams['axes.titlesize'] = 20
    # set font size for labels on axes
    pylab.rcParams['axes.labelsize'] = 20
    # set size of numbers on x-axis
    pylab.rcParams['xtick.labelsize'] = 16
    # set size of numbers on y-axis
    pylab.rcParams['ytick.labelsize'] = 16
    # set size of ticks on x-axis
    pylab.rcParams['xtick.major.size'] = 7
    # set size of ticks on y-axis
    pylab.rcParams['ytick.major.size'] = 7
    # set size of markers, e.g., circles representing points
    pylab.rcParams['lines.markersize'] = 10
    # set number of times marker is shown when displaying legend
    pylab.rcParams['legend.numpoints'] = 1
```

<br><br>

## 5.蒙特卡罗模拟

&emsp;&emsp;待补充

## 6.置信区间

&emsp;&emsp;待补充

## 7.采样和标准误差

&emsp;&emsp;待补充

## 8.依据实验数据构建模型

&emsp;&emsp;本节涉及Lecture9&10，Chapter18 Understanding Experimental Data。

### 8.1Spring Demo

#### 8.1.1目标函数

&emsp;&emsp;要求根据实验得到的数据计算出弹簧系数，但是需要注意的是，由于存在测量或观测误差，数据并不是我们想象的那么完美。

&emsp;&emsp;思路分析，假设y=kx+b.(y代表F，x代表位移，k代表弹簧系数，b代表弹簧自重，数据考虑是标量）。现在的问题是，针对不同的两组（k,b)，怎样评判哪一组更好呢？针对这类**线性回归问题**、如果存在一组（k1，b1）使得比其他的（k，b）都使得如下的目标函数：

![image-20210330161132951](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330161132951.png)

更小的话，那么k即为所求。

<br>

#### 8.1.2Polyfit & Polyval

&emsp;&emsp;按照之前的思路，需要尝试很多的（k，b），但是Pylab已经提供了一系列函数帮助我们做这样的事情。

![image-20210330161958213](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330161958213.png)

&emsp;&emsp;Polyfit传入的参数是实验得到的所有自变量X和因变量Y，以及多项式的次数；而它返回的是一个元组，代表当平方差求和最小时，多项式的各个项的系数。我们在求弹簧系数时，显然n=1。

<br>

Pylab也提供了求预估值的函数，![image-20210330162524547](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330162524547.png)

即polyval函数，该函数传入polyfit的返回结果（即训练好的模型）和自变量，即得到预估的因变量Y。

<br>

如果我们把实验数据和预估数据绘制在图上，那么将是类似于下面的结果。

![image-20210330162917643](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330162917643.png)

<br>

#### 8.1.3考虑实际情况

&emsp;&emsp;从上面的观察来看，好像k=21.5369就是目标所求，但实际情况不是这样。因为正如标题所示，要考虑**实际情况**。这里的实际情况是指**胡克定律必须在弹簧限度以内才成立**，也就是说，图中的一些实验数据，并不是合理的，这些点应该剔除掉。在删除掉这些点以后，我们得到的图如下所示：

![image-20210330163645775](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330163645775.png)

也就是说真正的弹簧系数k=15.6437。

<br>

&emsp;&emsp;现在的问题是，如果我们得到一组数据，而假设它是多项式类型的，但是我们并不知道它的次数到底是多少，那么该怎么办呢？这就要引入下面的Mystery Data Demo

<br>

### 8.2Mystery Data Demo

#### 8.2.1Mystery Data 来源

&emsp;&emsp;Mystery Data来源是2次函数，并人为在上面增加了干扰（添加高斯项）。

![image-20210330170028979](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330170028979.png)

&emsp;&emsp;1即是加的干扰，这个模拟的实际情况的测量或是观察误差。2即是该多项式是3x^2,并产生20组数据。**当然，实际情况下，我们不可能知道答案**。这里强调这一点的原因仅仅是站在上帝视角，为了和后面的结果作比较而已。

<br>

#### 8.2.2如何看待模型好坏

&emsp;&emsp;通过Polyfit我们可以得到针对不同多项式次数下，最好的model。不同维度的model之间，可以以平方差求和来比较。即：

![image-20210330170849104](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330170849104.png)

<br>

而单看一个model，如何判定它好不好，可以用决定系数来看(当然也可以看不同model的好坏）:

![image-20210330171008168](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330171008168.png)

<br>

当然，如果是多项式数据，R2的范围通常是在0到1之间，1表示模型好，0表示模型好。

![image-20210330171117545](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330171117545.png)

<br>

&emsp;&emsp;之所以用R2而不是平方差求和，是因为不能单从平方差求和看出model是好还是不好，这与数据的量级是有关的。比如看下面这组数据

![image-20210330171855264](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330171855264.png)

&emsp;&emsp;光看决定系数，可以看出多项式次数16是好的，因为接近1；但是看平方误差，它貌似是很大的，不好的，也就是看不出来是好还是不好。

&emsp;&emsp;这里补充一句：在我做了Pset5之后，我发现R2只能评估模型基于训练集的好坏，并不能用它测试集测试模型性能好坏的指标。但是平均平方差求和或是平均平方差求和再开根是可以的。

<br>

#### 8.2.3过拟合问题&为何构建模型

&emsp;&emsp;设置多项式次数为（1,2,4,8,16）,我们可以看出多项式次数为1肯定是不行的，但是貌似16才是我们想要的。![image-20210330172315123](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330172315123.png)

&emsp;&emsp;但是我们都知道多项式的次数是2而不是16，那么这里为什么是16呢？事实上，这里指的是**过拟合现象，过拟合指的是模型过好，将噪声都考虑在内**（这里的噪声其实就是各种干扰导致数据的变化，比如我们加的高斯项），而事实上，我们想要的模型是不想要这些噪声的，因为我们构建模型的目标至少是如下两点：

- 分析模型的内在性质（如spring demo）
- 预估新值（如这个demo）

&emsp;&emsp;这样的模型（存在过拟合）在泛化能力上，也就是预估新值上，效果是很差的。Lecture10提供了一个很简单的Demo来分析这个现象：

![image-20210330173513282](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330173513282.png)

&emsp;&emsp;该Demo根据已有数据（3.1存在噪声）得到了次数为2的多项式模型。事实上我们实际的模型是y=x，但是这个二次项模型的决定系数R^2比一次模型更好。那么如果测试新数据x=20，我们就会发现真实值和预估值存在很大差异。

![image-20210330185414645](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330185414645.png)

现在的问题是决定系数难道是错的？

&emsp;&emsp;决定系数并没有错，在测试数据上决定系数好的模型在测试数据上当然是好的，但是在预测数据上，决定系数好的模型却不一定表现出色。**更确切来讲，在训练集决定系数好只是必要条件，而非充分条件**。那么该怎么做呢？

&emsp;&emsp;这里补充一句：关于过拟合，在学习了整个MIT6.0002课程之后，发现至少有四个问题会导致过拟合，第一个就是本身数据就存在noise，这个问题是测量或是观测误差导致的。第二个是数据没有特征缩放，比如age的范围相比一些binary数据的范围大得多，这也会导致过拟合问题，比如第9章的reptile问题：判定短吻鳄是否是爬行动物。第三个是特征的维度相比样本数目的比值比较大时，这类高维度的问题也容易导致过拟合，具体原因貌似是关联特征在这种情况下影响明显。第四个就是信噪比太低，也就是存在大量无用特征会导致过拟合。

<br>

#### 8.2.4交叉验证

&emsp;&emsp;所谓交叉验证的做法大致意思就是将数据分为K份，每次用其中1份做测试集，剩余K-1次做训练集，然后又用另外一份做测试集，剩余K-1次做训练集。然后执行若干次这个过程，通过各种性能判定指标，查看模型到底好不好。交叉验证广泛适用于挑选各种参数。

交叉验证的方法可以细分为：

- 数据少时，采用留一法（即每次只有一个数据用于测试）
- 数据多时。
  - K折法（同交叉验证定义，留一法是K折法特例）
  - 重复随机取样验证（即随机从总体中取若干样本做测试集，剩余做训练集，训练次数自己决定）

&emsp;&emsp;在Lecture10中，研究美国从1960--2015年的温度数据中，采用的就是重复随机取样法，取样10次，一半数据用于训练 ,一半数据用于测试。

实际数据

![image-20210330191617364](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330191617364.png)

最终结果![image-20210330191729589](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330191729589.png)

可以发现平均决定系数最好且最稳定的就是维度为1时的model。

<br>

&emsp;&emsp;现在的问题是为什么用交叉验证？用一些数据测试，剩下数据检验不好吗？答案是，数据存在偶然性。Lecture10给出了单独针对维度为1，即多项式次数为1时，10次用一半数据训练一般数据检验得到的R\^2。![image-20210330192439775](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330192439775.png)

可以看到画红圈的那个数据就会非常低，而如果我们恰巧得到这个结果的话，就会影响我们的实际判断了。

<br>

#### 8.2.5回到MyStery Data Demo

&emsp;&emsp;相比于美国City温度有着40多万数据而言，MyStery Data Demo的数据少得可怜，所以用到的只能是留一法。**但是并不是一开始就用留一法；而且使用留一法时不能用决定系数来当评判指标**。

![image-20210330193013918](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330193013918.png)

因为这一项的结果永远是0.那么在评判不同维度的好坏时，应该**采用平方误差求和**。

这里补充一句

<br>

&emsp;&emsp;具体的做法是，分别选维度1,2,4,8,16来查看**训练**的R\^2,如果训练集都表现得不良好，那么就肯定不是好的model。

![image-20210330193345595](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330193345595.png)

&emsp;&emsp;从结果来看维度为1时，肯定不是好的model。那么接下来，我们先暂时用部分数据进行验证，剩下一部分数据进行测试，查看结果：

![image-20210330194429634](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330194429634.png)

好像16维度并不好，但是因为存在偶然性，单从这样是看不出来结果的，所以采用2折方案，得到下面结果：

![image-20210330194646165](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330194646165.png)![image-20210330194429634](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330194429634.png)

根据这组数据可以初步判定16维度应该的确不太好，既然如此将维度判定在2--15中，继续2折实验。

![image-20210330195211081](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330195211081.png)![image-20210330195220384](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330195220384.png)

进一步排除掉12维度，现在可以针对2维度到11维度采用留一法查看方差求和（当然用2折法查看10维度倒也行）。

![image-20210330195623229](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330195623229.png)

&emsp;&emsp;查看到这个结果到让人感到意外的，好像维度3才是最好的，但事实上，我们知道维度2才是最好的，那么站在上帝的视角上分析为什么出现了这种情况。

&emsp;&emsp;因为我们知道，该实验的数据来源于

![image-20210330170028979](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330170028979.png)

你仔细分析gauss的分布就会发现：

![image-20210330195929934](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330195929934.png)

&emsp;&emsp;大概率来讲，gauss产生的数据波动范围是（-100,100）,而当x在-6到6之间的数据，最大时的绝对值才108。也就是这些noise，压根就不是noise，而是disaster。

&emsp;&emsp;所以我修改了数据，将x的范围变为（-16,6）和（6,16）,并产生新的Dataset3.txt 和Dataset4.txt最后的结果是2维度。

![image-20210330201329923](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210330201329923.png)

接下来用Polyfit来查看当维度是2时的系数，得到的结果是

a=3.0861,b=0.3074,c=-17.6318

这个结果不算差了，至少2次项系数和1次项系数都非常接近了。

<br>

#### 8.2.6小总结

&emsp;&emsp;依据实验数据构建模型，其实首先做的应该是剔除掉不合理的数据，比如不符合胡克定律满足条件的数据和明显干扰过大的数据。但是这些数据的剔除是很难的，比如上面的Mystery Data问题，原先（-5,5）这个区间的noise过大，但是并不容易看出来。

&emsp;&emsp;剩下来的应该是应该先是作一些处理，如通过训练集和仅作一次测试验证去测试指数分布的维度（1,2,4,8,16)将不可能的维度排除掉。

&emsp;&emsp;剩下来根据数据采用重复随机抽样，K折，留一法来对数据进行训练测试，以找到合适的维度。

&emsp;&emsp;当然，这部分只是机器学习的入门中的入门，所有知识有待更新。

&emsp;&emsp;补充一句:这个MyStery Data Demo掺杂了我当时大量的自主测试，所以可能有不对的地方。不过基本思想是：训练集训练模型后，查看模型在训练集上的性能如何，比如R2，如果训练集模型都不好，那就没有进行交叉验证的必要（Train-Test），如果单次模型的训练之后还不错，那么我们就进行交叉验证。也就是说，单次模型验证是试水，单纯评估模型训练得怎么样；交叉验证是看模型的平均泛化能力怎么样。还有就是R2并不能作为测试集上的评估指标（参考Pset5）。

<br><br>

## 9.机器学习导论

### 9.1机器学习基础知识

#### 9.1.1机器学习概念

&emsp;&emsp;机器学习是什么？请看下图。

![image-20210404155014916](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404155014916.png)

&emsp;&emsp;机器学习是通过已知的数据和输出来构建一个模型（即程序）。比如我们知道北京自建国以来的几十年的天气情况（比如温度，湿度，是否下雨等），将这些数据交给机器，让机器给我们构建一个预估天气的模型的过程，就叫机器学习。

<br>

#### 9.1.2机器学习常识

&emsp;&emsp;机器学习涉及到如下概念：

1. 训练集

2. 测试集

3. 监督学习

   >数据有一系列特征（feature）和对应的标签（或称类别）。根据这些数据构建模型后，通过一个新样本的feature，来判断它到底是属于哪一类。

4. 无监督学习

   >数据有一系列特征（feature），但是没有标签。构建模型使这些数据分为若干类。

<br>

该讲提供了关于英格兰足球队的若干不同类型球员的数据，并讨论了监督学习和半监督学习

![image-20210404160621225](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404160621225.png)

&emsp;&emsp;如果是没有标签的话（即不考虑是Receiver还是Linmen），如何将它们自然地分为几类，也就是**聚类问题**。聚类问题很重要的是**怎样判断不同样本之间的相似性**，这个相似性通常是由**距离**来判定。这个在后面会有详细讲述，下面根据**直觉**来进行聚类：

**根据体重**

![image-20210404160948595](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404160948595.png)

**根据身高**

![image-20210404161008370](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404161008370.png)

**根据体重和身高**

![image-20210404161159233](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404161159233.png)

&emsp;&emsp;在已知是两类的情况下，上面是采用不同距离度量方式的模型，而第三种根据体重和身高是最好的模型（假定是这样的吧。）

<br>

&emsp;&emsp;如果是有标签的话，那么就是分类问题，即监督问题。该问题聚焦在如何找分界线，是得分界线两侧是不同的类别。

![image-20210404161844830](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404161844830.png)

<br>

#### 9.1.3机器学习方法

![image-20210404162201299](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404162201299.png)

<br>

### 9.2特征工程

&emsp;&emsp;特征工程的目的是如何从样本中提取有用的特征，提高信噪比（简单理解为有用特征数/无用特征数）。

![image-20210404162532739](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404162532739.png)

&emsp;&emsp;之所以这么做的原因是，无用的特征将干扰模型的训练，对于模型的泛化能力没有一点好处。比如一群人中大部分是12月份生的，而且他们的成绩都比较优秀，现在判定一个6月份的生的人是否成绩优秀，那么机器根据以往经验是这个人大概率是不优秀的，因为它月份是6月份。但是我们都知道这很扯淡，但是机器并不知道。所以特征工程很重要。

&emsp;&emsp;下面是Lecture11提供的一个较为简单的案例，表示特征工程该怎么做。简单来说，是将爬行动物的共有特征逐步提取出来，最后得到了爬行动物应该关注的feature。

**初始：**

![image-20210404163259717](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404163259717.png)

**结束：**

![image-20210404163320417](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404163320417.png)

&emsp;&emsp;当然，这个模型还不太完善，关注的这两个feature是爬虫动物的必要条件，而不是充分条件。也就是说不存在FN情况，因为如果我知道一个动物没有两个特征，那么肯定不是爬行动物，也就是说我不会把一个真的爬行动物判定成不是爬行动物的情况发生。但是存在，FT情况，也就是我错误地将具有这两个特征的非爬行动物错判成了爬行动物，比如上面的Salmon鱼。

<br>

![image-20210404164006219](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404164006219.png)

&emsp;&emsp;当然，特征过程关注的不只是那些特征该选取不选取，还关注样本之间的距离度量方式，和特征的权重配比。这些都要到后面才讲到了。

<br>

### 9.3距离度量

&emsp;&emsp;之前说了，动物之间的相似性可以由动物之间的**距离**来体现。而距离通常由一个闵式距离公式进行刻画，

![image-20210404164119663](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404164119663.png)

&emsp;&emsp;一般地，当参数P为1时，称作绝对距离或曼哈顿距离或街道距离，当参数P为2时，称作欧几里得距离。具体距离该如何选择还是在训练模型做交叉验证时确定的。**当然，多数参数都是在模型进行交叉训练的时候确定的**。

比如下面的是采用不同的距离策略方案（均为二进制特征）

![image-20210404164719674](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404164719674.png)

![image-20210404164730923](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404164730923.png)

&emsp;&emsp;无论从欧几里得还是绝对距离来看，动物之间的相似性都是一样的。但是实际情况是采用不同的距离度量方案可能是不同的。(注意原文还提供了特征未缩放之前的距离，但是我没贴出来，因为跟距离度量无关了)

<br>

### 9.4监督和无监督学习

&emsp;对于无监督学习而言，

![image-20210404171151412](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404171151412.png)

关心的问题是Cluster到底取几，特征到底怎么选，距离度量方案该怎么选。比如：

![image-20210404171240787](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404171240787.png)

&emsp;&emsp;聚两类是不行的，因为那个边界的黑点感觉不大对劲。那么聚的类的次数越大越好吗？也不是，也得考虑过拟合问题。所以聚类的K值选取就是一个问题。

<br>

又比如

![image-20210404171510831](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404171510831.png)

监督问题同样也要考虑是不是过拟合，怎样选择特征等问题。

<br>

### 9.5性能度量

模型怎样才算好？这就需要相关的性能度量手段。比如：

基于混淆矩阵

![image-20210404171828040](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404171828040.png)

的accuracy，sensitivity，specificity，positive predicted values等等。

**accuracy**

![image-20210404171953813](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404171953813.png)

<br>

**positive predicted value**

![image-20210404171934067](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404171934067.png)

<br>

**sensitivity&specificity**

![image-20210404172039051](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404172039051.png)



<br><br>

## 10.聚类问题

### 10.1性能度量

&emsp;&emsp;聚类问题说到底也是个优化问题，那么它优化什么呢？

![image-20210404173703138](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404173703138.png)

&emsp;&emsp;c表示一个cluster，mean(c)表示聚在一个cluster（也就是一类）的平均距离，通常情况下是欧几里得距离。variability（c）表示的是cluster的数据的变化程度，这个值越小代表该cluster的成员距离就越接近，也就意味着它们更加相似。**所谓的优化问题就是 所有的cluster的variability求和尽可能小**。

&emsp;&emsp;但是是个人都能看出，一个样本一个类，那么最小就是0，那还搞啥机器学习？所有通常情况下，都是有限制的。比如：

![image-20210404174237852](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404174237852.png)

&emsp;&emsp;不同cluster之间得有个最小距离限制，如果不同cluster之间的距离小于这个最小限制，那么就需要进行调整。此外，cluster到底取几个也有限制。

那么问题来了，**cluster之间的距离怎么计算？**这里给出了三种度量手段：

![image-20210404174541921](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404174541921.png)

假设ClusterA的点和ClusterB的点的距离为d，那么这些距离从小到大排为{d1，d2，d3,....dn}

&emsp;&emsp;第一个就是说，两个Cluster之间的距离就是d1。第二个是说，两个Cluster之间的距离就是dn，第三个是说两个Cluster之间的距离就是d1到dn的求和平均。至于用哪个，现在不知道，但总是会知道的。

<br>

### 10.2层次聚类

&emsp;&emsp;PPT对该算法的描述已经相当详细了

![image-20210404175116964](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404175116964.png)

&emsp;&emsp;简单来说，选取上面不同Cluster的距离度量方案。最开始n个点各为一个Cluster，然后计算不同之间的最小距离，最小距离的两个划分为一个Cluster。然后继续上述过程。直到化为一个size为N的一个Cluster。

&emsp;&emsp;当不同Cluster的距离度量方案定了之后，这个算法的结果也就定了，你要分几簇，那就在算法划分为几簇的时候停止程序就行了。

比如下面这个Demo，按照Single-Linkage进行聚类的结果是：

![image-20210404175630067](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404175630067.png)

如果你想聚3类，那么答案就是`{BOS,NY,CHI},{DEN},{SF,SEA}`,如果想聚2类，那么答案就是`{BOS,NY,CHI,DEN},{SF,SEA}`。

怎么评价层次聚类呢？

![image-20210404175905555](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404175905555.png)

&emsp;&emsp;这个算法当不同Cluster距离的度量方案定下来之后，就是决定性的。算法复杂度比较大，通常是n\^3，有的度量手段比如Single-Linkage，是n\^2，但使是n\^2还是比较慢。当然，层次聚类适用于当K未知的时候采用的策略方式。当K确定的时候，通常都采用K-Mean算法。

<br>

### 10.3K-Mean

#### 10.3.1基本思想

![image-20210404190156745](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404190156745.png)

&emsp;&emsp;简单来说，假设有n个样本，那么最开始的时候从中选取k个点，被选取的k个点称为聚类中心。然后n个点分别求到这k个聚类中心的距离d，比如点A求它到这K个聚类中心的距离按从小到大排为{d1，d2....dk}，那么点A就要划分到最小距离为d1的那个聚类中心代表的Cluster里面去。

&emsp;&emsp;划分完毕后，对于每个Cluster的所有点，计算其平均位置，这个位置就是新的聚类中心。假设聚类中心的集合是set ={n1，n2，.....nk},如果划分前后划分后的聚类中心集合不变的话（即set_before = set_after)，那么算法终止。

&emsp;&emsp;算法复杂度的分析，单次循环是 k \*n\*d。k代表聚类中心，n代表样本总数，d代表距离计算。而循环次数是不确定的，但通常来说比较小。**总之，是告诉你一件事情这个K-Mean算法要快于层次聚类**。

<br>

#### 10.3.2K-Mean存在问题

&emsp;&emsp;K-Mean算法是存在若干问题的:

1. 初始K个点的选取导致的结果可能是局部最优的。简单来说，K-Mean算法是贪心算法（当然，层次聚类也是贪心算法），它可能找不到最优解。
2. K-Mean算法是建立在K确定的情况下，问题是K不确定呢？貌似K-Mean算法具有一定的局限性。

<br>

&emsp;&emsp;关于第1个问题，解决办法是多次试验，选结果最好的(dissimilarity最小的），当然可能结果仍然不是最优的，但至少增大了概率。这里需要补充的是，1的问题还有种极端情况是结果出现了一个Cluster无点的情况，对于这种情况，一种解决方案就是直接忽略。

&emsp;&emsp;关于第2个问题，

![image-20210404192411335](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404192411335.png)

1. 一些明显的问题，是可以分类的，比如性别，细菌种类。
2. 如果不是明显的，那么尝试不同K，然后做交叉验证，最小的dissimilarty的那个K就是目标K值。或者选取数据集的一部分子集做层次聚类，通过观察层次聚类的结果来分辨到底那个类好。
   - 选取子集的原因是，层次聚类是比较耗时间的算法，而且没有选取整个集合的必要，因为你选整个集合，那么直接做层次聚类就行了。
   - 那么如何根据层次聚类来观察呢？

比如下面这个例子，猜K=2。

![image-20210404193628171](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404193628171.png)

<br>

#### 10.3.3一个Demo

![image-20210404194231580](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404194231580.png)

&emsp;&emsp;这个Demo的样本4个特征，如上所示，而Label是0或1，0表示negative，即阴性，1表示positive，即阳性。当然，这是个聚类问题，Label的作用是用于验证模型的好坏的。最开始基本的思想是聚2类，一类高风险，一类低风险。

关于数据（共250条记录，83人为positive）

![image-20210404194639328](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404194639328.png)

&emsp;&emsp;初始情况K=2，并执行K-Mean算法5次，打印最终两个Cluster中，positive/cluster_num的结果。为了避免样本特征scale导致结果不合理，所以采用了Z-Scale，简单来说就是将所有特征-平均/标准差。这个暂时不用多想，简单来说就是特征的scale过大，可能会导致结果出现偏差。比如Age的范围相比ST Evaluation的变化范围要大得多，这种范围变化可能导致Age的影响大于ST Evaluation。所有需要做Z-Scale。

&emsp;&emsp;K=2之后，得到的结果如下：

![image-20210404195303269](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404195303269.png)

&emsp;&emsp;如果出现这个数据，至少说明我们的K取错了，因为之前数据已经阐明positive的有83例，约占据总人数的1/3。虽然两个Cluster的positive占比差异很大是我们想要的结果，因为这代表这高positive的那些数据中，可以分析出到底那些特征才是positive的主要特征。但是，K=2是不对的，高风险的才有26人，然而高风险的人数是83左右，而26连83的1/3都不到。这里如果不能理解，那从另外一种角度去思考，我们主要是通过某些特征去判定人是否患病，也就是是否positive，如果根据高风险的那些犯病数据去推断人是否患病的话，那么会存在很多FN的情况，也就是错误地将一些本来患病的人判定成没患病的人，你想想如果是传染病暴发，存在这种sensitivity低得过头的情况，那么不出大问题？

&emsp;&emsp;补充一句sensitivity和specificity我真的记不住，sensitivity代表percentage correctly found，specificity代表percentage correctly rejected。

&emsp;&emsp;简而言之，K=2是不对的，所以尝试了其他不同的K，具体结果如下：

![image-20210404201234361](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404201234361.png)

&emsp;&emsp;这个结果说明划分4类和6类可能是合理的，只不过4类中的两类高positive背后下的原因是6类中3类高positive的原因的综合罢了。

事实上，我还在教授的代码基础上查看了5,7,8的占比，比如其中7,8的占比

![image-20210404201914351](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404201914351.png)

&emsp;&emsp;虽然，我不知道怎么解释，但是感觉这个数据就是比较怪，我总感觉出了某些问题。当然，这毕竟是聚类入门，想不通的问题多了去了，暂时就这样吧。

<br><br>

## 11.分类问题

### 11.1NN

&emsp;&emsp;NN代表的含义是Nearest Neighbor。该算法相当好理解，简单来说，就是新的样本计算与所有已知样本（特征和类别均知道）的距离，最小的距离对应的那个样本的label是什么，那么新的样本的label就是什么。

但是NN很容易出现这种情况，

![image-20210404203548783](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404203548783.png)

简单来说，4可以匹配4，但是这个0却匹配了9，偶然性太大。所以提出了KNN。

<br>

### 11.2KNN

&emsp;&emsp;KNN的基本思想也比较简单，简单来说，找到新样本最接近的K个样本,这些样本中那个类别占比大，那么这个新的样本就属于哪类。KNN有它的优点，也有它的缺点，具体如下：

![image-20210404204039693](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404204039693.png)

优点是很简单，缺点是占内存，K不好选。

&emsp;&emsp;最大的问题是K不好选，首先K不可能选很大，毕竟K每提高1，那么算法就要多计算N次距离。其次，如果存在类不平衡的问题，那么K的选取也不可能选得很大，比如K=3，猫有3只，狗有1只，即是你的新样本最接近狗，但是还是会被判成猫。（如果是个二类问题，K通常选做奇数）

&emsp;&emsp;通常情况下，是做交叉验证，比如K折或是重复随机取样。那么不同的K，会得到一个评估结果，选择评估结果最好的那个当做我们的K。

<br>

### 11.2Titanic Demo

#### 11.2.1性能度量

&emsp;&emsp;具体问题，具体分析，永远不要只关注一个性能度量准则。

![image-20210404205420799](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404205420799.png)

&emsp;&emsp;比如，如果我们将所有人都判定为死，所有人都判定为没疾病。那么从准确率来看，貌似还可以，但是我们知道这是不行的，因为accuracy受Class Imbalance的影响。所以，我们还要观察其他性能指标，比如：

![image-20210404205630376](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210404205630376.png)

&emsp;&emsp;如果是传染病防控，我比较关心senstivity，因为我不想有人被误判。但是如果作为患者，我比较关心specificity，如果我被判定negative了，我是不是真的就没问题。

<br>

#### 11.2.2测试方法

&emsp;&emsp;测试方法是我们的老朋友了，他们是留一法和重复随机取样法。留一法适用于样本少的时候使用，重复随机取样适用于样本多的时候使用。当样本足够多的时候，采用留一法，效率将是比较低的。

**留一法**

![image-20210406094022203](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406094022203.png)

&emsp;&emsp;样本的个数有多少， for循环就会执行多少次，每次都是其中1个样本做测试，其他样本用于训练模型。在这里留一法是计算混淆矩阵中的各个类别（如果是二类问题，通常是TP,TN,FP,FN)的个数，然后交给性能度量方法进行模型评估。

<br>

**重复随机取样方法**

![image-20210406094429403](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406094429403.png)

&emsp;&emsp;这里是训练集和测试集的划分，训练集和测试集的划分比通常是80/20。上面代码的意思是按照样本的索引进行80/20划分，然后取对应索引的样本划分到训练集或是测试集，这样的做法，教授说是为了提高效率。

![image-20210406094718040](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406094718040.png)

&emsp;&emsp;这个算法其实也挺好看懂的，唯一和留一法的区别是这里是混淆矩阵都取了平均，因为毕竟中重复取样。但是我个人觉得，如果交给性能度量方法，除不除的意义不大。

<br>

#### 11.2.3KNN方案

&emsp;&emsp;KNN在训练（其实不涉及训练这个概念）及测试模型的基本思想是：假设ex1是来自测试集的样本，那么计算ex1与所有训练集的样本距离，从中挑出K个最近的邻居。这K个最近的邻居中，那个label占比最大，那么ex1就被判定为那个label。然后，对比ex1的实际label和判定label，决定是ex1是（如果是二类问题的话）TP，TN，FP，FN的那个情况。当然，如果是二类问题，K通常取奇数。

<br>

```python
def findKNearest(example, exampleSet, k):
    """

    :param example: Passenger
    :param exampleSet: a set of Passengers
    :param k:

    KNN 算法  返回最近的 K 个 Passenger 和  距离
    """

    # kNearest, distances = [], []
    # # Build lists containing first k examples and their distances
    # for i in range(k):
    #     kNearest.append(exampleSet[i])
    #     distances.append(example.distance(exampleSet[i]))
    # maxDist = max(distances)  # Get maximum distance
    # # Look at examples not yet considered
    # for e in exampleSet[k:]:
    #     dist = example.distance(e)
    #     if dist < maxDist:
    #         # replace farther neighbor by this one
    #         maxIndex = distances.index(maxDist)
    #         kNearest[maxIndex] = e
    #         distances[maxIndex] = dist
    #         maxDist = max(distances)
    # return kNearest, distances

    # 按照最近距离排序的 example_list
    nearest_dist_example = sorted(exampleSet, key=lambda elt: elt.distance(example))
    kNearest = nearest_dist_example[:k]
    distances = [elt.distance(example) for elt in kNearest]
    return kNearest, distances
```

上面的算法是返回在exampleSet距离example最近的K个邻居与距离。

<br>

```python
def KNearestClassify(training, testSet, label, k):
    """Assumes training & testSet lists of examples, k an int
       Predicts whether each example in testSet has label
       Returns number of true positives, false positives,
          true negatives, and false negatives

    观看      numMatch > k // 2:  可以猜出这个分类是个 2分类，因为这是个充分条件，换句话来说，力度比较大了
    下面是交叉验证实验中  的 一次Trial。
    根据  KNN 算法,  如果最近的 K 个 大部分是 Label，那么认为 test_case 的label也是  Label，即上面的参数 label。
    反之，则认为不是Label。
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for testCase in testSet:
        nearest, distances = findKNearest(testCase, training, k)
        # conduct vote
        numMatch = 0
        for i in range(len(nearest)):
            if nearest[i].getLabel() == label:
                numMatch += 1
        if numMatch > k // 2:  # guess label
            if testCase.getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:  # guess not label
            if testCase.getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg
```

&emsp;&emsp;这是判定二类的一个KNN算法，根据每个测试集的样本，会得到距离它最近的K个邻居，如果K个邻居中是label的超过半数，那么就判定为label(这里的label当做是Positive），并看是TP还是NP。如果K个邻居中label的个数达不到半数，那么就会被判定为不是label（即Negative），并查看是TG还是NG。

<br><br>

&emsp;&emsp;当然，你会发现这个方法`KNearestClassify(training, testSet, label, k)`和`method(trainingData, testCase)`参数不同。在这里Professor提供了一个灵活性很好的方案。即：

```python
knn = lambda training, testSet: \
    KNearestClassify(training, testSet,
                     'Survived', 3)
```

这样很好地解决了参数不一致的问题。

<br>

测试代码

```python
numSplits = 10
print('Average of', numSplits,
     '80/20 splits using KNN (k=3)')
truePos, falsePos, trueNeg, falseNeg =\
     randomSplits(examples, knn, numSplits)

print('Average of LOO testing using KNN (k=3)')
truePos, falsePos, trueNeg, falseNeg =\
     leaveOneOut(examples, knn)
```

测试结果

![image-20210406101948793](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406101948793.png)

&emsp;&emsp;从结果来看，区别并不大，感觉过得去。当然至于怎样才算好，教授说通常情况下是70%，但是还是得根据实际情况来选中倾向的指标，比如流行病诊断率，你不想错过positive的病人（即不想存在NG情况），那么作为一个医生，你关注的是sensitivity。当如果你是一个患者，当拿到自己的状况是阴性以后，你希望是specificity是高的。当然，Acc存在Imbalance问题，这个就稍微提及一下，不要忘了。

<br>

#### 11.2.4逻辑回归方案

&emsp;&emsp;逻辑回归方法将比下面的讲述的实际要复杂得多，因为涉及了一定的数学运算，所以教授直接略过了，而在Lecture中也是直接调用的提供好的python库。

<br>

##### 11.2.4.1逻辑回归思想

&emsp;&emsp;逻辑回归的基本思想是会根据以往的样本构建一个模型，该模型会对新的样本进行判定，然后给出每个label的可能概率，哪个label的概率最大，那么新的样本就会判定为哪个label。当然，我们不可能直接用所有以往数据去训练模型，然后直接去预估新的样本，所有逻辑回归模型还是得经过训练和测试，然后投入使用。

&emsp;&emsp;逻辑回归相比KNN而言，它除了能预判新的label以外，还能通过特征中各个变量的权重来预估特征中不同变量对预判的贡献情况。通常情况下，如果是正的，那么更可能倾向于某个label，如果是负的，那么更不可能倾向于某个label。如果权重的占比越大，那么贡献情况越明显。

&emsp;&emsp;![image-20210406104405257](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406104405257.png)

如图所示，fit是训练模型，coef\_是模型训练好的权重，predict\_proba是预估新的样本并返回各个label的占比。

<br>

训练模型

![image-20210406104619280](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406104619280.png)

1和2是同维度的，代表测试集样本的特征label。

应用/测试模型



![image-20210406104810502](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406104810502.png)

&emsp;&emsp;1那里为probs\[i\]\[1\]的第二个设为1的原因是在二分类问题里面，默认将1看做positive，prob通常设置为0.5，当然这里不细讲，关于1和2都会在后面附录和P参数设置里面讲到。

测试代码：

![image-20210406105313899](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406105313899.png)

实验结果：

![image-20210406105349508](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406105349508.png)

逻辑回归的结果和KNN的基本一致。

<br>

##### 11.2.4.2分析模型权重

&emsp;&emsp;在分析模型之前，需要谈及L1逻辑回归和L2逻辑回归，但是在谈这个之前要需要谈及关联特征的问题。关联特征是一个很重要的问题，特别是当样本数和特征的维度（即特征里的变量数）相差不多的时候，很容易造成过拟合问题（比如1000个样本，每个样本的特征维度是100或是1000）。举个例子，比如评估一个房子的造价，那么以往的样本有特征（高度，宽度，长度，面积，地域，....)你可以看到，面积和宽度，长度是存在关联的，这就会造成一些问题（我认为是贡献过大）。

&emsp;&emsp;L1逻辑回归所做的事情就是避免此类关联特征导致过拟合问题的发生，加入有关联特征，它会将其中一个特征的权重降到为0，当然具体怎么做的，我不太清楚。

&emsp;&emsp;L2逻辑回归适用于低维度的特征问题，比如本章的Titantic Demo，采用的就是L2逻辑回归，它做的事是将权重分散到关联的特征上，所以，在看特征的时候，不要只关注于某个特征，而是将关联特征整合起来一起看。

从实验结果来看

![image-20210406112415058](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406112415058.png)

头等舱的人更容易存活，而年龄越大，更不容易存活，男士更不容易存活。

<br>

![image-20210406112811281](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406112811281.png)

如果去掉C1的话，从最后结果来看

![image-20210406112913494](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406112913494.png)

&emsp;&emsp;此时客舱等级之间已经没有关系，从结果来看，坐在二等舱和三等舱相比而言没有一等舱安全。（我这里是存在一个问题的，不清楚为什么可以这样分析）

<br>

##### 11.2.4.3修改参数P

![image-20210406113321609](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406113321609.png)

&emsp;&emsp;这个参数P之前提到过，通常是取0.5的，现在的问题是修改P的含义在哪里。其实这里很好分析，比如能将p设置为0.1，那么更多人容易被判为positive，简单来说，就是你不想错过Survived的人，那么这样的结果是sensitivity会提高，而specificity会降低。如果设为0.9，将是sensitivity降低，specificity提高。事实上，这是一个两者的trade-off，不同的机器学习问题关注的指标不同，那么P的设置就不同。而关于sensitivity和specificity的有一个ROC曲线，如下所示：

代码：

![image-20210406114517405](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406114517405.png)

结果：

![image-20210406113859341](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406113859341.png)

&emsp;&emsp;简单来说，ROC曲线是根据不同的p下的specificity和sensitivity得来。上面红色区域的面积即是AUROC=0.861，这个是用来评估模型在specificity和sensitivity相对于 random classifier的的好坏。显然AUROC的结果应该是0.5到1之间，因为我们的模型至少比随机猜测好，而随机猜测的概率就是0.5，所以AUROC至少是0.5起步，越接近1，代表模型更好，上面的那个黄色区域就代表的是比随机分类做得好的地方。

&emsp;&emsp;上面有两个特殊的点，即左下角和右上角。左下角代表的是sensitivity为0，specificity为1，显然这种情况是P设为1，右上角是specificity为0，sensitivity为1，显然这种情况是P设为0.

<br>

##### 11.2.4.4一些困惑

**1.关于Scale**

&emsp;&emsp;其实不难发现，KNN方案是没有进行特征缩放的，而逻辑回归方案由于是调用的python库，是否特征缩放无从得知。但是应该明确看到，age在KNN上的影响应该是大于座位的，因为前者是float，后者是binary。

<br>

**2关于逻辑回归模型权重**

&emsp;&emsp;我自己的结果是：

![image-20210406115857463](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406115857463.png)

也就是C1+C2+C3等于0，并不是教授的等于1，不知道是不是python库版本更改的结果。

还有就是怎样进行关联特征的分析还是不太清楚。

<br>

**3关于prob\[i\]\[1\]**

&emsp;&emsp;教授的代码是明确了survived是positive，所以是标题那个东西，按照我的想法，代码应该是下面这个

![image-20210406120228311](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406120228311.png)

关于具体的classe\_,等变量的分析见下面两图：

![image-20210406120330445](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406120330445.png)

![image-20210406120346658](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406120346658.png)

<br><br>

## 12.统计需要注意问题

&emsp;&emsp;本章涉及Lecture14&15。并涉及大量PPT内容。

### 12.1Statistical Measure Don't tell the whole story

4组xy

![image-20210406121559998](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406121559998.png)

他们的很多统计结果是一样的

![image-20210406121619835](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406121619835.png)

但是

![image-20210406121635714](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406121635714.png)

统计结果可能是骗人的，画图更加直观。（这让我想到了平均工资的笑话）

<br>

### 12.2Pictures can be deceiving

![image-20210406121749707](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406121749707.png)

貌似女生更优秀，但是：

![image-20210406121811551](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406121811551.png)

注意XY的表示意义和刻度。

<br>

![image-20210406121903957](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406121903957.png)

&emsp;&emsp;当然这里除了y轴没有刻度和label以外，这两组数据是不能比较的。People on welfare的基数本来就比People with a full time job。因为只要有家里有人领补助，那么整个家的人都要算作统计里面。比如一个3口之家，母亲领补助，父亲全职工作，孩子未工作。那么左侧+3，右侧+1。

<br>

### 12.3Garbage In Garbage Out

![image-20210406141355733](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406141355733.png)

对错误的数据进行分析将毫无意义。

<br>

### 12.4Sampling Bias

![image-20210406141944723](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406141944723.png)

&emsp;&emsp;很多结论的应用是基于随机取样的，比如之前的经验法则，CLT等等。如果数据不是随机取样的，那么不要从这些数据中得出“合理”的结论。

&emsp;&emsp;比如幸存者偏差。

![image-20210406142158139](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406142158139.png)

<br>

### 12.5Beware of Extrapolation

![image-20210406143023378](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406143023378.png)

简单来说，断章取义，混淆视听。

<br>

### 12.6The Texas Sharpshooter Fallacy

&emsp;&emsp;简单来说，就是有个故事，一个人往农场的枪开了几枪，然后将弹着点都涂上了油漆，然后给人吹嘘它枪法精准。也就是说，它把事后结果当做事前假设，然后得出完美结论。

这里教授讲述了一个案例，但是我听得不是很懂。所以这里存疑。

<br>

### 12.7Context Matters

![image-20210406150329906](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406150329906.png)

0.02%的枪支用于犯罪，感觉挺小的，但是乘以私有枪支，发现有60万枪击事件......

![image-20210406150450789](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406150450789.png)

猪流感导致超过159人死亡，感觉挺多的，但是与每年的季节性流感导致的36000死亡来说，简直不值得一提。

<br><br>

# Summary

&emsp;&emsp;整个MIT6.0002学习记录2021/3/16到2021/4/6，历时22天，第一周学习5个Lecture，第二周学习3个Lecture，第三周学习7个Lecture。

&emsp;&emsp;整个课程大致分为3个部分，第一个部分是贪心,动规，最短路径，这部分我学习得算不错。第二个部分是随机模型模拟，这部分第4-5Lecture也还不错，但是7-9我就比较头疼了，这个我花了一周的时间，但还是不算懂，究其根本，我数学太差劲了。第三个部分是机器学习入门，感觉还算不错。

&emsp;&emsp;我接下来的安排是在未来的1-2个月做好如下事情：一方面将高等数学复习好，为接下来的算法分析打下基础，此外考虑到我的现象能力训练得比较少，我可能还会学习pylab的画图知识。另一方面，我深感学习一门课容易疲劳，所以我准备同时复习JavaSE和设计模式，复习JavaSE的目的还是为了准备之后的算法。

&emsp;&emsp;计算机的通识课是很有必要的，完成上述任务后，操作系统，计算机网络，计算机组成原理，编译原理，图论等知识还等着我去攻克。当然，这些东西都是很好的，至少当我沉下心来，我才发现Computer Science真是太有趣了。AnyWay，Stay Hungry，Stay Foolish，做一个虔诚的求学者。

<br><br>

# Pset

## Pset1

&emsp;&emsp;Pset1涉及到了两个问题，一个是运输母牛，要求采用暴力搜索和贪心算法解决；一个是运送金蛋，要求采用动态规划来解决。下面我将针对两个问题分别阐述需要注意的问题。

### 1.运输母牛

**问题1 载入数据**

```python
def load_cows(filename):
    file_handle = None
    try:
        file_handle = open(filename, 'r')
        cow_from_name_to_weight_dic = {}  # 假设母牛的name是不存在重复的情况
        for line in file_handle:
            word_list = line.split(",")
            name = word_list[0]
            weight = int(word_list[1])  # "9  " 等转为int会忽略掉空白符,至少我观察出来是这样
            cow_from_name_to_weight_dic[name] = weight
        return cow_from_name_to_weight_dic
    except:
        raise FileNotFoundError(filename + "doesn't exist")
    finally:
        if file_handle is not None:
            file_handle.close()
```

&emsp;&emsp;这个部分没有太大的问题，就是需要主要到它文本的数据：

![image-20210322174651236](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210322174651236.png)

&emsp;&emsp;除了最后一行，其他行都是带有换行符的。所以不能简单地删除掉每行读取到的数据的最后一个字符。解决的方案是可以直接忽略,因为`int("9  ")`这种仍然能得到9。或者调用`strip()`函数去掉每行前后端的空白符。

<br>

**问题2.贪心算法**

&emsp;&emsp;这个贪心算法它贪的是什么呢？它贪的是每趟都将最重的牛装入，由于所有牛的总的重量是一样的，单独针对每一趟而言，总是当下所能装入重量最大的，所有按理说，总的趟数就会更短。

&emsp;&emsp;但是这个问题怪的是它返回的是名字，比较的是重量，所有我将它封装成了一个cow类，并调用了`sorted`函数对这些cow安装重量反向排序。这样问题很快就解决了。

代码如下所示:

```python
"""
封装cow的实体类,有两个属性  name(string) , weight(int)详见下文
"""


class Cow(object):
    def __init__(self, name, weight):
        """
        :param name:  cow的姓名,类型string
        :param weight: cow的重量,类型int(>0)
        """
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.name + "->" + str(self.weight)
    
def greedy_cow_transport(cows, limit=10):
        cow_list = []
    for key in cows:
        temp_cow = Cow(key, cows[key])
        cow_list.append(temp_cow)

    #  我封装了一个类 Cow,有两个属性,即name 和 weight
    #  下面代码的意思是产生cow_list的副本,顺序是按照weight从高到底进行排序。
    #   key是一个函数名,我这里写了一个匿名函数 ,它的形参是entity,对应cow_list中的每个元素(即实参)
    #   sorted会按照这个key的返回的值来进行排序,默认是升序,所以我设置了reverse=True,也就是反序
    new_cow_list = sorted(cow_list, key=lambda entity: entity.get_weight(), reverse=True)

    trip_list = []
    while len(new_cow_list) != 0:
        avail = limit  # 单个trip的剩余容量
        new_trip = []
        tmp_cow_list = new_cow_list[:]
        for elt in new_cow_list:
            if elt.get_weight() <= avail:
                new_trip.append(elt.get_name())
                avail = avail - elt.get_weight()
                tmp_cow_list.remove(elt)

        # 添加新的trip
        trip_list.append(new_trip)
        new_cow_list = tmp_cow_list
    return trip_list
```

<br>

**问题3暴力搜索**

&emsp;&emsp;说实话暴力搜索是最简单的，但是这里有个问题就是他给的`get_partitions()`的案例具有误导性，比如

```python
"""
get_partitions([1,2,3])的结果是
[
[[1, 2, 3]]
[[2, 3], [1]]
[[1, 3], [2]]
[[3], [1, 2]]
[[3], [2], [1]]
]
但实际上,它的产生顺序并不是先1等分，然后2等分，被这个迷惑了.
"""
```

所以你需要将`get_partitions()`的结果按照长度由小到大依次排序，然后再根据这个结果遍历。具体代码如下所示:

```python
def brute_force_cow_transport(cows, limit=10):
    all_cow_name = list(cows.keys())
    for trip_list in sorted(get_partitions(all_cow_name), key=lambda x: len(x)):
        is_trip_list_ok = True  # 标志判定此trip_list是否满足要求
        for trip in trip_list:
            total_weight = 0
            is_trip_ok = True  # 标志判定此trip是否满足要求
            for cow_name in trip:
                total_weight += cows[cow_name]
                if total_weight > limit:
                    is_trip_ok = False
                    break

            if not is_trip_ok:  # 如果此trip不行,那么此trip_list也不行,退出此次循环
                is_trip_list_ok = False
                break
        if is_trip_list_ok:
            return trip_list

    return None  # 如果是None 那么只说明了一个问题 至少有一只Cow的重量超过了limit_size
```

<br>

### 2.挑选金蛋

&emsp;&emsp;金蛋的类别为(1, 5, 10, 25)（单位磅），每个类型数量没有限制，问题是如何在总磅数一定的情况下挑选出最少的金蛋。题目明确说了用DP来做，那么需要用DP的两个性质来分析问题，即最优子结构和重叠子问题。

&emsp;&emsp;最优子结构的性质其实还是比较明显的，就是在做1,5,10,25这是个决策时，挑选出这四种决策后的最小值。而重叠子问题也是存在的，比如下图：

![ps1b](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/ps1b.png)

具体代码如下所示:

```python
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """

    """
      根据提示： 每个pound类型的蛋是无限的。
      问题是提供一种蛋的组合,最好pound数等于或是接近总的weight 并且要满足数量要越少越好。
      这是两个限制条件。但是提示也给了总是有egg为value1的,那么难度小了很多。
      现在是怎样让蛋的数量越少越好。
      
       1.最优子结构
       egg_weights 现在假设是(1, 5, 10, 25)
       dp_make_weight((1, 5, 10, 25),x,memo) , 当x - n >= 0 时(n代表 1,5,10,25）,
       然后在   dp_make_weight((1,5,10,25,x-n,memo) +1 中 挑选最小值。+1的原因是包含本次
       2.重叠子问题
         详见ps1b的图片。
       那么memo记录的key 为 avail(即剩余的容量) ,value  为avail下最小的蛋的数量n。
       
       那么base_case是什么?
       target == 0时,返回0
       现在按照深度优先的思路思考
    """

    if target_weight == 0:
        return 0

    if target_weight in memo:
        return memo[target_weight]

    result = None  # 占位符,没有多大用

    for elt in egg_weights:
        if target_weight - elt >= 0:  # 这样才有继续探索的必要
            tmp_result = dp_make_weight(egg_weights, target_weight - elt, memo) + 1
            if result is None or tmp_result < result:
                result = tmp_result
    memo[target_weight] = result
    return result
```

<br>

## Pset2

&emsp;&emsp;Pset2是最短加权路径问题，此外要求即是户外的行动距离也要在要求范围以内。注意问题如下：

1. 避免添加已访问节点，即注意环的存在。
2. 避免探索没有可能找到最优路径的路径。
3. 找到一条新的通往目标节点路径以后，与当前最优路径比较，根据比较结果，选择是否更新当前最优路径。

<br>

注意点1：

做这种题，最好的方式是**按照深度优先方式，画图分析**。

注意点2：

户外距离是限制条件，在判断时应该是当层节点到下层节点的户外距离 + 目前已知的户外距离**小于等于而不是小于**max_dist_outdoors。不然后面的测试是不会通过的。

核心代码

```python
# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """

    """
    这个和之前Lecture3 分析的最短路径差不多,不过这个是带权的而已。
    注意两个问题,1是start 已经是 访问过的节点,那么应该回溯,避免死循环问题。2是最优化处理,
    判定当前已经探索的路径是否有探索的必要。
    
    假设最开始path = [[],0,0] , best_path = None ,best_dist初始化为max_dist_traversed
    
    """
    # 检验start 和 end 节点是否是digraph的节点(当然我觉得没必要这么做)
    check_valid_node(digraph, start, end)

    # base case
    if start == end:
        return path[0] + [start], path[1]

    # 已经访问节点的name
    visited_node_str_list = path[0]
    if start not in visited_node_str_list:  # 避免访问重复节点
        dist_traversed = path[1]
        dist_outdoors = path[2]
        start_node = Node(start)
        edges = digraph.get_edges_for_node(start_node)
        path[0] = path[0] + [start]  # 更新探索的节点
        for edge in edges:
            # 限制条件 out_door_distance 满足限制 best_dist满足限制(这里的小于等于要注意)
            if edge.get_outdoor_distance() + dist_outdoors <= max_dist_outdoors and \
                    edge.get_total_distance() + dist_traversed <= best_dist:

                new_start = edge.get_destination().get_name()
                tmp_path = path[:]
                tmp_path[1] = tmp_path[1] + edge.get_total_distance()  # 更新dist_traversed
                tmp_path[2] = tmp_path[2] + edge.get_outdoor_distance()  # 更新dist_outdoors
                # cur_path 为 list,存储元素为 string。
                cur_path, cur_dist = get_best_path(digraph, new_start, end, tmp_path, max_dist_outdoors, best_dist,
                                                   best_path)

                if cur_dist < best_dist:
                    best_path = cur_path
                    best_dist = cur_dist

    return best_path, best_dist


# Problem 3c: Implement directed_dfs

def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    best_path, best_dist = get_best_path(digraph, start, end, [[], 0, 0], max_dist_outdoors, max_total_dist, None)
    if best_path is None:
        raise ValueError("Can't find the shortest path")
    return best_path
```

<br>

## Pset3

&emsp;&emsp;该Pset主要是关于比较不同清洁机器人清理地板的效率。机器人分为两种，一种是StandardRobot,一种是FaultyRobot，它们的区别在于随机清理地方的策略不同，后者会偶然出现状况，即暂停清洁。而地板也有分别，即有的地板如果有物体，那么该地板将无需清理。

&emsp;&emsp;整个题的难度是不难的，但是需要注意一些问题。

&emsp;&emsp;题中有个文件叫做ps3_tests_f16.py，这个文件放置了一些测试案例，进行测试就需要提供的test.pyc文件。如果编辑器是PyCharm的话，由于Pycharm默认忽略.pyc文件。所以需要`Setting->Editor->File Types`

![image-20210402115207194](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210402115207194.png)

将pyc文件去除掉。**但是这样做是没有多大用的**。接下来还会报这个问题：

![image-20210402115329938](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210402115329938.png)

&emsp;&emsp;简单来说，我的python解释器版本是3.8.5,而这个pyc的版本是3.5。而pyc文件可以理解为python解释器解释py文件产生的一个中间结果，如果用python3.8版本去执行之前版本的pyc文件就行不通。补充:Pycharm编辑器会在py文件的同级目录创建一个叫做\_pycache\_的文件夹，里面存放了pyc中间结果。从后缀38就可以看出python解释器版本。

![image-20210402120053117](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210402120053117.png)

&emsp;&emsp;所以我用anaconda新创建了一个3.5版本的环境，但是发现PyCharm已经不支持3.5版本了。

![image-20210402115758011](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210402115758011.png)

<br>

&emsp;&emsp;我最终查看了测试案例，发现只需要去除test.pyc相关代码，然后将所有依赖test.pyc创建的对象替换为你自己的代码的创建的对象即可。

比如：

![image-20210402120420872](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210402120420872.png)

<br>

## Pset4

&emsp;&emsp;这道题我有点不太明白一些方法的概率是怎么核算的。比如`is_killed`![image-20210403201429712](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210403201429712.png)

&emsp;&emsp;这个是 ResistantBacteria的is_klled函数。我不太理解为什么不耐药，反而更不容易死。那么问题来了，我既然存在困惑，那为什么还这样写呢？因为我发现只有这样写，才能得到和Pset4的PDF同样的结果。

&emsp;&emsp;当然，这道题消耗我很多时间，我从这道题和之前的Lecture7-9，明显地感受到了我的数学太过薄弱，缺乏直觉和思维能力。但是，我觉得这玩意儿孰能生巧，所以接下来要做的就是好好巩固数学。

&emsp;&emsp;这整道题看下来是不难的，主要是我数学涵养限制了我的解题速度。

<br>

## Pset5

&emsp;&emsp;此题不难，需要注意测试案例`test_moving_avg`是不太对的，因为它传的参数是list，而不是ndarry，所有需要自己修改一下测试案例。

![image-20210406205330031](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406205330031.png)

<br>

![image-20210406205352793](MIT6.0002%20Introduction%20to%20Computational%20Thinking%20and%20Data%20Science%20Notes.assets/image-20210406205352793.png)

<br><br>

# Reference

&emsp;&emsp;本文大量的图片参考自MIT Open Course Ware 6.0002提供的幻灯片以及Professor John V Guttag编著的教材《Introduction to Computation and Programming using Python》。