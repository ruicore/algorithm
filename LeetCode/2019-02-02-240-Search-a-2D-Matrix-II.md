# LeetCode 240. Search a 2D Matrix II

## Description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

## 描述

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

### 思路

* 我们从矩阵的右上角开始检查.
* 如果当前位置的元素大于target，由于当前列的元素都大于当前位置的元素，说明target不可能在当前列中，我们向左走一列.
* 如果当前位置的元素小于target，由于当前行的所有元素都小于当前位置的元素（当前位置后面的元素不在比较范围之内，因为已经通过刚才的列判断了target不可能在这些列中），说明target不可能在当前行中，我们向下走一行.
* 这样不断向左下走的过程中，如果遇到了target值，返回Ture，如果走到了左下角都没有遇到，返回Fasle.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 13:01:11
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 13:45:27


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        # 从矩阵的右上角开始寻找（左下角也可以）
        # 从右上角开始，如果向左走则所有的元素递减；如果向下走所有的元素递增
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            # 如果相等，返回True
            if matrix[row][col] == target: return True
            # 如果当前位置元素更大，由于当列的元素都大于当前元素
            # 即target不在当前列中，col自减一次
            if matrix[row][col] > target: col -= 1
            # 如果当前位置的元素更小，由于当前元素在行的末尾
            # （当前元素后面的元素已经被列判定给否定了）
            # 当前元素前面的元素前面的元素都小于当前元素
            # 即target不在当前行中，row自增一次
            if matrix[row][col] < target: row += 1
        return False
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-02-240-Search-a-2D-Matrix-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-240-search-a-2d-matrix-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
