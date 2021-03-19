"""
@Author  : Lord_Bao
@Date    : 2021/3/19

"""

"""
封装cow的实体类,有两个属性  name(string) , weight(int)详见下文
"""


class Cow(object):
    def __init__(self, name, weight):
        """
        :param name:  cow的姓名,类型string
        :param weight: cow的重量,类型int(>0)
        """
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.name + "->" + str(self.weight)
