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
