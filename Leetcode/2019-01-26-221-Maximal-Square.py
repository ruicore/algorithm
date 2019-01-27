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