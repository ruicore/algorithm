# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-03 08:11:17
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-03 11:57:48

import heapq

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        queue, visited, max_heigth, water = [], set(), 0, 0
        row, col = len(heightMap), len(heightMap[0])
        count = row * col

        self.fill_border(queue, heightMap)
        visited = {(row, col) for _, row, col in queue}
        while queue:
            if len(visited) == count:
                return water
            height, i, j = heapq.heappop(queue)
            max_heigth = max(max_heigth, height)
            water += self.visit_neighbors(queue, visited, heightMap, max_heigth, row, col, i, j)
        return water

    def visit_neighbors(self, queue, visited, heightMap, max_heigth, row, col, i, j):

        water = 0
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow, ncol = i + x, j + y
            if (nrow, ncol) not in visited and self.is_in_border(row, col, nrow, ncol):
                num = heightMap[nrow][ncol]
                water += max(0, max_heigth - num)
                visited.add((nrow, ncol))
                heapq.heappush(queue, (num, nrow, ncol))

        return water

    def fill_border(self, queue, heightMap):
        row, col = len(heightMap), len(heightMap[0])
        for i in range(row):
            heapq.heappush(queue, (heightMap[i][0], i, 0))
            heapq.heappush(queue, (heightMap[i][-1], i, col - 1))
        for i in range(1, col - 1):
            heapq.heappush(queue, (heightMap[0][i], 0, i))
            heapq.heappush(queue, (heightMap[-1][i], row - 1, i))

    def is_in_border(self, row, col, i, j):
        return 0 <= i < row and 0 <= j < col
