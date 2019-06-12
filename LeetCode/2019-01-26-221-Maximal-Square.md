# LeetCode 221. Maximal Square

## Description

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

## 描述

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

### 思路

* 这道题使用动态规划.
* 动态规划矩阵的值表示当前位置能够形成的最大正方形的边.
* 如果给定的matrix矩阵中，当前位置matrix\[i]\[j]是"0"，则动态规划矩阵当前位置为"0"，如果当前位置是"1"，则动态规划矩阵board当前位置的值为1+min(board\[i - 1]\[j],board\[i]\[j - 1],board\[i - 1]\[j - 1]),并且在循环的过程中，我们用一个值来记录最大的边长，并不断更新最大边长.
* 最后我们返回边长的平方，即矩阵的面积.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-26 21:25:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-27 20:17:15


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 如果矩阵为空，直接返回0
        if not matrix: return 0
        # 获取矩阵的行数和列数
        row, col = len(matrix), len(matrix[0])
        # 动态规划矩阵，矩阵中的值表示正方形的边长
        board = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        # res表示最大边长
        res = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                # 如果当前位置是'1'
                if matrix[i - 1][j - 1] == "1":
                    left = board[i - 1][j]
                    up = board[i][j - 1]
                    dia = board[i - 1][j - 1]
                    # 动态规划矩阵，当前位置的值为当前位置左边
                    # 当前位置上边，当前位置斜上边位置的最小值载加上1
                    board[i][j] += 1 + min(left, up, dia)
                    # 不断更新最大边长的值
                    res = max(res, board[i][j])
        # 返回最大边长的平方，即正方形的面积
        return res**2
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-26-221-Maximal-Square.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-221-maximal-square/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
