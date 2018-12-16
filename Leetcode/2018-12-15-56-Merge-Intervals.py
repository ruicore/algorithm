# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-15 19:23:28
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-16 13:11:49

# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def depart(self, intervals, left, right):
        pivotindex = left+((right-left) >> 1)
        pivotvalue = intervals[pivotindex].start
        i, j = left, left
        for j in range(left, right+1):
            if intervals[j].start < pivotvalue:
                intervals[i], intervals[j] = intervals[j], intervals[i]
                if i == pivotindex:
                    pivotindex = j
                i += 1
        intervals[i], intervals[pivotindex] = intervals[pivotindex], intervals[i]
        return i

    def quicksort(self, intervals, left, right):
        if left >= right:
            return
        middle = self.depart(intervals, left, right)
        self.quicksort(intervals, left, middle-1)
        self.quicksort(intervals, middle+1, right)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        self.quicksort(intervals, 0, len(intervals)-1)
        # intervals = sorted(intervals, key=lambda x: x.start)
        for item in intervals:
            if not ans or item.start > ans[-1].end:
                ans.append(item)
            elif item.end > ans[-1].end:
                ans[-1].end = item.end
        return ans


if __name__ == "__main__":
    so = Solution()
    a = Interval(1, 4)
    b = Interval(0, 4)
    c = Interval(8, 10)
    # d = Interval(15, 18)
    res = so.merge([a, b])
    # for item in res:
    #     print(item.start, item.end)
