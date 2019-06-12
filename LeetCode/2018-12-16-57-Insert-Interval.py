# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-16 15:54:35
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-16 16:27:48


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # 如果intervals为空，则直接返回newInterval，注意返回的形式为数组
        if not intervals:
            return [newInterval]
        # 初始化i表示起始索引，count表示intervals中的个数
        i, count = 0, len(intervals)
        # 找到intervals中第一个start值比newInterval大的位置
        while i < count and newInterval.start > intervals[i].start:
            i += 1
        # 在此位置插入
        intervals.insert(i, newInterval)
        # count总数加一
        count += 1
        i = 1
        while i < count:
            # 如果当前位置的区间起始位置在上一个区间之间
            if intervals[i-1].start <= intervals[i].start <= intervals[i-1].end:
                # 如果当前位置区间的结束大于上一个区间，则更新上一个区间的结束位置
                if intervals[i].end > intervals[i-1].end:
                    intervals[i-1].end = intervals[i].end
                # 删除当前的区间
                del intervals[i]
                # 区间总数减一
                count -= 1
                # 索引减一
                i -= 1
            i += 1
        return intervals


if __name__ == "__main__":
    so = Solution()
    a = Interval(1, 5)
    b = Interval(2, 3)
    res = so.insert([a], b)
    for item in res:
        print(item.start, item.end)
