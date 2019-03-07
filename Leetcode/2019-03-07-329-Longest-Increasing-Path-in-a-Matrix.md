# LeetCode 329. Longest Increasing Path in a Matrix

## Description

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

```py
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
```

Example 2:

```py
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. 
Moving diagonally is not allowed.
```

## 描述

给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

```py
输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
```

示例 2:

```py
输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
```

### 思路

* 这道题主要使用记忆化递归和深度优先遍历。
* 我们以给定的矩阵的每一个位置为起点，进行深度优先遍历。
* 我们存储每个位置深度优先遍历的结果，当下一次走到这个位置的时候，我们直接返回当前位置记录的值，这样可以减少遍历的次数，加快执行速度。
* 二维矩阵 dp 初始化每个位置都为 0 ，当遍历到某个位置不为 0 的时候，说明该位置已经遍历过了，我们直接返回其值。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-07 21:19:51
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-07 22:23:10

from itertools import product


class Solution:
    def longestIncreasingPath(self, matrix: [[int]]) -> int:
        # 如果矩阵为空，返回 0
        if not matrix or not matrix[0]: return 0
        # 获取矩阵的行数和列数
        row, col = len(matrix), len(matrix[0])
        # 记忆化递归，记录每个位置的最大值
        dp = [[0] * col for _ in range(row)]
        # 遍历每一个位置，以每一个位置为起点进行深度优先遍历
        # 返回最大值
        return max(
            self._dfs(i, j, row, col, matrix, dp)
            for i, j in product(range(row), range(col)))

    def _dfs(self, i, j, row, col, matrix, dp):
        # 如果当前位置不为零，说明当前位置的最大值已经被找到
        # 采用记忆化递归，直接返回最大值
        if dp[i][j]: return dp[i][j]
        # 遍历四个方向
        for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            m, n = x + i, y + j
            # 如果下一个位置没有越界并且下一个位置的只严格大于位置i，j
            if 0 <= m < row and 0 <= n < col and matrix[i][j] < matrix[m][n]:
                # 记录最大值
                dp[i][j] = max(dp[i][j], self._dfs(m, n, row, col, matrix, dp))
        # 把当前位置本身加上
        dp[i][j] += 1
        # 返回以当前位置为起点，所有路径中的最大值
        return dp[i][j]
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-07-329-Longest-Increasing-Path-in-a-Matrix.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-329-longest-increasing-path-in-a-matrix/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-329-longest-increasing-path-in-a-matrix/) ，作者信息和本声明.
微信公众号：techruicore 
