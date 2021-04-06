# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:45:20 2016

@author: johnguttag
"""
import numpy
import pylab, random


# set line width
# pylab.rcParams['lines.linewidth'] = 4
# #set font size for titles
# pylab.rcParams['axes.titlesize'] = 20
# #set font size for labels on axes
# pylab.rcParams['axes.labelsize'] = 20
# #set size of numbers on x-axis
# pylab.rcParams['xtick.labelsize'] = 16
# #set size of numbers on y-axis
# pylab.rcParams['ytick.labelsize'] = 16
# #set size of ticks on x-axis
# pylab.rcParams['xtick.major.size'] = 7
# #set size of ticks on y-axis
# pylab.rcParams['ytick.major.size'] = 7
# #set size of markers
# pylab.rcParams['lines.markersize'] = 10
# #set number of examples shown in legends
# pylab.rcParams['legend.numpoints'] = 1

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p
    return dist ** (1 / p)


class Animal(object):
    def __init__(self, name, features):
        """Assumes name a string; features a list of numbers"""
        self.name = name
        self.features = pylab.array(features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        """Assumes other an Animal
           Returns the Euclidean distance between feature vectors
              of self and other"""
        return minkowskiDist(self.getFeatures(),
                             other.getFeatures(), 2)

    def __str__(self):
        return self.name


##Actual number of legs
# cobra = Animal('cobra', [1,1,1,1,0])
# rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
# boa = Animal('boa\nconstrictor', [0,1,0,1,0])
# chicken = Animal('chicken', [1,1,0,1,2])
# alligator = Animal('alligator', [1,1,0,1,4])
# dartFrog = Animal('dart frog', [1,0,1,0,4])
# zebra = Animal('zebra', [0,0,0,0,4])
# python = Animal('python', [1,1,0,1,0])
# guppy = Animal('guppy', [0,1,0,0,0])
# animals = [cobra, rattlesnake, boa, chicken, guppy,
#           dartFrog, zebra, python, alligator]
#
##Binary features only           
cobra = Animal('cobra', [1, 1, 1, 1, 0])
rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
boa = Animal('boa\nconstrictor', [0, 1, 0, 1, 0])
# chicken  的  legs  应该是错了吧 按照binary,这里应该是1，而不是2
# chicken = Animal('chicken', [1, 1, 0, 1, 2])
chicken = Animal('chicken', [1, 1, 0, 1, 1])
alligator = Animal('alligator', [1, 1, 0, 1, 1])
dartFrog = Animal('dart frog', [1, 0, 1, 0, 1])
zebra = Animal('zebra', [0, 0, 0, 0, 1])
python = Animal('python', [1, 1, 0, 1, 0])
guppy = Animal('guppy', [0, 1, 0, 0, 0])
animals = [cobra, rattlesnake, boa, chicken, guppy,
           dartFrog, zebra, python, alligator]


def compareAnimals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of Euclidean distance between each animal"""
    # Get labels for columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    # Get distances between pairs of animals
    # For each row
    for a1 in animals:
        row = []
        # For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    # Produce table
    table = pylab.table(rowLabels=rowLabels,
                        colLabels=columnLabels,
                        cellText=tableVals,
                        cellLoc='center',
                        loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2.5)
    pylab.axis('off')
    pylab.savefig('distances')
    # pylab.show()


# compareAnimals(animals, 3)
# assert False

class Passenger(object):
    featureNames = ('C1', 'C2', 'C3', 'age', 'male gender')

    def __init__(self, pClass, age, gender, survived, name):
        self.name = name
        # 前面3个0代表客舱等级，分别是1等 2等 3等
        self.featureVec = [0, 0, 0, age, gender]
        self.featureVec[pClass - 1] = 1
        self.label = survived
        self.cabinClass = pClass
        #     featureNames = ('C2', 'C3', 'age', 'male gender')
        #     def __init__(self, pClass, age, gender, survived, name):
        #         self.name = name
        #         if pClass == 2:
        #             self.featureVec = [1, 0, age, gender]
        #         elif pClass == 3:
        #             self.featureVec = [0, 1, age, gender]
        #         else:
        #             self.featureVec = [0, 0, age, gender]
        #         self.label = survived
        #         self.cabinClass = pClass


    def distance(self, other):
        return minkowskiDist(self.featureVec, other.featureVec, 2)

    def getClass(self):
        return self.cabinClass

    def getAge(self):
        return self.featureVec[3]

    def getGender(self):
        return self.featureVec[4]

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.featureVec[:]

    def getLabel(self):
        return self.label

    def __str__(self):
        return "name :" + str(self.name) + ";feature:" + str(self.featureVec) + ";survived:" + str(self.label)


def getTitanicData(fname):
    """
    TitanicPassengers.txt 里面的每行的数据分别代表
    class(int,1,2,3)  age(float)   gender(int,1表Male,0表Female) survived(survived,died）  name(str)

    返回一个词典 data{

    'class' = [],
    'age' = [],
    'gender' = []
    'survived' = []
    'name' = []
    }
    """
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(float(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else:
            data['gender'].append(0)
        if split[3] == '1':
            data['survived'].append('Survived')
        else:
            data['survived'].append('Died')
        data['name'].append(split[4:])
        line = f.readline()
    return data


def buildTitanicExamples(fileName):
    """
    :param fileName:  读取TitanicPassengers.txt，转为Passenger,用list存储并返回
    :return:
    """
    data = getTitanicData(fileName)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i],
                      data['gender'][i], data['survived'][i],
                      data['name'][i])
        examples.append(p)
    print('Finishe processing', len(examples), 'passengers\n')
    return examples


examples = buildTitanicExamples('TitanicPassengers.txt')


def findNearest(name, exampleSet, metric):
    """
    :param name: Passenger 的 name
    :param exampleSet: 所有passenger的集合
    :param metric: 度量准则


    NN 算法   返回距离name  最近的邻居  ,类型 Passenger
    """
    exist_name = False
    example = None
    for e in exampleSet:
        if e.getName() == name:
            example = e
            exist_name = True
            break
    if not exist_name:
        raise ValueError("name doesn't EXIST!")

    nearest_dist = None
    nearest_neighbor = None
    for e in exampleSet:
        if e.getName() != name:
            if nearest_dist is None or \
                    metric(example, e) < nearest_dist:
                nearest_neighbor = e
                nearest_dist = metric(example, nearest_neighbor)
    return nearest_neighbor


def accuracy(truePos, falsePos, trueNeg, falseNeg):
    """
         评估手段： 准确度
    """
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator / denominator


def sensitivity(truePos, falseNeg):
    """
         评估手段：percentage  correctly found
    """
    try:
        return truePos / (truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')


def specificity(trueNeg, falsePos):
    """
         评估手段：  percentage correctly rejected
    """
    try:
        return trueNeg / (trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')


def posPredVal(truePos, falsePos):
    """
         评估手段： 成功预估正确占比 即 成功预估正确/成功预估正确 + 错误预估正确
    """
    try:
        return truePos / (truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')


def negPredVal(trueNeg, falseNeg):
    """
         评估手段： 成功预估错误占比  即 成功预估错误 / 成功预估错误 + 错误预估错误
    """
    try:
        return trueNeg / (trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')


def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint=True):
    """
     get  statistics about evaluation result of  accuracy,sensitivity,specificity,positive predicted values
    """
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return (accur, sens, spec, ppv)


def findKNearest(example, exampleSet, k):
    """

    :param example: Passenger
    :param exampleSet: a set of Passengers
    :param k:

    KNN 算法  返回最近的 K 个 Passenger 和  距离
    """

    # kNearest, distances = [], []
    # # Build lists containing first k examples and their distances
    # for i in range(k):
    #     kNearest.append(exampleSet[i])
    #     distances.append(example.distance(exampleSet[i]))
    # maxDist = max(distances)  # Get maximum distance
    # # Look at examples not yet considered
    # for e in exampleSet[k:]:
    #     dist = example.distance(e)
    #     if dist < maxDist:
    #         # replace farther neighbor by this one
    #         maxIndex = distances.index(maxDist)
    #         kNearest[maxIndex] = e
    #         distances[maxIndex] = dist
    #         maxDist = max(distances)
    # return kNearest, distances

    # 按照最近距离排序的 example_list
    nearest_dist_example = sorted(exampleSet, key=lambda elt: elt.distance(example))
    kNearest = nearest_dist_example[:k]
    distances = [elt.distance(example) for elt in kNearest]
    return kNearest, distances


# example_set = [
#     Passenger(0, 23.0, 1, 1, 'a'),
#     Passenger(0, 24.0, 1, 1, 'b'),
#     Passenger(0, 25.0, 1, 1, 'c')
# ]
# ex = Passenger(0, 22.0, 1, 1, 'd')
# kNearest, distances = findKNearest(ex, example_set, 2)
# for i in range(len(kNearest)) :
#     print(str(kNearest[i]) + " || dist :"+str(distances[i]))


def KNearestClassify(training, testSet, label, k):
    """Assumes training & testSet lists of examples, k an int
       Predicts whether each example in testSet has label
       Returns number of true positives, false positives,
          true negatives, and false negatives

    观看      numMatch > k // 2:  可以猜出这个分类是个 2分类，因为这是个充分条件，换句话来说，力度比较大了
    下面是交叉验证实验中  的 一次Trial。
    根据  KNN 算法,  如果最近的 K 个 大部分是 Label，那么认为 test_case 的label也是  Label，即上面的参数 label。
    反之，则认为不是Label。
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for testCase in testSet:
        nearest, distances = findKNearest(testCase, training, k)
        # conduct vote
        numMatch = 0
        for i in range(len(nearest)):
            if nearest[i].getLabel() == label:
                numMatch += 1
        if numMatch > k // 2:  # guess label
            if testCase.getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:  # guess not label
            if testCase.getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg


def leaveOneOut(examples, method, toPrint=True):
    """
     留一法，适用于数据较少时候适用。
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(examples)):
        testCase = examples[i]
        trainingData = examples[0:i] + examples[i + 1:]
        results = method(trainingData, [testCase])
        truePos += results[0]
        falsePos += results[1]
        trueNeg += results[2]
        falseNeg += results[3]
    if toPrint:
        getStats(truePos, falsePos, trueNeg, falseNeg)
    return truePos, falsePos, trueNeg, falseNeg


def split80_20(examples):
    """
    随机取样，按 80/20 占比取 训练集和测试集。
    最开始的随机取样是   随机取索引。据说是为了效率
    """
    sampleIndices = random.sample(range(len(examples)),
                                  len(examples) // 5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet


def randomSplits(examples, method, numSplits, toPrint=True):
    """

    :param examples:
    :param method:
    :param numSplits: 重复随机取样的次数
    :param toPrint:
    :return:

    重复随机取样方法，适用于数据较多的额时候。下面要除以次数，是因为毕竟从定义上。
    重复随机取样方法，就是将一个方法执行多次，当然了我个人觉得除不除无所谓。
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    random.seed(0)
    for t in range(numSplits):
        trainingSet, testSet = split80_20(examples)
        results = method(trainingSet, testSet)
        truePos += results[0]
        falsePos += results[1]
        trueNeg += results[2]
        falseNeg += results[3]
    getStats(truePos / numSplits, falsePos / numSplits,
             trueNeg / numSplits, falseNeg / numSplits, toPrint)
    return truePos / numSplits, falsePos / numSplits, \
           trueNeg / numSplits, falseNeg / numSplits


# 这个真的是太妙了！ 解决了方法不一致的问题
knn = lambda training, testSet: \
    KNearestClassify(training, testSet,
                     'Survived', 3)
# numSplits = 10
# print('Average of', numSplits,
#      '80/20 splits using KNN (k=3)')
# truePos, falsePos, trueNeg, falseNeg =\
#      randomSplits(examples, knn, numSplits)
#
# print('Average of LOO testing using KNN (k=3)')
# truePos, falsePos, trueNeg, falseNeg =\
#      leaveOneOut(examples, knn)

import sklearn.linear_model


def buildModel(examples, toPrint=True):
    featureVecs, labels = [], []
    for e in examples:
        featureVecs.append(e.getFeatures())
        labels.append(e.getLabel())
    LogisticRegression = sklearn.linear_model.LogisticRegression
    # 直接调用库,并拿到训练好的模型
    model = LogisticRegression().fit(featureVecs, labels)
    if toPrint:
        print('model.classes_ =', model.classes_)  # model.classes_ = ['Died' 'Survived']参考buildModel.png
        for i in range(len(model.coef_)):
            print('For label', model.classes_[1])  # Survived
            for j in range(len(model.coef_[0])):  # 训练好的系数
                print('   ', Passenger.featureNames[j], '=',
                      model.coef_[0][j])
    return model


# L = [x*x for x in range(10)]
# print(L)
# L = [x*x for x in range(10) if x%2 == 0]
# print(L)

def applyModel(model, testSet, label, prob=0.5):
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        # prob是一个标准，如果结果是大于prob,那么被认为是label（形式参数），反之认为不是label。
        # prob[i][1] 中i表示第i个测试样本,1表示positive。参考applyModel.png
        # 但事实上，应该不能这么算 这里的1碰巧对应的positive的坐标。而与label没什么关系。
        #
        label_index = -1
        if label in model.classes_:
            label_index = list(model.classes_).index(label)
        else:
            raise ValueError("Wrong Label")

        if probs[i][label_index] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg


def lr(trainingData, testData, prob=0.5):
    """
     逻辑回归方法，训练模型，测试模型，并返回混淆矩阵中的所有结果。
    """
    model = buildModel(trainingData, False)
    results = applyModel(model, testData, 'Survived', prob)
    return results


# random.seed(0)
# numSplits = 10
# print('Average of', numSplits, '80/20 splits LR')
# truePos, falsePos, trueNeg, falseNeg =\
#      randomSplits(examples, lr, numSplits)
#
# print('Average of LOO testing using LR')
# truePos, falsePos, trueNeg, falseNeg =\
#      leaveOneOut(examples, lr)

"""
查看weights
"""
# # Look at weights
# trainingSet, testSet = split80_20(examples)
# model = buildModel(trainingSet, True)

"""
改变不同P（threshold）
"""


##Look at changing prob
# random.seed(0)
# trainingSet, testSet = split80_20(examples)
# model = buildModel(trainingSet, False)
# print('Try p = 0.1')
# truePos, falsePos, trueNeg, falseNeg = \
#     applyModel(model, testSet, 'Survived', 0.1)
# getStats(truePos, falsePos, trueNeg, falseNeg)
# print('Try p = 0.9')
# truePos, falsePos, trueNeg, falseNeg = \
#     applyModel(model, testSet, 'Survived', 0.9)
# getStats(truePos, falsePos, trueNeg, falseNeg)


def buildROC(trainingSet, testSet, title, plot=True):
    model = buildModel(trainingSet, True)
    xVals, yVals = [], []
    p = 0.0
    while p <= 1.0:
        truePos, falsePos, trueNeg, falseNeg = \
            applyModel(model, testSet,
                       'Survived', p)
        xVals.append(1.0 - specificity(trueNeg, falsePos))
        yVals.append(sensitivity(truePos, falseNeg))
        p += 0.01
    auroc = sklearn.metrics.auc(xVals, yVals)
    if plot:
        pylab.plot(xVals, yVals)
        pylab.plot([0, 1], [0, 1])
        title = title + '\nAUROC = ' + str(round(auroc, 3))
        pylab.title(title)
        pylab.xlabel('1 - specificity')
        pylab.ylabel('Sensitivity')
        pylab.xlim(0.0, 1.0)
        pylab.ylim(0.0, 1.0)
    return auroc


"""
查看ROC曲线
"""
# random.seed(0)
# trainingSet, testSet = split80_20(examples)
# buildROC(trainingSet, testSet, 'ROC for Predicting Survival, 1 Split')
# pylab.show()
