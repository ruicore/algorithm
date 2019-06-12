# LeetCode 209. Minimum Size Subarray Sum

## Description

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

## 描述

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

### 思路

* 使用两个指针left和right，用_sum来表示当前的和. right不断向右移动，_sum累加，当_sum大于等于s的时候，left向右移动直到_sum小于s，有效长度为right-left+2,返回所有有效长度的最小值即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 11:37:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 11:37:16

import sys


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 初始化长度
        length = sys.maxsize
        _sum, left, right = 0, 0, 0
        while right < len(nums):
            _sum += nums[right]
            # 如果当前的和已经大于等于s
            if _sum >= s:
                # 我们将左指针向右移动，和小于s时跳出
                while _sum >= s and left <= right:
                    _sum -= nums[left]
                    left += 1
                # 更新长度
                length = min(right - left + 2, length)
            right += 1
        # 如果length始终没有发生改变返回0，否则返回length本身
        return length if length != sys.maxsize else 0
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-22-209-Minimum-Size-Subarray-Sum.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-209-minimum-size-subarray-sum/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
