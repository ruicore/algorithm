# LeetCode 436. Find Right Interval

## Description

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

```py
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
```

Example 2:

```py
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
``` 

Example 3:

```py
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
```

### 思路

* 所有的区间的结尾不重复，因此构造一个字典，健为区间的开始位置，值为区间在原数组中的索引。
* 将所有的区间的开始位置取出来形成一个数组 starts ，对数组按照从小到大排序。
* 对于一个区间，记此区间结尾为 end，查找在 starts 数组中第一个大于等于 end 的数所在的位置 t，t 即为满足条件的区间。
* 根据 t ，找到 t 在字典中对应的值即可确定区间的位置；对所有的区间都进行此操作。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-04-11 16:08:04
# @Last Modified by:   何睿
# @Last Modified time: 2020-04-11 16:34:06


from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        index_dict = {}
        for index, interval in enumerate(intervals):
            starts.append(interval[0])
            index_dict[interval[0]] = index

        starts.sort()

        return list(self._binary_find(starts, interval[1], index_dict) for interval in intervals)

    def _binary_find(self, nums, target, index_dict):

        if target in index_dict:
            return index_dict[target]

        left, right = 0, len(nums) - 1
        middle = left + (right - left) // 2
        while left <= right:
            if nums[middle] >= target and (middle == 0 or nums[middle - 1] < target):
                return index_dict[nums[middle]]
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] >= target and (middle == 0 or nums[middle - 1] >= target):
                right = middle - 1
            middle = left + (right - left) // 2

        return -1
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2020-04-11-436-Find-Right-Interval.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-436-find-right-interval/) ，作者信息和本声明.
