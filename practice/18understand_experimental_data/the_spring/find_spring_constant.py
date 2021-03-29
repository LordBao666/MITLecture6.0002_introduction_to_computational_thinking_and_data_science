"""
@Author  : Lord_Bao
@Date    : 2021/3/29

"""
import pylab


def labelPlot():
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    pylab.legend(loc="best")


def getData(file_name):
    x_vals = []
    y_vals = []

    with open(file_name, 'r') as data_file:
        data_file.readline()  # discard header
        for line in data_file:
            x, y = line.split()
            x_vals.append(float(x))
            y_vals.append(float(y))

    # 参考mysteryData.txt，我觉得x和y是反的
    return x_vals, y_vals


def find_constant_of_spring(file_name):
    pylab.figure()
    x_vals, y_vals = getData(file_name)
    # ndarry
    distances = pylab.array(x_vals)
    mass = pylab.array(y_vals)
    force = mass * 9.81
    print(force)
    model = pylab.polyfit(force, distances, 1)
    est_distances = pylab.polyval(model, force)
    pylab.plot(force, distances, 'og',
               label='Measured points')
    # 弹簧系数
    k = round(1 / model[0], 4)
    pylab.plot(force, est_distances, label="Liner estimate,k=" + str(k))
    labelPlot()


find_constant_of_spring("springData.txt")
find_constant_of_spring("springData2.txt")

pylab.show()