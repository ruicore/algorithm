# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 10:26:20
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 11:18:07


class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                count = self.__serach(board, i, j, row - 1, col - 1)
                # 如果当前位置是1，并且周围有两个1;或者当前周围有3个1
                if (board[i][j] and count == 2) or count == 3:
                    board[i][j] |= 0b10
        # 更新当前位置的信息
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1
        return

    def __serach(self, board, i, j, row, col):
        # 统计当前位置的临近的8个方格内1的个数
        count = 0
        # 获取行的边界
        row1, row2 = max(0, i - 1), min(row, i + 1)
        # 获取列的边界
        col1, col2 = max(0, j - 1), min(col, j + 1)
        for k in range(row1, row2 + 1):
            for m in range(col1, col2 + 1):
                count += (board[k][m] & 1)
        # 减去本身这个位置的值
        return count - (board[i][j] & 1)