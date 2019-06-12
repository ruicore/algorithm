# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-17 21:58:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-18 10:59:36


class Solution:
    # 递归版本，当前位置最小值 = min{当前位置左边最小值，当前位置上边最小值}+当前位置的值
    def __init__(self):
        # 声明结果矩阵，用于记录已经遍历过的位置
        self.res = []

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 入股gird为空，则直接返回
        if not grid:
            return 0
        # 获取最大行的索引，获取最大列的索引
        row, col = len(grid)-1, len(grid[0])-1
        # 初始化第一行，每一个位置的最短路径 = 左边的最短路径+本身的值
        for i in range(1, col+1):
            grid[0][i] += grid[0][i-1]
        # 初始化第一列，每一个位置的最短路径 = 上边的最短路径+本身的值
        for i in range(1, row+1):
            grid[i][0] += grid[i-1][0]
        # 初始化结果矩阵，-1表示当前位置还没有遍历过
        self.res = [[-1 for _ in range(col+1)] for _ in range(row+1)]
        return self.recur(row, col, grid)

    def recur(self, row, col, grid):
        # 如果到达矩阵左上角的位置，返回此位置的路径值
        if row == 0 and col == 0:
            return grid[0][0]
        # 如果到达第一行但不是最坐上角
        elif row == 0:
            return grid[0][col]
        # 如果到达第一列但不是最左上角
        elif col == 0:
            return grid[row][0]
        # 如果当前位置已经遍历过
        elif self.res[row][col] != -1:
            return self.res[row][col]
        # 求矩阵当前位置做左边的最小值
        left = self.recur(row, col-1, grid)
        # 求矩阵当前位置上边的最小值
        top = self.recur(row-1, col, grid)
        # 记录矩阵当前位置的值
        self.res[row][col] = min(left, top)+grid[row][col]
        # 返回矩阵当前位置的值
        return self.res[row][col]


class Solution2:
    # 循环版本实现，当前位置最小值 = min{当前位置左边最小值，当前位置上边最小值}+当前位置的值
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 如果gird矩阵为空，则直接返回
        if not grid:
            return 0
        # 获得行的最大索引，获得列的最大索引
        row, col = len(grid)-1, len(grid[0])-1
        # 初始化第一行，当前位置最短路径 = 当前位置左边最短路径 + 当前位置的值
        for i in range(1, col+1):
            grid[0][i] += grid[0][i-1]
        # 初始化第一列，当前位置最短路径 = 当前位置上边最短路径 + 当前位置的值
        for i in range(1, row+1):
            grid[i][0] += grid[i-1][0]
        # 遍历每一个位置，当前位置最短路径 = min {当前位置左边最短路径，当前位置上边最短路径} + 当前位置的值
        for i in range(1, row+1):
            for j in range(1, col+1):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[row][col]


if __name__ == "__main__":
    so = Solution2()
    res = so.minPathSum([[3, 8, 6, 0, 5, 9, 9, 6, 3, 4, 0, 5, 7, 3, 9, 3], [0, 9, 2, 5, 5, 4, 9, 1, 4, 6, 9, 5, 6, 7, 3, 2], [8, 2, 2, 3, 3, 3, 1, 6, 9, 1, 1, 6, 6, 2, 1, 9], [1, 3, 6, 9, 9, 5, 0, 3, 4, 9, 1, 0, 9, 6, 2, 7], [8, 6, 2, 2, 1, 3, 0, 0, 7, 2, 7, 5, 4, 8, 4, 8], [4, 1, 9, 5, 8, 9, 9, 2, 0, 2, 5, 1, 8, 7, 0, 9], [6, 2, 1, 7, 8, 1, 8, 5, 5, 7, 0, 2, 5, 7, 2, 1], [8, 1, 7, 6, 2, 8, 1, 2, 2, 6, 4, 0, 5, 4, 1, 3], [9, 2, 1, 7, 6, 1, 4, 3, 8, 6, 5, 5, 3, 9, 7, 3], [
                        0, 6, 0, 2, 4, 3, 7, 6, 1, 3, 8, 6, 9, 0, 0, 8], [4, 3, 7, 2, 4, 3, 6, 4, 0, 3, 9, 5, 3, 6, 9, 3], [2, 1, 8, 8, 4, 5, 6, 5, 8, 7, 3, 7, 7, 5, 8, 3], [0, 7, 6, 6, 1, 2, 0, 3, 5, 0, 8, 0, 8, 7, 4, 3], [0, 4, 3, 4, 9, 0, 1, 9, 7, 7, 8, 6, 4, 6, 9, 5], [6, 5, 1, 9, 9, 2, 2, 7, 4, 2, 7, 2, 2, 3, 7, 2], [7, 1, 9, 6, 1, 2, 7, 0, 9, 6, 6, 4, 4, 5, 1, 0], [3, 4, 9, 2, 8, 3, 1, 2, 6, 9, 7, 0, 2, 4, 2, 0], [5, 1, 8, 8, 4, 6, 8, 5, 2, 4, 1, 6, 2, 2, 9, 7]])
    print(res)
