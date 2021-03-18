"""
@Author  : Lord_Bao
@Date    : 2021/3/18

"""


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


class DiGraph(object):
    def __init__(self):
        """
        nodes  即为DiGraph的 节点
        edges  即为Digraph的 边 key 为 Node, value为 Node 的子节点集合（list)
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
