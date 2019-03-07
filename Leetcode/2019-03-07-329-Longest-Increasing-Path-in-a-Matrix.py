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