# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-14 12:14:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-14 15:36:07

import fractions


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # 如果为空返回0
        if not points:
            return 0
        res, nums = 1, len(points)
        # 遍历所有的线段，以points[i]为起点
        for i in range(nums - 1):
            # dict用于存储该斜率的点一共出现了多少次
            slopedict = dict()
            # 以当前节点为起始节点
            pivot = points[i]
            # 统计和当前节点相同的节点，不包括pivot节点本身.
            duplicate = 0
            for j in range(i + 1, nums):
                # 如果和此节点相同，则不用计算斜率
                if pivot.x == points[j].x and pivot.y == points[j].y:
                    duplicate += 1
                else:
                    # 当前斜率的点数目加一，如果当前斜率不存在，其默认值为1（即pivot本身）
                    slope = self.slope(slopedict, pivot, points[j])
                    slopedict[slope] = slopedict.get(slope, 1) + 1
            # 如果都是相同的点，则字典为空
            # 如果在字典不为空的情况下
            if slopedict:
                # 最大值为斜率次数最多的点加上与pivot相同的节点
                res = max(res, max(slopedict.values()) + duplicate)
            # 如果都是相同的节点，则最大值为相同的节点数目加一
            else:
                res = max(res, duplicate + 1)
            del slopedict
        return res

    def slope(self, slopedict, one, two):
        # 在这里斜率不能用一个值表示，因为当数据非常大做除法时，精度会导致相近的点变成同一个点
        # 我们以元组（x，y）横纵左边来表示斜率
        if one.y == two.y:
            return (0, one.y)
        if one.x == two.x:
            return (one.x, 0)
        x, y = two.x - one.x, two.y - one.y
        # 用x，y除以其最大公因数，得到的结果最为坐标元组，即字典的key.
        cfactor = fractions.gcd(x, y)
        return (x // cfactor, y // cfactor)
