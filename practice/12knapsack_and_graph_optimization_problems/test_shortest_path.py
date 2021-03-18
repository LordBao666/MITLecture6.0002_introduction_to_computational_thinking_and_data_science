"""
@Author  : Lord_Bao
@Date    : 2021/3/18

"""
from shortest_path import *

if __name__ == '__main__':
    """
    # ############测试Node Edge Graph ############
    """
    # ############构建node############
    name_list = ["0", '1', '2', '3', '4', '5']
    node_list = []
    for name in name_list:
        node = Node(name)
        node_list.append(node)
    # for elt in node_list:
    #     print(elt)
    # ############构建node############

    # ############构建edge############
    edge_list = []
    edge_list.append(Edge(node_list[0], node_list[1]))
    edge_list.append(Edge(node_list[0], node_list[2]))
    edge_list.append(Edge(node_list[1], node_list[0]))
    edge_list.append(Edge(node_list[1], node_list[2]))
    edge_list.append(Edge(node_list[2], node_list[3]))
    edge_list.append(Edge(node_list[2], node_list[4]))
    edge_list.append(Edge(node_list[3], node_list[1]))
    edge_list.append(Edge(node_list[3], node_list[4]))
    edge_list.append(Edge(node_list[3], node_list[5]))
    edge_list.append(Edge(node_list[4], node_list[0]))
    # for elt in edge_list:
    #     print(elt)
    # ############构建edge############

    # ############构建digraph############
    di_graph = DiGraph()
    for node in node_list:
        di_graph.add_node(node)
    for edge in edge_list:
        di_graph.add_edge(edge)
    # print(di_graph)
    # ############构建digraph############
    """
       # ############测试Node Edge Graph ############
    """

    # ############## 测试print_path ###########
    # print(print_path(node_list))
    # ############## 测试print_path ###########

    # #############  测试dfs ##############
    # shortest_path = dfs(di_graph, node_list[0], node_list[5], [], None, True)
    # print("shortest path: " + print_path(shortest_path))
    # shortest_path = dfs(di_graph, node_list[0], node_list[4], [], None, True)
    # print("shortest path: " + print_path(shortest_path))
    # #############  测试dfs ##############

    # #############  测试bfs ##############
    shortest_path = bfs(di_graph, node_list[0], node_list[5], True)
    print("shortest path: " + print_path(shortest_path))
    # shortest_path = bfs(di_graph, node_list[0], node_list[4], True)
    # print("shortest path: " + print_path(shortest_path))
    # #############  测试bfs ##############
