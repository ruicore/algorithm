# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-03-31 19:18:41
# @Last Modified by:   何睿
# @Last Modified time: 2020-04-01 15:23:00
rom typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        count = 0
        last = 0
        for i in range(1, len(intervals)):
            if intervals[last][1] > intervals[i][0]:
                count += 1
                if intervals[last][1] >= intervals[i][1]:
                    last = i
            else:
                last = i

        return count
