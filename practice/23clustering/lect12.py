import cluster
import random, pylab, numpy

"""
83人positive ,共250人

"""


class Patient(cluster.Example):
    pass


def scaleAttrs(vals):
    vals = pylab.array(vals)
    mean = sum(vals) / len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals / sd


def getData(toScale=False):
    # read in data
    hrList, stElevList, ageList, prevACSList, classList = [], [], [], [], []
    cardiacData = open('cardiacData.txt', 'r')
    for l in cardiacData:
        l = l.split(',')
        hrList.append(int(l[0]))
        stElevList.append(int(l[1]))
        ageList.append(int(l[2]))
        prevACSList.append(int(l[3]))
        classList.append(int(l[4]))
    if toScale:
        hrList = scaleAttrs(hrList)
        stElevList = scaleAttrs(stElevList)
        ageList = scaleAttrs(ageList)
        prevACSList = scaleAttrs(prevACSList)
    # Build points
    points = []
    for i in range(len(hrList)):
        features = pylab.array([hrList[i], prevACSList[i], \
                                stElevList[i], ageList[i]])
        pIndex = str(i)
        points.append(Patient('P' + pIndex, features, classList[i]))
    return points


def kmeans(examples, k, verbose=False):
    """
    :param examples:  样本 类型Example
    :param k: k表示k个聚类中心
    :param verbose: 冗长的意思，这里类比 to_print
    :return: k-mean的结果
    """
    # Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    clusters = []
    # 依据k个initialCentroids,创建k个Cluster(每个Cluster的点暂时只有一个,即对应的initialCentroid
    for e in initialCentroids:
        clusters.append(cluster.Cluster([e]))

    # Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        # Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])

        # Associate each example with closest centroid
        for e in examples:
            # Find the centroid closest to e
            # 假设e与第一个Cluster的聚类中心的距离是最短的，然后根据实际情况更新
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            # Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)

        for c in newClusters:  # Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        # Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            # 第i个更新examples和聚类中心,并返回旧的聚类中心和新的聚类中心的距离
            # 如果该距离大于0,表示聚类中心发生变化,根据k-mean算法，继续执行一次while循环，直到converged = True,即聚集完成
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('')  # add blank line
    return clusters


def trykmeans(examples, numClusters, numTrials, verbose=False):
    """Calls kmeans numTrials times and returns the result with the
          lowest dissimilarity"""
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = cluster.dissimilarity(best)
    trial = 1
    while trial < numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue  # If failed, try again
        currDissimilarity = cluster.dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best


def printClustering(clustering):
    """Assumes: clustering is a sequence of clusters
       Prints information about each cluster
       Returns list of fraction of pos cases in each cluster

       简单来说就是 clustering = [cluster1,cluster2,clustern] 不一定是列表
       返回每个cluster中的 positive/总的个数
       即 fractions = [posratio1,poratio2.。。。。]
       """
    posFracs = []
    for c in clustering:
        numPts = 0
        numPos = 0
        for p in c.members():
            numPts += 1
            if p.getLabel() == 1:
                numPos += 1
        fracPos = numPos / numPts
        posFracs.append(fracPos)
        print('Cluster of size', numPts, 'with fraction of positives =',
              round(fracPos, 4))
    return pylab.array(posFracs)


def get_positive_ratio(this_cluster):
    """
    :return:  返回单个cluster 的  positive 占比
    """
    numPts = 0
    numPos = 0
    for p in this_cluster.members():
        numPts += 1
        if p.getLabel() == 1:
            numPos += 1
    fracPos = numPos / numPts

    return fracPos


def testClustering(patients, numClusters, seed=0, numTrials=5):
    random.seed(seed)
    bestClustering = trykmeans(patients, numClusters, numTrials)
    posFracs = printClustering(bestClustering)
    return posFracs


patients = getData(True)
# for k in (2, 3, 4, 5, 6):
#     print('\n     Test k-means (k = ' + str(k) + ')')
#     posFracs = testClustering(patients, k, 2)

# numPos = 0
# for p in patients:
#    if p.getLabel() == 1:
#        numPos += 1
# print('Total number of positive patients =', numPos)


clusters = trykmeans(patients, 4, 5)
count = 0
print("In All Clusters,High Positive Cluster:")
for cur_cluster in clusters:
    if get_positive_ratio(cur_cluster) > 0.6:  # 假定0.6就算高 positive
        print("Positive Examples of Cluster" + str(count) + ":\n")
        for example in cur_cluster.get_examples():
                print(example)
