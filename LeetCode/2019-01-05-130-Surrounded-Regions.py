# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-05 22:10:17
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-06 14:25:42

from pprint import pprint


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 如果矩阵为空，则直接返回
        if not board:
            return
        # 获取矩阵行数和列数
        row, col = len(board), len(board[0])
        # 遍历第一行和最后一行
        for i in range(0, row):
            # 如果当前的元素为"O",则进行深度优先遍历，将所有的"O"都置为"1"
            # （或者其他标记元素，只要不是"X"或"O"即可）
            # 检查第一行的所有元素
            if board[i][0] == "O":
                self.dfs(board, i, 0, row, col)
            # 检查最后一行的所有元素
            if board[i][col-1] == 'O':
                self.dfs(board, i, col-1, row, col)
        # 同上，遍历第一列和最后一列的所有元素
        for i in range(1, col-1):
            if board[0][i] == 'O':
                self.dfs(board, 0, i, row, col)
            if board[row-1][i] == 'O':
                self.dfs(board, row-1, i, row, col)
        # 遍历所有元素，将刚才标记的元素置为"O",其他元素都置为"X"
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == "1":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def dfs(self, board, row, col, rows, cols):
        # 递归结束条件，如果已经越界则结束递归
        if row >= rows or col >= cols or row < 0 or col < 0:
            return
        # 如果当前元素是"O",则置为标记元素"1"
        if board[row][col] == "O":
            board[row][col] = '1'
            # 进行深度优先遍历，一共有上下左右四个出口
            self.dfs(board, row+1, col, rows, cols)
            self.dfs(board, row-1, col, rows, cols)
            self.dfs(board, row, col+1, rows, cols)
            self.dfs(board, row, col-1, rows, cols)
