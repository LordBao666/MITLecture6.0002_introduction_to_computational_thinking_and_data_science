"""
@Author  : Lord_Bao
@Date    : 2021/3/17

"""
"""
关于斐波拉契时间复杂度的分析(大概分析)
1.最普通的斐波拉契数列计算，见fib(self, n):
  这个函数忽略掉那些打印的步骤,我们发现当
  n >= 2 时,  fib花的时间 主要在 判断是不是base_case 和 fib(n) = fib(n-1) + fib(n-2)上。
  我们画树形图的时候,fib(n) 下面要计算 fib(n-1) + fib(n-2)。我们放小一下，求
  fib(n-1)+fib(n-2)的复杂度肯定要比 2fib（n-2) 要大.
  即 O(fib(n))  = O(1) + O(fib(n-1) + fib(n-2)) >= O(1) + 2O(fib(n-2))
  也就意味着
  O(fib(n)) >= O(1) + 2O(fib(n-2)) >= O(1)  + 2(O(1) + 2O(fib(n-4))) = 3O(1) + 4O(fib(n-4)))
            >= (1+ 2+ 4+.... 2^n/2)O(1)  + 2^2/nO(fib(1))
            =  O(2^n/2) (根号2 的n次方)
  也就是说最普通的斐波拉契数列的 算法复杂度 至少是 指数型。碰到指数型的就肯定嗝屁了。          

2.带字典的斐波拉契数列计算,见fast_fib(self, n, memo={0: 1, 1: 1}):  
  这个函数忽略掉那些打印的步骤,我们发现当
  n >= 2 时,  fib花的时间 主要在 是不是字典中 ,  fib(n) = fib(n-1) + fib(n-2)  和 将新的kv对存储到 字典中
  按照深度优先 和 左优先的顺序
  求O(fib(n)) == O(len(old_dic)) + O(fib(n-1) + fib(n-2)) + O(len(new_dic)
   注意 查询字典，存储新的KV对的worst_case的情况下 是 O(len(dic)) 还有计算后O(fib(n-1) + fib(n-2))的字典已经不是原来的字典了
   all right ,开始分析
   O(fib(n)) = O(2) + O(fib(n-1) + fib(n-2)) + O(len(new_dic)
             ################################看下面的公式会晕，画图分析比较快######################
             = O(2) + O(2) + O(fib(n-2))+ O(fib(n-3) + O(len(new_dic2) + O(fib(n-2)) + O(len(new_dic)
             = nO(2) + O(fib(1))+O(fib(0)) +O(len(new_dicn-1)+ .... +   O(fib(n-3) + O(len(new_dic2) + O(fib(n-2)) + O(len(new_dic)
             = nO(2) + O(2)+O(2)+O(2) + O(2) + O(fib(1)+O(len(new_dicn-2)  +....+O(fib(n-3) + O(len(new_dic2) + O(fib(n-2)) + O(len(new_dic)
             = nO(2) + O(2)+O(2)+O(2) + O(2) + O(3) +O(3) + O(fib(2)+O(len(new_dicn-3)
             ？？？？？？？？？？？？？？？？
              ################################看上面的公式会晕，画图分析比较快######################
    O(fib(n)) = O(2) + O(fib(n-1) + fib(n-2)) + O(len(new_dic)
    按照深度优先 和 左优先的顺序
    1.从fib(n)  到 fib(2) ,都是在查x是不是在字典里。这段时间字典的长度是2，那么时间复杂度是 2O(n-1)
    2.求fib(2):在step1查完字典后 来到 fib(1) + fib(0) ,查字典耗时2O(2),将两个相加耗时O(1),存储fib(2) 耗时 O(2)
    3.求fib(3):注意第1步的查找字典已经算了查找3是不是在字典了，不要加这部分。求fib(3)，需要计算fib(2)+fib(1)
               fib(2)已经由第2步计算，所以这里是查fib(1)  查字典耗时 O(3) ,相加O(1)，存储fib(3)耗时O(3)
    4.求fib(4):再三强调第1步，已经查了4是不是字典的key了，所以这里不加,fib(3) + fib(2)中，fib(3)的计算耗时也有第3步计算
    所以不管。所以现在是求 fib(2)查字典耗时 O(4) ,fib(3)+fib(2) 耗时 O(1),存储fib(4)耗时O(4)
    5.求fib(5):  求fib(3) 耗时 O(5) fib(3)+fib(4)耗时 O(1) ，存储fib(5) 耗时O(5)
    .....
    n.求fib(n):  求fib(n-1) 耗时 O(n-1)   fib(n-2)+fib(n-1) 耗时 O(1),存储fib(n) 耗时 O(n-1)
    
    所以把步骤1到n加起来
    2O(n-1) + (2O(2) + O(3)+O(4)+..O(n-1)) + n-1O(1) + (O(2)+O(3)+....O(n-1))
    =O(n^2)
    
    也就是多项式级别的，这个比指数好多了,但是如果我们不考虑查字典的耗时，将查字典看做是O(1).那么上述方式就是O(n)
    
    3.迭代式斐波拉契数列:
    很明显O(n)
    
    斐波拉契数列能用dp解决的原因是:
    1.满足最优子结构,显然 fib(n) = fib(n-1)+fib(2)
    2.重叠子问题,显然,存在大量相同的问题。
    用动态规划解决这类问题的关键就是 记忆化,也就是将将新的结果存储到字典里,这样可以节省很多求重复问题的时间。
    
"""


class FibFamily(object):
    # fib(x) 计算的次数 排除base_case  n==0 和 n ==1的情况
    fib_count = 0
    # fast_fib(x) 计算的次数 排除base_case  n==0 和 n ==1的情况，将这种情况存储到memo中
    fast_fib_count = 0
    # iter_fib(x)  计算的次数 排除n==0 和 n ==1的情况
    iter_fib_count = 0

    def fib(self, n):
        if n == 0 or n == 1:
            return 1
        FibFamily.fib_count += 1
        ans = self.fib(n - 1) + self.fib(n - 2)
        print("fib(" + str(n) + ") -->" + str(ans))
        return ans

    def fast_fib(self, n, memo={0: 1, 1: 1}):
        if n in memo:
            return memo[n]
        FibFamily.fast_fib_count += 1
        ans = self.fast_fib(n - 1, memo) + self.fast_fib(n - 2, memo)
        memo[n] = ans
        print("fast_fib(" + str(n) + ") -->" + str(ans))
        return ans

    def iter_fib(self, n):
        if n == 1 or n == 0:
            FibFamily.iter_fib_count += 1
            return 1
        result_1 = 1
        result_2 = 1

        for iter_left in range(2, n + 1):
            FibFamily.iter_fib_count += 1
            result_2 = result_2 + result_1
            result_1 = result_2 - result_1
            print("iter_fib(" + str(iter_left) + ") -->" + str(result_2))
        return result_2


if __name__ == '__main__':
    n = 6
    print("\nfib(" + str(n) + ")-->" + str(FibFamily().fib(n)))
    print("num spent --> " + str(FibFamily.fib_count))
    print("####################################################")
    print("\nfast_fib(" + str(n) + ")-->" + str(FibFamily().fast_fib(n)))
    print("num spent --> " + str(FibFamily.fast_fib_count))
    print("####################################################")
    print("\niter_fib(" + str(n) + ")-->" + str(FibFamily().iter_fib(n)))
    print("num spent --> " + str(FibFamily.iter_fib_count))
    print("####################################################")
