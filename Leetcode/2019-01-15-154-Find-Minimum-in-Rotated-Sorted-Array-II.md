# LeetCode 154. Find Minimum in Rotated Sorted Array II

## Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

## 描述

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是寻找旋转排序数组中的最小值的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

### 思路

* 此题目是第[153题](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)的递进题，允许重复不会增加算法的时间复杂度，只是会增加判断的条件.
* [基本思路](https://www.ruicore.cn/leetcode-153-find-minimum-in-rotated-sorted-array/)同153一样.
* 在增加了重复的情况下，我们先将left移动到相等数值的最右边，right移动到相同数值的最左边，然后我们判断当前的数值是否已经连续递增或递减，若是则直接返回最小值.
* 若不是，则进行条件判断，这时的条件同第153题目完全一样.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 16:01:45
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 16:35:18


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            # 相同的值直接跳过
            while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                left += 1
            while right > 0 and nums[right] == nums[right - 1]:
                right -= 1
            middle = left + ((right - left) >> 1)
            # 判断当前的片段是否连续
            # 如果是连续递增，返回最左边的值
            if nums[left] <= nums[middle] <= nums[right]:
                return nums[left]
            # 如果是连续递减，返回最右边的值
            if nums[right] <= nums[middle] <= nums[left]:
                return nums[right]
            # 找到枢纽值的条件
            if nums[middle] < nums[middle + 1] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[0]:
                left = middle + 1
            if nums[middle] < nums[-1]:
                right = middle
        return nums[left]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-15-154-Find-Minimum-in-Rotated-Sorted-Array-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-154-find-minimum-in-rotated-sorted-array-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
