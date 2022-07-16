# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:51:56 2022

@author: 15149
"""
# import numpy as np

from numpy import poly1d, polyfit, corrcoef, array


def Polyfit(x, y, deg=1):
    import matplotlib.pyplot as plt
    # from seaborn import set
    # import pandas as pd

    # set()
    # 以上为预设，非必要
    plt.scatter(x, y)
    model = poly1d(polyfit(x, y, deg))
    # r = pd.DataFrame(corrcoef(x, y))
    r = corrcoef(x, y)
    plt.plot(x, model(x))
    plt.title(str(model) +
              '\nCorrelation coefficient \n(take rows in order as new rows, first-order correlation, multi-order ignore)\n'+str(r))
    plt.show()
    return model, r


if __name__ == '__main__':

    # import matplotlib.pyplot as plt

    # # 支持中文
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # from matplotlib import rc
    # font = {'family': 'SimHei', "size": 24}
    # rc('font', **font)  # 一次定义终身使用
    # from gethtml.gethtmlbypyppeteer import gethtmlbypyppteer
    # f = hehe(n=1)
    print('输入样式：\n[0.0048965,0.009793,0.0146895,0.019586,0.0244825,0.029379,0.0342755]\n[12.5,25.1,38.4,51.5,66.6,79.5,91.5]\n1\n')
    x = input('x\n')
    y = input('y\n')
    deg = input('deg(拟合阶数)\n')
    x = array(eval(x))
    y = array(eval(y))
    deg = int(deg)
    # print(x, y, deg)
    print(Polyfit(x, y, deg))
    input("input for out")
