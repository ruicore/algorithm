# LeetCode 57. Insert Interval

## Description

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

## 描述

给定一组非重叠间隔，在间隔中插入新间隔（必要时合并）。

您可以假设间隔最初是根据其开始时间排序的。

### 思路

* 这一道题是第五十六题Merge Intervals的演变，所以解题思路非常相似，只是多了一步插入而已,第五十六题在[这里](https://leetcode.com/problems/merge-intervals)，解析在[这里](https://www.ruicore.cn/leetcode-56-merge-intervals/).
* 这道题是要求向已经按起始位置排好序的区间中插入一个新区间，如果插入导致了区间有重叠则需要合并区间
* 因此思路如下
1. 找到原始区间中 第一个 **区间起始位置大于需要插入区间** 的区间
2. 在此位置插入区间
3. 对重叠的区间进行合并:检查当前区间起始位置是否在上一个区间之间，若是：检查当前区间的结束位置是否大于上一个区间，如果大于则更新上一个区间的结束位置，然后删除当前区间；如果没有在上一个区间之间，则什么也不做，继续判断下一个区间

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-16-57-Insert-Interval.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leecode-57-insert-interval/)，欢迎转载，转载需保留文章来源，作者信息和本声明.