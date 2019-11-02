# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-02 10:57:28
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-02 12:02:14

from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        for i in range(row):
            self.dfs(matrix, i, 0, -1, row, col, pacific)
            self.dfs(matrix, i, col - 1, -1, row, col, atlantic)

        for i in range(col):
            self.dfs(matrix, 0, i, -1, row, col, pacific)
            self.dfs(matrix, row - 1, i, -1, row, col, atlantic)

        return filter(lambda x: pacific[x[0]][x[1]] and atlantic[x[0]][x[1]], ((i, j) for i in range(row) for j in range(col)))

    def dfs(self, matrix, i, j, height, row, col, reached):
        if not 0 <= i < row or not 0 <= j < col or reached[i][j] or matrix[i][j] < height:
            return
        reached[i][j] = True
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            self.dfs(matrix, i + x, j + y, matrix[i][j], row, col, reached)
