"""
@Author  : Lord_Bao
@Date    : 2021/3/20

"""

import pylab
import customized_style_sheets

# ### 说到底 pylab 和 tmp都是同一个脚本,所以这里返回True
# tmp = customized_style_sheets.initialize_plot_style()
# print(tmp == pylab)


pylab.figure(1)  # create figure 1
pylab.plot([1, 2, 3, 4], [1, 7, 3, 5])  # draw on  figure 1
pylab.show()  # show figure1  on screen

# pylab.figure(1)  # 创建figure1,current figure 为 1
# pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])
# pylab.figure(2)  # 创建figure2,current figure 为 2
# pylab.plot([1, 4, 2, 3], [5, 6, 7, 8])
# pylab.savefig("Figure-Addie")  # 保存当前current figure,格式png
# pylab.figure(1)  # 切换到figure1
# pylab.plot([5, 6, 10, 3])  # 只传一个序列,那么代表是y值。 x值默认是 range(len(y序列))
# pylab.savefig("Figure-Jane")