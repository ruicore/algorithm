# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 15:52:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 17:07:43


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # 我们人为的在s和t中的首位置增加一个空字符
        # 行数和列数
        # 以目标字符串t作为行数，来源字符串s作为列数（反之也可以）
        row, col = len(t)+1, len(s)+1
        # 初始花二维矩阵
        matrix = [[0 for _ in range(col)] for _ in range(row)]
        # 矩阵的matrix[0][0]置为1，表示从来源字符串中取空个字符串够成目标字符串中的空个字符有1种方法
        matrix[0][0] = 1
        # 初始化第一行，表示从来源字符串s中取字符构成目标字符串t的第一个字符（空字符）只有1种方法
        for i in range(1, col):
            matrix[0][i] = 1
        # 初始化第第一列，表示取来源字符串中的第一个字符（空字符）构成t[1:i]有0种方法
        for i in range(1, row):
            matrix[i][0] = 0
        for i in range(1, col):
            for j in range(1, row):
                # 如果当前来源字符s[i-1]与目标字符t[j-1]相等
                if t[j-1] == s[i-1]:
                    matrix[j][i] = matrix[j-1][i-1]+matrix[j][i-1]
                else:
                    matrix[j][i] = matrix[j][i-1]
        # 最终结果存储在矩阵右下角
        return matrix[row-1][col-1]
