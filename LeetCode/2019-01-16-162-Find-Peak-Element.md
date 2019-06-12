# LeetCode 162. Find Peak Element

## Description

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

## 描述

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。

### 思路

* 此题目使用二分查找.
* 如果当前值小于右边的值，说明峰值应该在右边（不包括当前节点），如果当前值大于右边的值，说明峰值应该当前值左边（包括当前节点）.
* 找到的条件是到达了边界或者当前值比左右两边的值都大.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 10:40:41
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 11:21:29


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        middle, left, right = 0, 0, count - 1
        while left <= right:
            # 取中间值
            middle = left + ((right - left) >> 1)
            # 如果当前是递增的序列，说明较大值在右边（不包括当前节点）
            if middle < count - 1 and nums[middle] < nums[middle + 1]:
                left = middle + 1
            # 如果当前是递减的徐磊，说明较大值在左边（包括当前节点）
            if middle < count - 1 and nums[middle] > nums[middle + 1]:
                right = middle
            # 结束条件：到达了边界或者当前值比左右两个值大
            if (middle==0 or nums[middle] > nums[middle - 1]) and (middle == count-1 or nums[middle] > nums[middle + 1]):
                return middle
        return middle
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-162-Find-Peak-Element.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-162-find-peak-element/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
