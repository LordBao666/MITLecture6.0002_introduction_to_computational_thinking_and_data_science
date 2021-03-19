"""
@Author  : Lord_Bao
@Date    : 2021/3/19

"""
from ps1a import *
from ps1_partition import *
from unittest import TestCase

"""
下面是ps1a 函数的测试代码

"""


class Test(TestCase):
    def test_load_cows(self):
        # cow_from_name_to_weight_dic = load_cows("ps1_cow_data.txt")
        cow_from_name_to_weight_dic = load_cows("ps1_cow_data_2.txt")
        for key in cow_from_name_to_weight_dic:
            print(key + "->" + str(cow_from_name_to_weight_dic[key]))

    def test_greedy_cow_transport(self):
        cow_from_name_to_weight_dic = load_cows("ps1_cow_data.txt")
        # cow_from_name_to_weight_dic = load_cows("ps1_cow_data_2.txt")
        trip_list = greedy_cow_transport(cow_from_name_to_weight_dic, 10)
        for trip in trip_list:
            print(trip)

    def test_partition(self):

        # for partition in get_partitions([1, 2, 3, 4]):
        #     print(partition)
        cow_from_name_to_weight_dic = load_cows("ps1_cow_data.txt")
        for partition in get_partitions(list(cow_from_name_to_weight_dic.keys())):
            print(partition)

    def test_brute_force_cow_transport(self):
        # cow_from_name_to_weight_dic = load_cows("ps1_cow_data.txt")
        cow_from_name_to_weight_dic = load_cows("ps1_cow_data_2.txt")
        trip_list = brute_force_cow_transport(cow_from_name_to_weight_dic)
        for trip in trip_list:
            print(trip)

    def test_compare_cow_transport_algorithms(self):
        compare_cow_transport_algorithms()