"""
@Author  : Lord_Bao
@Date    : 2021/4/4

"""
import pylab


def minkowski_dist(v1, v2, p):
    """
    计算v1和v2 之间的闵式距离，当p=1，表示曼哈顿距离。p=2表示欧几里得距离
    """
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p

    return dist ** (1.0 / p)


class Animal(object):
    def __init__(self, name, features, label=None):
        self.name = name
        self.features = pylab.array(features)
        self.label = label

    def get_name(self):
        return self.name

    def get_features(self):
        return self.features

    # 默认计算的是欧几里得距离
    def get_minkowski_dist_from_other(self, other, p=2):
        return minkowski_dist(self.features, other.get_features(), p)

    def __str__(self):
        return self.name + ":" + str(self.features)


def compareAnimals(animals, title, precision, p=2):
    """
    :param p: 闵式距离参数 默认为2，即欧几里得距离
    :param animals:  list  of Animals
    :param precision: 距离精度

    制作一张table，该table绘制了不同动物之间的距离
    """
    # 1.行列起首的名称
    column_label = []
    for ani in animals:
        column_label.append(ani.get_name())
    row_label = column_label[:]

    # 2.计算动物之间的距离
    table_val = []
    for i in range(len(animals)):
        ani = animals[i]
        this_row_val = []
        for j in range(len(animals)):
            if i == j:
                this_row_val.append("--")
            else:
                this_row_val.append(str(round(ani.get_minkowski_dist_from_other(animals[j], p), precision)))
        table_val.append(this_row_val)

    # 3.绘制距离图
    pylab.figure(num=1, frameon=False)
    table = pylab.table(rowLabels=row_label,
                        colLabels=column_label,
                        cellText=table_val,
                        cellLoc="center",  # 每个cell里面的内容摆放位置
                        loc="center",  # 整个table在figure的摆放位置
                        colWidths=[0.2] * len(animals),  # 每列的宽度
                        )
    table.scale(1, 2.5)  # table的cell的宽度不变,高度*2.5
    # 去除掉 x轴  和 y轴的刻度
    # pylab.xticks(ticks=[])
    # pylab.yticks(ticks=[])
    # 去掉坐标轴
    pylab.axis('off')
    pylab.title(title)
    pylab.show()


"""
动物的特征向量是 egg-laying,scales,poisonous,cold_blooded,legs
"""

animal_list_binary_feature = [
    Animal("rattlesnake", [1, 1, 1, 1, 0]),
    Animal("boa\nconstrictor", [0, 1, 0, 1, 0]),
    Animal("dartFrog", [1, 0, 1, 0, 1]),
    Animal("alligator", [1, 1, 0, 1, 1])
]

animal_list_non_binary_feature = [
    Animal("rattlesnake", [1, 1, 1, 1, 0]),
    Animal("boa\nconstrictor", [0, 1, 0, 1, 0]),
    Animal("dartFrog", [1, 0, 1, 0, 4]),
    Animal("alligator", [1, 1, 0, 1, 4])
]

# 计算欧几里得距离,采用未缩放过(legs)的特征
compareAnimals(animal_list_non_binary_feature, title="Euclidean distance;No Scale", precision=3, p=2)
# 计算曼哈顿距离,采用未缩放过(legs)的特征
compareAnimals(animal_list_non_binary_feature, title="Absolute distance;No Scale", precision=3, p=1)
# 计算欧几里得距离,但采用的是缩放过的特征
compareAnimals(animal_list_binary_feature, title="Euclidean distance;Scale", precision=3, p=2)
