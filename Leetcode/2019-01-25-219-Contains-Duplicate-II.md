# LeetCode 219. Contains Duplicate II

## Description

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

## 描述

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

### 思路

* 我们使用一个字典来存储相同的值，字典的键为该数字，字典的值为一个数组，存储该数字的索引值.
* 每次向数组中添加值的时候，我么都检查数组的最后两个值的差是否小于等于k，若存在一个解，我们返回True，否则我们返回False.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-25 19:04:39
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 22:37:41


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 如果没有数字或者只有一个数字，则不可能有满足题意的解
        if nums == [] or len(nums) == 1: return False
        # 如果没有重复元素，也不可能有满足题意的解
        if len(nums) == len(set(nums)): return False
        # 我们用一个dict存储重复的值
        dic = {}
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = []
            dic[num].append(index)
            # 如果相同的值索引差小于等于k，返回True
            if len(dic[num]) > 1 and dic[num][-1] - dic[num][-2] <= k:
                return True
        # 如果遍历整个数组都没有找到满足条件的值，返回False
        return False
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-25-219-Contains-Duplicate-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-219-contains-duplicate-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
