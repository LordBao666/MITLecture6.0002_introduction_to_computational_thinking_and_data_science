# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge


#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
# 将校园中的所有Building视作Node,将校园中Building之间的连接关系看做是边,distance也由
# 边进行封装


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    print("Loading map from file...")
    campus_map = Digraph()
    with open(map_filename, 'r') as file_handle:
        for line in file_handle:  # 32 36 70 0
            info = line.strip().split()  # info = ["32","36","70","0"] strip返回一个去掉前后端的line的副本
            from_node = Node(info[0])
            to_node = Node(info[1])
            if not campus_map.has_node(from_node):
                campus_map.add_node(from_node)
            if not campus_map.has_node(to_node):
                campus_map.add_node(to_node)
            cur_edge = WeightedEdge(from_node, to_node, int(info[2]), int(info[3]))
            # 假设cur_edge不存在重复的情况,也就是说mit_map.txt没有提供重复的数据
            campus_map.add_edge(cur_edge)
    return campus_map


# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer: 该函数的输入是一个DiGraph,输出是最短路径。限制是最小。
#

def check_valid_node(graph, from_node, to_node):
    """

    :param graph: DiGraph  的实例对象
    :param from_node: str
    :param to_node: str

    检验 from_node 和 to_node是不是graph中的节点,不是抛出 Value_Error
    """
    node_a = Node(from_node)
    node_b = Node(to_node)
    if not (graph.has_node(node_a) and graph.has_node(node_b)):
        raise ValueError("Node not in graph")


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


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
