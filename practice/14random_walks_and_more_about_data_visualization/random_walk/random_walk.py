"""
@Author  : Lord_Bao
@Date    : 2021/3/21

"""
from entity import *
import pylab


def walk(drunk, field, num_steps):
    """
    :param drunk:  Drunk实例
    :param field:  Field实例,假设drunk 处在 field中
    :param num_steps: 走的步数
    :return: 返回初始点到走了num_steps的距离
    """
    start_loc = field.get_location(drunk)
    for n in range(num_steps):
        field.move_drunk(drunk)

    end_loc = field.get_location(drunk)
    return start_loc.distance_from(end_loc)


def sim_walk(num_steps, num_trials, d_class):
    """
    :param num_steps: 测试步数
    :param num_trials: 测试次数
    :param d_class: Drunk的种类  是一个构造函数
    :return: 一个list,存储num_trials次的distance
    """
    f = Field()
    start = Location(0.0, 0.0)
    d = d_class()
    f.add_drunk(d, start)
    distances = []
    for n in range(num_trials):
        dist = walk(d, f, num_steps)
        distances.append(round(dist, 1))  # 精度为1
    return distances


def drunk_test(walk_length, num_trials, d_class):
    """
       :param walk_length: 测试步数 是个列表
       :param num_trials: 测试次数
       :param d_class: Drunk的种类  是一个构造函数

       """
    for i in walk_length:
        distances = sim_walk(i, num_trials, d_class)
        print(d_class.__name__, "random walk of", i, "steps")
        print("Mean = ", round(sum(distances) / len(distances), 4))
        print("Max = ", max(distances), "Min = ", min(distances))


def drunk_test_with_graph(walk_length, num_trials, d_class_list):
    """
         :param walk_length: 测试步数 是个列表
         :param num_trials: 测试次数
         :param d_class_list: Drunk的种类  若干构造函数

      """
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
    styles = StyleIterator([".-b", ".-.g", ".:r"])
    for d_class in d_class_list:
        cur_style = styles.next_style()
        mean_distance = []
        for num_step in walk_length:
            distances = sim_walk(num_step, num_trials, d_class)
            mean_distance.append(round(sum(distances) / len(distances), 4))
        pylab.plot(walk_length, mean_distance, cur_style, label=d_class.__name__)

    pylab.title("Distance from origin(" + str(num_trials) + ")trials")
    pylab.xlabel("Num of steps")
    pylab.ylabel("Distance from origin")
    pylab.legend(loc="best")  # 将图例放在最好的位置。问题不是很大，可以不设置。可选的还有如
    # ===============   =============
    #         Location String   Location Code
    #         ===============   =============
    #         'best'            0
    #         'upper right'     1
    #         'upper left'      2
    #         'lower left'      3
    #         'lower right'     4
    #         'right'           5
    #         'center left'     6
    #         'center right'    7
    #         'lower center'    8
    #         'upper center'    9
    #         'center'          10
    pylab.semilogx()  # Base 默认是10 。简单来说就是将你的 x 取对数展。比如x =1000 ，那么在图上展示的 log1000 = 3  。但是图上户表明是 10^3
    pylab.semilogy()
    pylab.show()


def get_final_locs(num_steps, num_trials, d_class):
    """

    :param num_steps: 走几步
    :param num_trials: 试验次数
    :param d_class: Drunk的构造函数
    :return: 记录num_trials  的最终location
    """
    locs = []

    for trial in range(num_trials):
        drunk = d_class()
        start = Location(0.0, 0.0)
        field = Field()
        field.add_drunk(drunk, start)
        for step in range(num_steps):
            field.move_drunk(drunk)
        locs.append(field.get_location(drunk))

    return locs


def plot_locs(drunk_kinds, num_steps, num_trials):
    styles = StyleIterator(["ob", "xg", "^r"])
    for drunk_kind in drunk_kinds:
        final_locs = get_final_locs(num_steps, num_trials, drunk_kind)
        x_locs = []
        y_locs = []
        for loc in final_locs:
            x_locs.append(loc.get_x())
            y_locs.append(loc.get_y())
        mean_x = sum(x_locs) / len(x_locs)
        mean_y = sum(y_locs) / len(y_locs)

        label_str = drunk_kind.__name__ + "mean loc : <" + str(mean_x) + "," + str(mean_y) + ">"
        pylab.plot(x_locs, y_locs, styles.next_style(), label=label_str)
    pylab.title('Location at End of Walks (' + str(num_steps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc='lower left')
    pylab.show()


def trace_walk(drunk_kinds, num_steps):
    styles = StyleIterator(["ob", "xg", "^r", "+m"])
    # field = Field()
    field = OddField(2000,200,200)
    for drunk_kind in drunk_kinds:

        start = Location(0.0, 0.0)
        drunk = drunk_kind()
        field.add_drunk(drunk, start)
        x_walk = [0.0]
        y_walk = [0.0]
        for step in range(num_steps):
            field.move_drunk(drunk)
            loc = field.get_location(drunk)
            x_loc = loc.get_x()
            y_loc = loc.get_y()
            x_walk.append(x_loc)
            y_walk.append(y_loc)
        pylab.plot(x_walk, y_walk, styles.next_style(), label=drunk_kind.__name__)

    pylab.title('Spots Visited on Walk ('
                + str(num_steps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc='best')
    pylab.show()
