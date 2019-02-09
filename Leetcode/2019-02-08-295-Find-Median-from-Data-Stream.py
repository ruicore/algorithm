# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 13:58:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 13:58:09

# 二分搜索库
import bisect


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 声明一个数组
        self.list = []
        # 数组中元素的个数
        self.count = 0

    def addNum(self, num: 'int') -> 'None':
        # 将元素个数自增一次
        self.count += 1
        # 插入新元素
        bisect.insort_left(self.list, num)

    def findMedian(self) -> 'float':
        # 如果是奇数，返回中间值
        if self.count % 2:
            return self.list[self.count // 2]
        else:
            # 如果是偶数，返回中间两个数的平均值
            num1 = self.count // 2
            return (self.list[num1] + self.list[num1 - 1]) / 2
