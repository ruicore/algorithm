# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-14 21:48:26
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-14 21:49:22

import copy


class Solution:

    def __init__(self):
        # 初始变量，减少函数传递次数
        # 记录列的情况，表示是否被占用,Ture表示被占用，False表示空
        self.coloccupied = []
        # 记录左对角线的情况，表示左对角线是否被占用
        self.Left_diag = []
        # 记录又对角线的情况，表示右边的对角线是否被占用
        self.right_diag = []
        # 矩阵维度
        self.rank = 0
        # 结果数组
        self.count = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.rank = n
        self.coloccupied = [False]*self.rank
        self.Left_diag = [False]*(2*self.rank-1)
        self.right_diag = [False]*(2*self.rank-1)
        self.nQueen(0)
        return self.count

    # 检查当前位置是否被占用，被占用返回Ture，没有被占用返回False
    def isOccupied(self, row, col):
        # 当前位置所在的列，左对角线，右对角线只要有一个被占用，则该位置就被占用
        return self.coloccupied[col] or self.Left_diag[row+col] or self.right_diag[row+self.rank-col-1]

    def put(self, row, col, isput):
        # 该列是否被占用
        self.coloccupied[col] = isput
        # 该位置左对角线是否被占用
        self.Left_diag[row+col] = isput
        # 该位置右对角线是否被占用
        self.right_diag[row+self.rank-col-1] = isput
        # 如果是放置，则放入"Q"，清空，放置"."
        # self.board[row][col] = "Q" if isput else "."

    def nQueen(self, row):
        if row == self.rank:
            # 注意，这里需要用深拷贝
            self.count += 1
            return
        for col in range(self.rank):
            if self.isOccupied(row, col):
                continue
            # 在当前位置放置皇后
            self.put(row, col, True)
            # 进入下一层寻找
            self.nQueen(row+1)
            # 返回的时候，逐层清除原来放置的皇后
            self.put(row, col, False)


if __name__ == "__main__":
    so = Solution()
    res = so.totalNQueens(3)
    print(res)
