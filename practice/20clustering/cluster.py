import pylab


# set line width
# pylab.rcParams['lines.linewidth'] = 6
# # set general font size
# pylab.rcParams['font.size'] = 12
# # set font size for labels on axes
# pylab.rcParams['axes.labelsize'] = 18
# # set size of numbers on x-axis
# pylab.rcParams['xtick.major.size'] = 5
# # set size of numbers on y-axis
# pylab.rcParams['ytick.major.size'] = 5
# # set size of markers
# pylab.rcParams['lines.markersize'] = 10


def minkowskiDist(v1, v2, p):
    # Assumes v1 and v2 are equal length arrays of numbers
    # 闵式距离 特别地 p=1表示曼哈顿距离,也叫绝对距离。p=2表示欧几里得距离
    dist = 0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p
    return dist ** (1 / p)


class Example(object):

    def __init__(self, name, features, label=None):
        # Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        # 维度 也即单个样本的特征种类个数 .e.g example = [男,33,未婚],它的维度即为3
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        # 此处是返回欧几里得距离
        return minkowskiDist(self.features, other.getFeatures(), 2)

    def __str__(self):
        return self.name + ':' + str(self.features) + ':' \
               + str(self.label)


class Cluster(object):

    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""
        self.examples = examples
        self.centroid = self.computeCentroid()

    def update(self, examples):
        """Assume examples is a non-empty list of Examples
           Replace examples; return amount centroid has changed"""
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)

    def computeCentroid(self):
        """
        ------ 教授说--------------
        python2x 写法,必须写[0.0]
        vals = pylab.array([0.0] * self.examples[0].dimensionality())
        python3写法
        vals = pylab.array([0] * self.examples[0].dimensionality())
        ------ 教授说--------------
        但是我发现 如果特征值是浮点值的话 这里还只能是
        vals = pylab.array([0.0] * self.examples[0].dimensionality())
        可能是我对pylab.array 不熟悉。

        此方法计算该Cluster的聚类中心。
        比如example的维度是3，这里的array的元素就是3个,computeCentroid就是
        每个Example的对应特征值相加，取平均,然后据此创建并返回新的聚类中心。
        """
        vals = pylab.array([0.0] * self.examples[0].dimensionality())
        for e in self.examples:  # compute mean
            vals += e.getFeatures()
        centroid = Example('centroid', vals / len(self.examples))
        return centroid

    def get_examples(self):
        return self.examples

    def getCentroid(self):
        return self.centroid

    def variability(self):
        totDist = 0
        for e in self.examples:
            totDist += (e.distance(self.centroid)) ** 2
        return totDist

    def members(self):
        # https://blog.csdn.net/mieleizhi0522/article/details/82142856/
        # 此函数是 生成器。简单来说 第一次调用members,会返回第一个e,第二次调用members，会返回第一个e。
        # 调用方法是 f = c.members() ,next(f)  next(f)。c是Cluster的实例,next是一个函数
        # 不要这样 next(c.memebers()) ,next(c.members())
        # 如果超出范围,比如两个example,调用3次,那么会报错的。
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid ' \
                 + str(self.centroid.getFeatures()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]  # remove trailing comma and space


def dissimilarity(clusters):
    """Assumes clusters a list of clusters
       Returns a measure of the total dissimilarity of the
       clusters in the list"""
    totDist = 0
    for c in clusters:
        totDist += c.variability()
    return totDist


# a = Example('jack', pylab.array([1.0, 2.0, 3.0]))
# b = Example('roy', pylab.array([0.0, 2.0, 2.0]))
# print(a.distance(b))
# examples = [a, b]
# c = Cluster(examples)
# print(c.variability())
# print(c.getCentroid())
# f =c.members()
# print(next(f))
# print(next(f))
# print(c)

# 测试 dissimilarity(clusters)
# a = Example('jack', pylab.array([1.0, 2.0, 3.0]))
# b = Example('roy', pylab.array([0.0, 2.0, 2.0]))
# examples = [a, b]
# c1 = Cluster(examples)
#
# a = Example('jack', pylab.array([1.0, 2.0, 3.0]))
# b = Example('roy', pylab.array([0.0, 2.0, 2.0]))
# examples = [a, b]
# c2 = Cluster(examples)
#
# dissimilarity([c1,c2])
