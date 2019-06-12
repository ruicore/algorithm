# LeetCode 304. Range Sum Query 2D - Immutable

## Description

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

```py
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

## 描述

给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。

Range Sum Query 2D
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:

```py
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```

说明:

你可以假设矩阵不可变。
会多次调用 sumRegion 方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2。

### 思路

* 这道题目使用动态规划.
* 状态：我们声明一个同给定数组一样大小的二维矩阵self.sum，self.sum的每个位置的值self.sum\[i]\[j]表示给定矩阵从matrix\[0]\[0]到matrix\[i]\[j]构成的矩阵的和.
* 转移方程：我们用temp记录第matirx第i行的前j个数的和，则self.sum\[i]\[j] = temp+self.sum\[i-1]\[j]
* 答案，area3 - area1 - area2.如下图
![LeetCode 304. Range Sum Query 2D - Immutable](![LeetCode 304. Range Sum Query 2D - Immutable]())

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-11 09:27:14
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-11 10:09:38


class NumMatrix:
    def __init__(self, matrix: 'List[List[int]]'):
        # 如果矩阵为空，则记录和的矩阵也置为空
        if not matrix:
            self.sum = [[]]
        else:
            # 矩阵的行数，矩阵的列数
            self.row, self.col = len(matrix), len(matrix[0])
            # self.sum 值self.sum[i][j]表示matrix[0][0]到matrix[i][j]构成矩阵的所有值的和
            self.sum = [[matrix[0][0]] * self.col for _ in range(self.row)]
            # 初始化第一行
            for i in range(1, self.col):
                self.sum[0][i] = self.sum[0][i - 1] + matrix[0][i]
            # 初始化第一列
            for i in range(1, self.row):
                self.sum[i][0] = self.sum[i - 1][0] + matrix[i][0]
            # 填充矩阵的每一个位置
            for i in range(1, self.row):
                temp = matrix[i][0]
                for j in range(1, self.col):
                    temp += matrix[i][j]
                    self.sum[i][j] = self.sum[i - 1][j] + temp

    def sumRegion(self, row1: 'int', col1: 'int', row2: 'int',col2: 'int') -> 'int':
        # 面积1为给定矩阵右下角和matirx[0][0]构成的矩阵
        area1 = self.sum[row2][col2]
        # 面积2为左侧空出来的矩阵
        area2 = self.sum[row2][col1 - 1] if col1 > 0 else 0
        # 面积3为上侧空出来的矩阵，去掉和面积2重叠的部分
        area3 = 0
        if col1 == 0 and row1 != 0: area3 = self.sum[row1 - 1][col2]
        elif row1 != 0 and col1 != 0:
            area3 = self.sum[row1 - 1][col2] - self.sum[row1 - 1][col1 - 1]
        return area1 - area2 - area3
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-11-304-Range-Sum-Query-2D-Immutable.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-304-range-sum-query-2d---immutable/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
