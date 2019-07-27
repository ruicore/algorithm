# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-27 08:06:32
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-27 08:06:32

import heapq

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count_row, count_col = len(matrix), len(matrix[0])
        if not matrix:
            return 0
        heap = []
        for i in range(count_row):
            for j in range(count_col):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heap[0]


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        small, big = matrix[0][0], matrix[-1][-1]
        while small < big:
            middle = small + ((big - small) >> 1)
            count = self.less_eq_than_k(matrix, middle)
            if count >= k:
                big = middle
            if count < k:
                small = middle + 1

        return small

    def less_eq_than_k(self, matrix: List[List[int]], middle: int) -> int:
        count, i, j = 0, 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= middle:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count
