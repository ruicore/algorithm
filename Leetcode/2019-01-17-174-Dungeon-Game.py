# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 14:11:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-17 19:43:57

import sys


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        # 这道题目使用动态规划
        row, col = len(dungeon), len(dungeon[0])
        # 声明一个二维数组
        b = [[sys.maxsize for _ in range(col + 1)] for _ in range(row + 1)]
        # 初始化右下角的位置为1，1表示这里需要1个生命值
        b[row][col - 1], b[row - 1][col] = 1, 1
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                # 当前位置的生命值由其下面一个和右边一个生命值决定
                need = min(b[i + 1][j], b[i][j + 1]) - dungeon[i][j]
                # 如果need为正说明这个地方需要消耗生命值
                # 如果need为负说明这个位置会提供生命值
                b[i][j] = max(1, need)

        return b[0][0]
