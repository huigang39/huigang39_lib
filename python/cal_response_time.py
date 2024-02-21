"""
@Author: Huigang Wang
@Email: huigang39@outlook.com
@Date: 2024-2-21 11:00
@Description: 计算 FreeMaster 采集数据的响应时间
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def importData(filename):
    data = pd.read_table(filename)
    return data


def dataClean(data):
    data = data.rename(columns={"# Time [sec]": "Time [sec]"})
    data = data.drop(data.index[0])
    data = data.reset_index(drop=True)
    data = data.astype(float)
    return data


def calResponseTime(ref, feedback, time):
    # 计算交叉相关
    corr = np.correlate(ref, feedback, "full")

    # 找到最大相关索引
    delay = corr.argmax() - (len(time) - 1)

    # 获取采样频率
    fs = 1 / (time[1] - time[0])

    # 计算响应时间
    responseTime = delay / fs

    return responseTime


if __name__ == "__main__":
    pass
