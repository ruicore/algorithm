# LeetCode 149. Max Points on a Line

## Description


Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

```python
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
```

Example 2:

```python
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
```

## 描述

给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

```python
输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
```
示例 2:

```python
输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
```
### 思路

* 我们使用双重循环，使用斜率来统计有多少个点出现在同一条直线上.
* 基本思路是：以斜率为键，以点为值，键对应的值中最大值即为在一条线上的最多点数.
* 要注意的是，我们不能直接用数学上的"斜率"作为键，因为在坐标非常大并且两个点非常接近的时候，如A(x,y),B(x+1,y+1),会因为计算精度问题而认为B点在A点和原点(0,0)构成的直线上.
* 为了解决这个问题我们以坐标为键.
* 同时还要注意的是平行和垂直的情况.
* 我们每次以一个点为基本点，称此点为pivot,将pivot后面的点与pivot构成直线，计算斜率，统计每个斜率出现了多少次，该趟循环取最大值为本趟结果，重复n-1次（n为节点个数.
* 还要注意相同的点，如果一个点与pivot坐标相同，我们不用进行斜率计算，直接计算出现了多少次重复，最后在比较的时候加上重复的值即可.

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-14-149-Max-Points-on-a-Line.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-149-max-points-on-a-line/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
