"""
@Author  : Lord_Bao
@Date    : 2021/3/16

"""

if __name__ == '__main__':
    list1 = [3, -6, 2]
    list2 = [2, 4, 7]

    # abs
    temp_list = []
    for elt in map(abs, list1):
        temp_list.append(elt)
    assert temp_list == [3, 6, 2]
    print(temp_list)
    print("--------------------------")

    # max
    temp_list = []
    for elt in map(max, list1, list2):
        temp_list.append(elt)
    assert temp_list == [3, 4, 7]
    print(temp_list)
    print("--------------------------")

    # lambda  power
    temp_list = []
    for elt in map(lambda x, y: x ** y, list1, list2):
        temp_list.append(elt)
    assert temp_list == [9, 1296, 128]
    print(temp_list)
