# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""


class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """

    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            # city - > year -> month - > day  疯狂嵌套的字典
            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature

        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]


def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y) ** 2).sum()
    var_x = ((x - x.mean()) ** 2).sum()
    SE = pylab.sqrt(EE / (len(x) - 2) / var_x)
    return SE / model[0]


"""
End helper code
"""


def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    list_of_coefficients_for_degs = []
    for deg in degs:
        model = pylab.polyfit(x, y, deg)
        list_of_coefficients_for_degs.append(model)
    return list_of_coefficients_for_degs


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    mean = y.sum() / len(y)
    numerator = ((y - estimated) ** 2).sum()
    denominator = ((y - mean) ** 2).sum()
    return 1 - (numerator / denominator)


def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        pylab.figure()

        predicted_vals = pylab.polyval(model, x)
        R2 = r_squared(y, predicted_vals)
        poly = len(model) - 1

        # 处理title,当维度为1 ,即 y =ax + b时,title需添加 Ratio of SE
        title = None
        if poly == 1:
            ratio_of_se = se_over_slope(x, y, predicted_vals, model)
            title = "Polynomial " + str(poly) + ":R2=" + str(round(R2, 4)) + "\nRatio of SE=" + str(
                round(ratio_of_se, 4))
        else:
            title = "Polynomial " + str(poly) + ":R2=" + str(round(R2, 4))
        pylab.title(title)
        pylab.xlabel("years")
        pylab.ylabel("degrees Celsius")
        pylab.plot(x, y, '.b', label="Origin Data")
        pylab.plot(x, predicted_vals, color="red", label="Predicted Value Under Polynomial " + str(poly))
        pylab.legend(loc="best")

    pylab.show()


def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    temperatures = []
    for year in years:
        temp_cur_year = []
        for city in multi_cities:
            temps = climate.get_yearly_temp(city, year)
            # 加入 该city 于 该year的平均温度
            temp_cur_year.append(temps.sum() / len(temps))
        # 加入所以城市的平均温度
        temperatures.append(sum(temp_cur_year) / len(temp_cur_year))
    return pylab.array(temperatures)


def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    # 不破坏原来的y ndarry
    y_copy = y.copy()
    len_y = len(y_copy)

    if len_y < window_length:
        result = []
        for i in range(len_y):
            # 获取 y_copy的前i个子集
            sub_set = y_copy[:i + 1]
            result.append(sub_set.sum() / len(sub_set))
        return pylab.array(result)
    else:
        first_part = []
        second_part = []
        for i in range(window_length):
            # 获取 y_copy的前i个元素的子集
            sub_set = y_copy[:i + 1]
            first_part.append(sub_set.sum() / len(sub_set))
        for i in range(window_length, len(y_copy)):
            # 获取 [y[i-2],y[i-1],y[i]]
            sub_set = y_copy[i - window_length + 1:i + 1]
            second_part.append(sub_set.sum() / len(sub_set))
        first_part.extend(second_part)
        return pylab.array(first_part)


def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    n = len(y)
    result = (((y - estimated) ** 2).sum() / n) ** 0.5
    return result


def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """

    def get_std(temps):
        mean = sum(temps) / len(temps)
        result = 0
        for temp in temps:
            result += (temp - mean) ** 2
        return (result / len(temps)) ** 0.5

    temperatures = []
    for year in years:
        temp_cur_year = []
        for city in multi_cities:
            temps = climate.get_yearly_temp(city, year)
            # 加入该city当年的所有温度
            temp_cur_year.append(list(temps))

        avg_temp_cur_year = []
        # 计算每天各城市的平均温度
        for i in range(len(temp_cur_year[0])):
            temp = 0
            for j in range(len(temp_cur_year)):
                temp += temp_cur_year[j][i]
            avg_temp_cur_year.append(temp / len(temp_cur_year))

        temperatures.append(get_std(avg_temp_cur_year))
    return pylab.array(temperatures)


def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        pylab.figure()

        predicted_vals = pylab.polyval(model, x)
        RMSE = rmse(y, predicted_vals)
        poly = len(model) - 1

        # 处理title,添加RMSE
        title = "Polynomial " + str(poly) + ":RMSE=" + str(round(RMSE, 4))

        pylab.title(title)
        pylab.xlabel("years")
        pylab.ylabel("degrees Celsius")
        pylab.plot(x, y, '.b', label="Origin Data")
        pylab.plot(x, predicted_vals, color="red", label="Predicted Value Under Polynomial " + str(poly))
        pylab.legend(loc="best")

    pylab.show()


if __name__ == '__main__':
    pass

    # Part A.4_1
    # climate = Climate("data.csv")
    # train_x_data = TRAINING_INTERVAL
    # train_y_data = []
    # city = 'NEW YORK'
    # month = 1
    # day = 10
    # for year in train_x_data:
    #     temperature = climate.get_daily_temp(city, month, day, year)
    #     train_y_data.append(temperature)
    # train_x_data = pylab.array(train_x_data)
    # train_y_data = pylab.array(train_y_data)
    # models = generate_models(train_x_data, train_y_data, (1, ))
    # evaluate_models_on_training(train_x_data, train_y_data, models)

    # Part A.4_2
    # climate = Climate("data.csv")
    # train_x_data = TRAINING_INTERVAL
    # train_y_data = []
    # city = 'NEW YORK'
    # for year in train_x_data:
    #     temperatures = climate.get_yearly_temp(city, year)
    #     mean_temperature = temperatures.sum() / len(temperatures)
    #     train_y_data.append(mean_temperature)
    # train_x_data = pylab.array(train_x_data)
    # train_y_data = pylab.array(train_y_data)
    # models = generate_models(train_x_data, train_y_data, (1,))
    # evaluate_models_on_training(train_x_data, train_y_data, models)

    # Part B
    # climate = Climate("data.csv")
    # train_x_data = pylab.array(TRAINING_INTERVAL)
    # train_y_data = gen_cities_avg(climate, CITIES, list(TRAINING_INTERVAL))
    #
    # models = generate_models(train_x_data, train_y_data, (1,))
    # evaluate_models_on_training(train_x_data, train_y_data, models)
    # Part C
    # climate = Climate("data.csv")
    # train_x_data = pylab.array(TRAINING_INTERVAL)
    # window_length = 5
    # national_avg_temp_per_year = gen_cities_avg(climate, CITIES, list(TRAINING_INTERVAL))
    # train_y_data = moving_average(national_avg_temp_per_year, window_length)
    # models = generate_models(train_x_data, train_y_data, (1,))
    # evaluate_models_on_training(train_x_data, train_y_data, models)

    # Part D.2
    # climate = Climate("data.csv")
    # train_x_data = pylab.array(TRAINING_INTERVAL)
    # window_length = 5
    # train_national_avg_temp_per_year = gen_cities_avg(climate, CITIES, list(TRAINING_INTERVAL))
    # # 获取y的训练集
    # train_y_data = moving_average(train_national_avg_temp_per_year, window_length)
    # models = generate_models(train_x_data, train_y_data, (1, 2, 20))
    """
    训练集评估模型
    """
    # evaluate_models_on_training(train_x_data, train_y_data, models)

    """
    测试集评估模型
    """
    # test_x_data = pylab.array(TESTING_INTERVAL)
    # test_national_avg_temp_per_year = gen_cities_avg(climate, CITIES, list(TESTING_INTERVAL))
    # test_y_data = moving_average(test_national_avg_temp_per_year, window_length)
    # evaluate_models_on_testing(test_x_data, test_y_data, models)

    # Part E
    # TODO: replace this line with your code
    climate = Climate("data.csv")
    std_devs = gen_std_devs(climate, CITIES, list(TRAINING_INTERVAL))

    train_x_data = pylab.array(TRAINING_INTERVAL)
    window_length = 10

    # 获取y的训练集
    train_y_data = moving_average(std_devs, window_length)
    models = generate_models(train_x_data, train_y_data, (1, 2, 3))
    evaluate_models_on_training(train_x_data, train_y_data, models)
