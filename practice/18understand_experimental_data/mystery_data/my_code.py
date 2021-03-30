"""
@Author  : Lord_Bao
@Date    : 2021/3/28

"""
import pylab


def label_plot():
    pylab.title('Mystery Data')
    pylab.xlabel('X')
    pylab.ylabel('Y')


def getData(file_name):
    x_vals = []
    y_vals = []

    with open(file_name, 'r') as  data_file:
        data_file.readline()  # discard header
        for line in data_file:
            x, y = line.split()
            x_vals.append(float(x))
            y_vals.append(float(y))

    # 参考mysteryData.txt，我觉得x和y是反的
    return y_vals, x_vals


def get_coefficient_of_determination(real_y_vals, predicted_y_vals):
    """
    :param real_y_vals: ndarray
    :param predicted_y_vals:ndarray
    :return: ndarray
    """
    mean_error = ((real_y_vals - predicted_y_vals) ** 2).sum() / len(real_y_vals)
    variance = pylab.var(real_y_vals)
    return 1 - (mean_error / variance)


def fitData(file_name, polynomial_degrees, to_print=False):
    """

    :param to_print: 是否打印决定系数和平方误差
    :param file_name:  实验数据文件名
    :param polynomial_degrees: 预拟合模型的多项式系数，e.g(1,2,4,8,16)
    :return:
    """
    x_vals, y_vals = getData(file_name)
    # 处理成array,将来作为实际参数传到polyfit
    x_vals = pylab.array(x_vals)
    y_vals = pylab.array(y_vals)

    """绘制实验得到的数据"""
    pylab.plot(x_vals, y_vals, 'bo',
               label='Measured points')
    label_plot()

    for degree in polynomial_degrees:
        # polyfit函数会（针对线性回归）返回平方误差最小的元组,model.e.g ，当degree为1时,返回a,b
        model = pylab.polyfit(x_vals, y_vals, degree)
        est_y_vals = pylab.polyval(model, x_vals)  # 根据model 和 自变量,预估因变量
        coefficient_of_determination = get_coefficient_of_determination(y_vals, est_y_vals)
        pylab.plot(x_vals, est_y_vals,
                   label='Degree of  ' + str(degree) + ",R2:"
                         + str(round(coefficient_of_determination, 4)))
        if to_print:
            variance = ((y_vals - est_y_vals) ** 2).sum()
            print("多项式次数 " + str(degree) + "平方误差=" + str(round(variance, 4))
                  + ";决定系数=" + str(round(coefficient_of_determination, 4)))

    pylab.legend(loc='best')
    pylab.show()


# 查看 result.png
fitData("mysteryData.txt", (1, 2, 4, 8,16), True)
