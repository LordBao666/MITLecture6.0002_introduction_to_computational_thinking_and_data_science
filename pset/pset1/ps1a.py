###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
from entity import *


# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
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


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
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


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

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


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    dic = load_cows("ps1_cow_data.txt")
    print("#####################贪心算法开始##################")
    start = time.time()
    trip_list = greedy_cow_transport(dic)
    end = time.time()
    print("贪心算法用时" + str(end - start) + "s")
    print("贪心算法挑选出的trip:")
    for trip in trip_list:
        print(trip)
    print("#####################贪心算法结束##################")

    print("#####################暴力算法开始##################")
    start = time.time()
    trip_list = brute_force_cow_transport(dic)
    end = time.time()
    print("暴力算法用时" + str(end - start) + "s")
    print("暴力算法挑选出的trip:")
    for trip in trip_list:
        print(trip)
    print("#####################暴力算法结束##################")
