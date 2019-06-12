# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-11 20:41:49
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-12 08:14:42

import sys
import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        if not matrix: return 0
        area, row, col = -sys.maxsize, len(matrix), len(matrix[0])

        for left in range(col):
            tmp = [0 for _ in range(row)]
            for right in range(left, col):
                for i in range(row):
                    tmp[i] += matrix[i][right]
                res = self.__get_kadane(tmp, k)

                if res != None: area = max(res, area)

        return area

    def __get_kadane(self, array: List[int], k: int) -> int:

        if not array: return 0

        sum_list, tmp, res = [0], 0, -sys.maxsize

        for item in array:
            tmp += item
            max_min = tmp - k
            if max_min == 0:
                return k
            else:
                index = bisect.bisect_left(sum_list, max_min)
                if index != len(sum_list):
                    res = max(res, tmp - sum_list[index])

            bisect.insort_left(sum_list, tmp)

        return res if res <= k else None