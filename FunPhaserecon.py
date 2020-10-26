# -*- coding:utf-8 -*-
# @Time : 2020/9/30 8:30
# @Author: Li Pengtao
# @Note：

import numpy as np
import math
import cv2


# *******************************
# 解包裹
# *******************************
def unpack(inputfile):
    '''
    :param inputfilr:
    :return: 解包裹数值结果
    '''
    raw_img = cv2.imread(inputfile, cv2.IMREAD_GRAYSCALE)  # 读取图像灰度值

    n_row = raw_img.shape[0]
    n_col = raw_img.shape[1]

    a = np.asarray(raw_img)  # 转为矩阵

    x = math.ceil(n_row / 2)  # 向下取整
    y = math.ceil(n_col / 2)

    p = np.zeros((n_row, n_col))
    k = np.zeros((n_row, n_col))
    f = np.zeros((n_row, n_col))
    z = np.zeros((n_row, n_col))
    g = np.zeros((n_row, n_col))

    p[x][y] = 0  # 中心点设为0

    h = y + 5
    if h < (x + 5):
        h = x + 5

    # 上面
    for i in range(h):
        for j in range(y - i + 2, y + i - 1):  # 2*i-2
            if x - i+1 >= 0 and n_col >= j >= 0:
                if k[x - i + 1][j] != 1:
                    if int(a[x - i + 1][j]) - int(a[x - i + 2][j]) > 192:
                        p[x - i + 1][j] = p[x - i + 2][j] - 1
                    elif int(a[x - i + 2][j]) - int(a[x - i + 1][j]) > 192:
                        p[x - i + 1][j] = p[x - i + 2][j] + 1
                    else:
                        p[x - i + 1][j] = p[x - i + 2][j]
                    f[x - i ][j] = 1

        # 下面
        for j in range((y - i + 2), (y + i - 1)):
            if (x + i - 1) < n_row and n_col >= j >= 0:
                if f[x + i - 1][j] != 1:
                    if int(a[x + i - 1][j]) - int(a[x + i - 2][j]) > 192:
                        p[x + i - 1][j] = p[x + i - 2][j] - 1
                    elif int(a[x + i - 2][j]) - int(a[x + i - 1][j]) > 192:
                        p[x + i - 1][j] = p[x + i - 2][j] + 1
                    else:
                        p[x + i - 1][j] = p[x + i - 2][j]
                    f[x + i - 1][j] = 1

        # 左边
        for j in range(x - i + 1, x + i):
            if y - i + 1 >= 0 and n_row > j >= 0:
                if f[j][y - i + 1] != 1:
                    if int(a[j][y - i + 1]) - int(a[j][y - i + 2]) > 192:
                        p[j][y - i + 1] = p[j][y - i + 2] - 1
                    elif int(a[j][y - i + 2]) - int(a[j][y - i + 1]) > 192:
                        p[j][y - i + 1] = p[j][y - i + 2] + 1
                    else:
                        p[j][y - i + 1] = p[j][y - i + 2]
                    f[j][y - i + 1] = 1

        # 右边
        for j in range(x - i + 1, x + i):
            if y + i - 1 < n_col and n_row > j >= 0:
                if k[j][y + i - 1] != 1:
                    if int(a[j][y + i - 1]) - int(a[j][y + i - 2]) > 192:
                        p[j][y + i - 1] = p[j][y + i - 2] - 1
                    elif int(a[j][y + i - 2]) - int(a[j][y + i - 1]) > 192:
                        p[j][y + i - 1] = p[j][y + i - 2] + 1
                    else:
                        p[j][y + i - 1] = p[j][y + i - 2]
                    f[j][y + i - 1] = 1

    for i in range(n_row):
        for j in range(n_col):
            z[i][j] = int(a[i][j]) + 225 * p[i][j]

    return z, a


# ****************************
# 重构函数
# ****************************
def reconstraction(upresults, s, d):
    '''

    :return:
    '''
    n_row = upresults.shape[0]
    n_col = upresults.shape[1]

    results = np.zeros((n_row, n_col))
    for y in range(n_row):
        for x in range(n_col):
            if x in range(s):
                results[y][x] = upresults[y][x]
            if x in range(s, 2 * s):
                results[y][x] = results[y][x - s] + upresults[y][x] - 25


            if x in range(2 * s, n_col):
                results[y][x] = 2 * results[y][x - s] - results[y][x - 2 * s] + (upresults[y][x] - upresults[y][x - s])

    return results  # data type: ndarray


# *************************************
# 计算图像的前s列
# *************************************
def img_s_median(s, img_mat, n_row):
    '''
    :param s:执行重构时输入的s值
    :param img_mat: 图像灰度值矩阵
    :param n_row: 图像的行数
    :return: 图像前s列的中位数
    '''
    img_s_arrary = []

    for i in range(n_row):
        for k in range(s):
            img_s_arrary.append(img_mat[i][k])

    s_median = np.median(img_s_arrary)

    return 255 - s_median


# 归一化 0-255
def normalization(x, x_min, x_max):
    nor_x = (x - x_min) / ((x_max - x_min))
    return int(nor_x * 255)
