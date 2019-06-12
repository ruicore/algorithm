# LeetCode 56. Merge Intervals

## Description

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

## 描述

给定间隔的集合，合并所有重叠的间隔。

### 思路

* 这道题是给定一些区间，要求合并有重叠部分的区间.
* 思路很清晰，我们首先按照区间的起始位置，对所有的区间从小到大排序.
* 然后我们检查每一个区间的起始位置是否在前一个区间之内，如果是，并且此区间的结束位置大于上一个区间的结束位置，我们我们更新上一个区间的结束位置
* 如果不是，我们把当前区间添加到结果数组中.
* 这里说一下排序.

### [快速排序](!https://zh.wikipedia.org/zh/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

* 这道题我们采用快速排序.
* 快排的思路是在数组中随便找一个值P，然后把数组分成两部分：左边部分的所有值小于等于P，右边的所有值大于等于P（以从小到大排序为例）.
* 快排是不稳定的排序算法，平均时间复杂的O（nlogn）,空间复杂度O(1).
* 说一下空间复杂度：空间复杂的为常数，即要求排序在原地排序.
* 排序的关键是分区：假设有一个数组A\[0:max],我们取最后一个值P=A\[max]为分区点，我们假设A\[0:i-1]为已经排好序的区间，我们每次从未排序区间中找小于等于P的值
* 然后我们把这个值放到已排序区间的尾部，i自增一次，然后一直重复，直到末尾，最后把A\[i]和A\[max]交换，就完了成了分区.

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-15-56-Merge-Intervals.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-56-merge-intervals/)，欢迎转载，转载需保留文章来源，作者信息和本声明.