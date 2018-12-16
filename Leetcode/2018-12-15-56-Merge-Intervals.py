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
        # 确定分区点的位置
        pivot = left+((right-left) >> 1)
        # 将分区点和最后一个位置交换
        intervals[right], intervals[pivot] = intervals[pivot], intervals[right]
        # i，j 初始位置为最左边的位置，i表示以排序区间的末尾（不包含在排序区间之内）
        i, j = left, left
        for j in range(left, right):
            # 如果当前位置比pivot位置的值小（由于已经把pivot交换到最后一个位置，pivot==riht）
            if intervals[j].start < intervals[right].start:
                # 把当前位置的值放入已排序区间的末尾
                intervals[i], intervals[j] = intervals[j], intervals[i]
                # 已排序区间自增一次
                i += 1
        # 把最后一个位置和i交换
        intervals[i], intervals[right] = intervals[right], intervals[i]
        return i

    def quicksort(self, intervals, left, right):
        # 递归结束条件，当left>=right时
        if left >= right:
            return
        # 对数组取某一个值，分为两块
        middle = self.depart(intervals, left, right)
        # 对左边排序
        self.quicksort(intervals, left, middle-1)
        # 对右边排序
        self.quicksort(intervals, middle+1, right)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        # 对
        self.quicksort(intervals, 0, len(intervals)-1)
        # 这里也可以用python自带的排序函数，python排序函数是用C实现的，速度更快
        # intervals = sorted(intervals, key=lambda x: x.start)
        for item in intervals:
            if not ans or item.start > ans[-1].end:
                ans.append(item)
            elif item.end > ans[-1].end:
                ans[-1].end = item.end
        return ans


if __name__ == "__main__":
    so = Solution()
    a = Interval(1, 3)
    b = Interval(2, 6)
    c = Interval(8, 10)
    d = Interval(15, 18)
    res = so.merge([a, b, c, d])
    for item in res:
        print(item.start, item.end)
