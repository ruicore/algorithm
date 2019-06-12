# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 18:21:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 18:32:37


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        res, row, col = 0, len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
