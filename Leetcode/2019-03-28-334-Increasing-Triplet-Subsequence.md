# LeetCode 334. Increasing Triplet Subsequence

## Description

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: \[1,2,3,4,5]
Output: true
Example 2:

Input: \[5,4,3,2,1]
Output: false

## 描述

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr\[i] < arr[j] < arr\[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: \[1,2,3,4,5]
输出: true
示例 2:

输入: \[5,4,3,2,1]
输出: false

### 思路

* 声明三个变量 i，j，k 用于表示 nums\[i] \< nums\[j] \< nums\[k]
* 首先遍历数组，找到第一对满足 nums\[i] \< nums\[j] 的数。
* 然后，另 k = j + 1，这个时候我们考虑以下情况
* 1. 如果 nums\[k] 大于 nums\[j] 说明已经有三个数满足条件，我们返回 True；
* 2. 如果 nums\[k] 在 nums\[i] 和 nums\[j] 中间，那么只要后面有一个数大于 nums\[j], 就一定会大于 nums\[k],于是我们更新 j = k；
* 3. 如果 nums\[k] 小于 nums\[i]，说明我们找到了更小的数，更新 i = k。此时依然有 nums\[i]<\nums\[j],但是 j \< i，不影响判断的逻辑。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-28 10:02:55
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-28 11:08:49


class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        # 声明三个索引变量，用于记录满足条件的之
        i, j, k = 0, 1, 1
        # 元素的个数
        count = len(nums)
        # 找到数组中最前面递增的两个数
        while i < count and j < count and nums[i] >= nums[j]:
            i += 1
            j += 1
        # k 更新为 j 后面的那一个数
        k = j + 1
        while k < count:
            # 如果 nums[k] 比 nums[j] 大，说明已经有三个数满足条件
            if nums[k] > nums[j]: return True
            # 如果 nums[k] 在 nums[i] 和 nums[j] 中间，我们丢掉 nums[j]
            # 更新现有的 j 为 k，因为如果接下来有个数比 nums[j]大，那么一定比 nums[k] 大
            if nums[i] < nums[k] <= nums[j]: j = k
            # 如果 nums[k] 比 nums[i] 还小，我们更新 i 
            if nums[k] <= nums[i]: i = k
            k += 1
        # 前面没有满足条件的数，返回 False
        return False
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-28-334-Increasing-Triplet-Subsequence.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-334-increasing-triplet-subsequence/) ，作者信息和本声明.
