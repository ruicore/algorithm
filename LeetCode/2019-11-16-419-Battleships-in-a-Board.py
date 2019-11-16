# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-16 21:22:05
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-16 21:36:25

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        count, row, col = 0, len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue
                count += 1

                # 下面这种写法是正向思考，等价于上面的写法，思考是下面的思路，简化代码为上面的写法
                # if i > 0 and j > 0:
                #     if board[i][j] == "X" and board[i][j - 1] == "." and board[i - 1][j] == ".":
                #         count += 1
                # elif i == 0 and j == 0:
                #     if board[i][j] == "X":
                #         count += 1
                # elif i == 0:
                #     if board[i][j] == "X" and board[i][j - 1] == ".":
                #         count += 1
                # elif j == 0:
                #     if board[i][j] == "X" and board[i - 1][j] == ".":
                #         count += 1

        return count
