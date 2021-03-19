###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
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


def dp_make_weight_more_detail(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int,dict,
                     int smallest number of eggs needed to make target weight
                     dict  :  key egg_weight_type ,value :num _of _used_egg_weight_type
                     比如 target_weight 为3时,int 为 3 ,dict 为 {1:3}
    """

    if target_weight == 0:
        return 0, {}

    if target_weight in memo:
        return memo[target_weight]

    result_int, result_dic = None, {}  # 占位符,没有多大用

    for elt in egg_weights:
        if target_weight - elt >= 0:  # 这样才有继续探索的必要
            tmp_int, tmp_dic = dp_make_weight_more_detail(egg_weights, target_weight - elt, memo)
            tmp_int += 1  # 加上本次

            if result_int is None or tmp_int < result_int:
                result_int = tmp_int
                if elt in tmp_dic:
                    tmp_dic = tmp_dic.copy()  # 不要破坏原来的dic的结构
                    tmp_dic[elt] += 1
                else:
                    tmp_dic = tmp_dic.copy()  # 不要破坏原来的dic的结构
                    tmp_dic[elt] = 1
                result_dic = tmp_dic

    memo[target_weight] = result_int, result_dic
    return result_int, result_dic


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (1, 5, 10, 25)
    # n = 99
    # memo = {}
    # print("Egg weights = (1, 5, 10, 25)")
    # print("n = 99")
    # print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    # print("Actual output:", dp_make_weight(egg_weights, n,memo))
    # print("memo",memo)
    # print()

    # egg_weights = (1, 5, 10, 20)
    # n = 99
    # memo = {}
    # print("Egg weights = (1, 5, 10, 25)")
    # print("n = 99")
    # print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    # print("Actual output:", dp_make_weight(egg_weights, n, memo))
    # print("memo", memo)
    # print()

    # egg_weights = (1, 5, 10, 20)
    # n = 99
    # memo = {}
    # print("Egg weights = (1, 5, 10, 25)")
    # print("n = 99")
    # print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    # print("Actual output:", dp_make_weight_more_detail(egg_weights, n, memo))
    # print("memo", memo)
    # print()

    egg_weights = (1, 5, 10, 25)
    n = 99
    memo = {}
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight_more_detail(egg_weights, n, memo))
    # print("memo", memo)
    print()
