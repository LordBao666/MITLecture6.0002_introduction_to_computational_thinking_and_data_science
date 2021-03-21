"""
@Author  : Lord_Bao
@Date    : 2021/3/21

"""
import random

"""
这个module(即这个py文件) 主要包含的是random_walk案例的一些实体类
比如 Drunk Location Field

"""


class Drunk(object):
    """
    所有类型Drunk(如Usual)的基类
    """

    def __init__(self, name="Anonymous"):
        """
        :param name: string。 不取名的话。通通叫Anonymous
        """
        self.name = name

    def __str__(self):
        if (type(self)).__name__ == "Drunk":
            raise NotImplementedError("Drunk类不能存在实例对象,请务必子类调用__str__方法")
        else:
            return (type(self)).__name__ + ":" + self.name

    def take_steps(self):
        raise NotImplementedError("Drunk类不能存在实例对象,请务必子类实现take_steps方法")


class UsualDrunk(Drunk):
    def take_steps(self):
        x_step, y_step = random.choice([(1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -1.0)])
        return x_step, y_step


class SouthDrunk(Drunk):
    def take_steps(self):
        """
        x轴上与UsualDrunk相同。但在y轴上,向y负半轴走的距离大于y正半轴的距离。理解为倾向南方
        """
        x_step, y_step = random.choice([(1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -2.0)])
        return x_step, y_step


class OnlyXDrunk(Drunk):
    def take_steps(self):
        """
        只走X轴,不过相比于其他Drunk ，它是2倍的步距
       """
        x_step, y_step = random.choice([(2.0, 0.0), (-2.0, 0.0)])
        return x_step, y_step


class WestDrunk(Drunk):
    def take_steps(self):
        """
        y轴上与UsualDrunk相同。但在x轴上,向x负半轴走的距离大于x正半轴的距离。理解为倾向西方
       """
        x_step, y_step = random.choice([(1.0, 0.0), (-2.0, 0.0), (0.0, 1.0), (0.0, -1.0)])
        return x_step, y_step


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from(self, other):
        """
        :param other: Location
        :return: self  和 other 之间的距离
        """
        return ((self.x - other.get_x()) ** 2 + (self.y - other.get_y()) ** 2) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Field(object):
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, location):
        """
        :param location:  Location 实例
        :param drunk: Drunk的实例
        """
        if drunk in self.drunks:
            raise ValueError("Duplicate Drunk")
        else:
            self.drunks[drunk] = location

    def get_location(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("drunk not in field")
        else:
            return self.drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("drunk not in field")
        else:
            delta_x, delta_y = drunk.take_steps()
            current_loc = self.drunks[drunk]
            new_loc = current_loc.move(delta_x, delta_y)
            self.drunks[drunk] = new_loc


class OddField(Field):
    """
      模拟传送门
    """

    def __init__(self, num_holes, x_range, y_range):
        """
        :param num_holes: 坑位的个数(传送门的个数)
        :param x_range:  x的范围
        :param y_range: y的范围
        """
        Field.__init__(self)
        self.worm_holes = {}
        for i in range(num_holes):
            from_x = random.randint(-x_range, x_range)
            from_y = random.randint(-y_range, y_range)
            to_x = random.randint(-x_range, x_range)
            to_y = random.randint(-y_range, y_range)
            self.worm_holes[(from_x, from_y)] = Location(to_x, to_y)

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        loc = self.get_location(drunk)
        loc_x = loc.get_x()
        loc_y = loc.get_y()
        if (loc_x, loc_y) in self.worm_holes:
            self.drunks[drunk] = self.worm_holes[loc_x, loc_y]


class StyleIterator(object):
    """
      画图的辅助函数
    """

    def __init__(self, styles):
        """
        :param styles: 能便利的有序数据结构，比如 list tuple。存储元素为string，代表画图风格。比如 ‘b-’
        """
        self.index = 0
        self.styles = styles

    def next_style(self):
        style = self.styles[self.index]
        if self.index != len(self.styles) - 1:
            self.index += 1
        else:
            self.index = 0

        return style
