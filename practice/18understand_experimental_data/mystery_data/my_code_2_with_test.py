"""
@Author  : Lord_Bao
@Date    : 2021/3/30

"""
import pylab


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


def build_models(train_data_file_name, polynomial_degrees):
    """

    :param train_data_file_name:  训练数据文件名
    :param polynomial_degrees: 预拟合模型的多项式系数，e.g(1,2,4,8,16)
    :return: 根据不同维度训练好的模型
    """
    x_vals, y_vals = getData(train_data_file_name)
    # 处理成array,将来作为实际参数传到polyfit
    x_vals = pylab.array(x_vals)
    y_vals = pylab.array(y_vals)

    models = []

    for degree in polynomial_degrees:
        model = pylab.polyfit(x_vals, y_vals, degree)
        models.append(model)
    return models


def test_model(test_data_file_name, models):
    """
    :param test_data_file_name: 测试文件名
    :param models: 训练好的模型
    :return:
    """
    """绘制实验得到的数据"""
    x_vals, y_vals = getData(test_data_file_name)
    # 处理成array,将来作为实际参数传到polyVal
    x_vals = pylab.array(x_vals)
    y_vals = pylab.array(y_vals)

    pylab.plot(x_vals, y_vals, 'bo',
               label='Measured points')

    for model in models:
        est_y_vals = pylab.polyval(model, x_vals)
        R2 = round(get_coefficient_of_determination(y_vals, est_y_vals), 4)
        label = "Degree of " + str(len(model) - 1) + ", R2=" + str(R2)
        pylab.plot(x_vals, est_y_vals, label=label)

    pylab.title('Model Performance for test data: ' + str(test_data_file_name))
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.legend(loc='best')
    pylab.show()


def get_total_date(file_names):
    total_x_vals = []
    total_y_vals = []
    for file_name in file_names:
        x_vals, y_vals = getData(file_name)
        total_x_vals.extend(x_vals)
        total_y_vals.extend(y_vals)
    return total_x_vals, total_y_vals


def leave_one_out_model(file_names, degrees, to_print):
    """
    :param to_print: 是否打印每个维度的平均R2
    :param file_names: 所有实验数据文件名.list 或 tuple皆可，比如 ["Dataset 1.txt","Dataset 2.txt"]
    :param degrees:测试维度
    :return:
    """
    x_vals, y_vals = get_total_date(file_names)

    SE = [0] * len(degrees)
    # 共计n次
    for i in range(len(x_vals)):
        """
            留一法,取样本中的一份做为测试数据,另外数据作为训练数据，设评估结果为p.然后取p的平均。
        """
        SE_for_this_trial = []

        for degree in degrees:
            x_vals_copy = x_vals[:]
            y_vals_copy = y_vals[:]
            test_x_val = pylab.array(x_vals_copy.pop(i))
            test_y_val = y_vals_copy.pop(i)
            train_x_vals = pylab.array(x_vals_copy)
            train_y_vals = pylab.array(y_vals_copy)
            model = pylab.polyfit(train_x_vals, train_y_vals, degree)
            # 如果传入的ndarry的大小是1的话,est_y_val就是一个数字，而不是ndarry
            est_y_val = pylab.polyval(model, test_x_val)
            SE_for_this_trial.append((est_y_val - test_y_val) ** 2)
        for j in range(len(SE)):
            SE[j] += SE_for_this_trial[j]

    if to_print:
        for index in range(len(degrees)):
            print("Degree of " + str(degrees[index]) + ",SUM Of SE  = " + str(SE[index]))
    degree_str_list = []
    for degree in degrees:
        # x轴
        degree_str_list.append(str(degree))
    pylab.title("SUM OF SE for Degree" + str(degrees))
    pylab.xlabel("Degree")
    pylab.ylabel("SUM OF SE")
    pylab.plot(degree_str_list, SE)
    pylab.legend(loc="best")
    pylab.show()


if __name__ == '__main__':
    """
    查看 train1test2.png 和 train2test1.png,发现维度应该是在8以内。
    所以测试234567。
    """
    # degrees = (1, 2, 4, 8)
    # models = build_models("Dataset 1.txt", degrees)
    # test_model("Dataset 2.txt", models)
    # models = build_models("Dataset 2.txt", degrees)
    # test_model("Dataset 1.txt", models)

    """
    查看train1test2_for_degree234567.png 和 train2test1_for_degree234567.png
    发现没什么区别。那么可能需要用留出法来测试了。
    """
    # degrees = (2, 3, 4, 5, 6, 7)
    # models = build_models("Dataset 1.txt", degrees)
    # test_model("Dataset 2.txt", models)
    # models = build_models("Dataset 2.txt", degrees)
    # test_model("Dataset 1.txt", models)

    # degrees = ( 2, 4, 8, 16)
    # degrees = (2, 4, 8, 12)
    # degrees = (2, 3, 4, 5, 6, 7, 8)
    # models = build_models("Dataset 1.txt", degrees)
    # test_model("Dataset 2.txt", models)
    # models = build_models("Dataset 2.txt", degrees)
    # test_model("Dataset 1.txt", models)

    # file_names = ["Dataset 1.txt", "Dataset 2.txt"]
    # degrees = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    # leave_one_out_model(file_names, degrees, True)
    # file_names = ["Dataset 3.txt", "Dataset 4.txt"]
    # degrees = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    # leave_one_out_model(file_names, degrees, True)

    models = build_models("Dataset3&4.txt", (2,))
    a = round(models[0][0], 4)
    b = round(models[0][1], 4)
    c = round(models[0][2], 4)
    print("a=" + str(a) + ",b=" + str(b) + ",c=" + str(c))
