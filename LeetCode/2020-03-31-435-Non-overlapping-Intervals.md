# LeetCode 435. Non-overlapping Intervals

## Description

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

```py
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```
Example 2:

```py
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```
Example 3:

```py
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```
Note:

```py
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
```

### 思路

* 对每个区间按照起始位置从小到大排序。
* 对于两个区间，如果前一个区间的结尾位置大于后一个区间的起始位置，说明存在重叠，需要去除重复。
* 为了尽量减少去重的区间，我们选择去掉结尾位置靠后的区间。在实际的代码中，我们不需要真的删除区间，用一个变量指向上一个保留的区间就可以了。

```py
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
            # 上一个区间的 end 大于下一个区间的 start，说明有重叠
            if intervals[last][1] > intervals[i][0]:
                count += 1
                # 保留区间中 end 较小的那一个
                if intervals[last][1] >= intervals[i][1]:
                    last = i
            # 没有重叠，last 指向下一个区间
            else:
                last = i

        return count
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2020-03-31-435-Non-overlapping-Intervals.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-435-non-overlapping-intervals/) ，作者信息和本声明.
