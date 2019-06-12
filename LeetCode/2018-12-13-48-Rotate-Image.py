# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-13 11:02:39
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-13 14:32:12


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 正矩阵的维度
        rank = len(matrix[0])
        # 第一行，最左边的列，最后一行，最右边一列
        rowtop, coleft, rowbot, colright = 0, 0, rank-1, rank-1
        while rank > 1:
            for i in range(rank-1):
                # 第rowtop行的第coleft+i个元素保存
                temp = matrix[rowtop][coleft+i]
                # 将矩阵第一列的元素给矩阵第一行的元素
                matrix[rowtop][coleft+i] = matrix[rowbot-i][coleft]
                # 将矩阵最后一行的元素给矩阵第一列的元素
                matrix[rowbot-i][coleft] = matrix[rowbot][colright-i]
                # 将矩阵最后一列的元素给矩阵最后一行的元素
                matrix[rowbot][colright-i] = matrix[rowtop+i][colright]
                # 将矩阵第一行的元素给矩阵最后一列的元素
                matrix[rowtop+i][colright] = temp
            # 矩阵的行数（行列的个数相等，也可以表示为列数）减少2（上下各减少一行）
            rank -= 2
            # 最高的行数加一，表示行向内进一层，行数减少一行
            rowtop += 1
            # 最左边的列加一，表示向右进一层，列数减少一列
            coleft += 1
            # 最下边的行减一，表示向上进程一层，行数减少一行
            rowbot -= 1
            # 最右边的列减少一列，表示向左进一层，列数减少一列
            colright -= 1
        return
