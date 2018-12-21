# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-20 21:40:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-21 09:28:08

from pprint import pprint


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 获取行数或者列数
        row, col = len(matrix), len(matrix[0])
        # 把所有的整数自增一次，这样我们就创造了一个特殊值1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > 0:
                    matrix[i][j] += 1
        # 按行遍历，遇到每一行的第一个0，则把0前面的元素全部置为0
        # 把0后面的元素：若是0，置为1，如不是0，置为0
        # 把本身（即第一个0）置为0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    for t in range(0, j):
                        matrix[i][t] = 0
                    for t in range(j+1, col):
                        if matrix[i][t] == 0:
                            matrix[i][t] = 1
                        else:
                            matrix[i][t] = 0
                    break
        # 检查列，只要此列有1，则把此列置为0
        for i in range(col):
            for j in range(row):
                if matrix[j][i] == 1:
                    for t in range(0, row):
                        matrix[t][i] = 0
                    break
        # 把所有的正数自减一次
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1


class Solution2:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 用于标记第一行，第一列是否需要改变
        firstrow, firstcol = False, False
        # 获取行数和列数
        row, col = len(matrix), len(matrix[0])
        # 检查矩阵第一列是否需要改变
        # 只要矩阵第一列有0，则第一列需要置为0
        for i in range(row):
            if matrix[i][0] == 0:
                # 找到0即可break退出循环
                firstcol = True
                break
        # 检查矩阵第一行是否需要改变
        # 只要矩阵第一行有0，则第一行需要置为0
        for i in range(col):
            if matrix[0][i] == 0:
                # 找到0即可break推出循环
                firstrow = True
                break
        # 从（1，1）开始检查，若matrix[i][j]==0
        # 则置matrix[i][0]=0,matrix[0][j]=0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 把第一行为0所对应的列全部置为0
        for i in range(1, col):
            if matrix[0][i] == 0:
                for j in range(1, row):
                    matrix[j][i] = 0
        # 把第一列所对应的行全部置为0
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0
        # 检查是否许需要把第一列置为0
        if firstcol:
            for i in range(row):
                matrix[i][0] = 0
        # 检查是否需要把第一行置为0
        if firstrow:
            for i in range(col):
                matrix[0][i] = 0


if __name__ == "__main__":
    so = Solution2()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    so.setZeroes(matrix)
    pprint(matrix)
