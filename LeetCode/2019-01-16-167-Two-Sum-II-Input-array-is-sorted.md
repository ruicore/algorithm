# LeetCode 167. Two Sum II - Input array is sorted

## Description

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

## 描述

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

### 思路

* 数组已经排好序，我们从两边开始求和，如果当前的和小于target，我们让左指针向右移动一个，如果大于target我们让右指针向左移动一个，直到其和与target相等.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 15:49:20
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 15:53:13


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum > target:
                right -= 1
            elif _sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-167-Two-Sum-II-Input-array-is-sorted.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-167-two-sum-ii---input-array-is-sorted/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
