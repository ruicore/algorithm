# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-17 17:39:38
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-18 09:58:16


class Solution:
    def __init__(self):
        # 递归版本实现，当前位置的路径条数 = 当前位置左边的路径条数 + 当前位置上边的路径条数
        # 结果矩阵，用于存储已经遍历过的位置，减少递归重复
        self.res = []

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 如果矩阵为空，则直接返回0
        if not obstacleGrid:
            return 0
        # 获取矩阵的行数最大索引，获取矩阵列数最大索引
        row, col = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        # 初始化结果矩阵，每一个位置都初始化为-1，表示当前位置还没有遍历到
        self.res = [[-1 for _ in range(col+1)] for _ in range(row+1)]
        # 进行递归调用
        return self.recur(row, col, obstacleGrid)

    def recur(self, row, col, o):
        # 存储递归结果的递归，要注意递归的结束条件
        # 条件一：如果到达左上角，则返回
        if row == 0 and col == 0:
            # 如果左上角没有障碍返回1，表示有一条路，否则返回0，表示不可到达，即没有路
            return 1 if o[0][0] == 0 else 0
        # 条件二：如果已经到达矩阵之外，返回0，表示没有路，不可到达
        elif row < 0 or col < 0:
            return 0
        # 条件三：如果当前位置已经遍历过，则直接返回当前位置的路径
        elif self.res[row][col] != -1:
            return self.res[row][col]
        # 条件四：如果当前位置不可到达，直接返回0，并标记当前位置已经遍历过
        elif o[row][col] == 1:
            self.res[row][col] = 0
            return 0
        else:
            # 求得当前位置左边的路径条数
            left = self.recur(row, col-1, o)
            # 求得当前路径上边的路径条数
            top = self.recur(row-1, col, o)
            # 记录当前位置的路径条数
            self.res[row][col] = left+top
        # 返回当前位置的路径条数
        return self.res[row][col]


class Solution2:
    # 循环版本实现，当前位置的路径条数 = 当前位置左边的路径条数 + 当前位置上边的路径条数
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 如果矩阵为空，直接返回0
        if not obstacleGrid:
            return 0
        # 获得矩阵行数最大索引，获得矩阵列数最大索引
        row, col = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        # 结果矩阵，用于存储到达每一个位置的路径条数，每一个位置都初始化为0
        res = [[0 for _ in range(col+1)] for _ in range(row+1)]
        # 初始化左上角
        res[0][0] = 1 if not obstacleGrid[0][0] else 0
        # 初始化第一行，当前位置如果没有障碍且上一个位置能够到达：初始化为1，否则初始化为0
        for i in range(1, col+1):
            res[0][i] = 1 if not obstacleGrid[0][i] and res[0][i-1] else 0
        # 初始化第一列，当前位置如果没有障碍且上一个位置能够到达：初始化为1，否则初始化为0
        for i in range(1, row+1):
            res[i][0] = 1 if not obstacleGrid[i][0] and res[i-1][0] else 0
        # 遍历每一个位置
        for i in range(1, row+1):
            for j in range(1, col+1):
                # 当前位置没有障碍：当前位置路径条数= 当前位置左边路径条数+当前位置上一个路径条数
                # 当前位置有障碍：条数为0
                res[i][j] = res[i-1][j] + \
                    res[i][j-1] if not obstacleGrid[i][j] else 0
        return res[row][col]


if __name__ == "__main__":
    so = Solution2()
    res = so.uniquePathsWithObstacles([[0, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(res)
