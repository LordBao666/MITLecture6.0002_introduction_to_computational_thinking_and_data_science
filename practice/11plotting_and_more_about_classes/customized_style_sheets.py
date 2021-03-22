"""
@Author  : Lord_Bao
@Date    : 2021/3/22

"""
import pylab

"""
MIT 提供的风格设置
"""


def initialize_plot_style():
    # set line width
    pylab.rcParams['lines.linewidth'] = 4
    # set font size for titles
    pylab.rcParams['axes.titlesize'] = 20
    # set font size for labels on axes
    pylab.rcParams['axes.labelsize'] = 20
    # set size of numbers on x-axis
    pylab.rcParams['xtick.labelsize'] = 16
    # set size of numbers on y-axis
    pylab.rcParams['ytick.labelsize'] = 16
    # set size of ticks on x-axis
    pylab.rcParams['xtick.major.size'] = 7
    # set size of ticks on y-axis
    pylab.rcParams['ytick.major.size'] = 7
    # set size of markers, e.g., circles representing points
    pylab.rcParams['lines.markersize'] = 10
    # set number of times marker is shown when displaying legend
    pylab.rcParams['legend.numpoints'] = 1

    # return pylab
