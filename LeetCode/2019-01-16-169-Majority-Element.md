# LeetCode 169. Majority Element

## Description

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

## 描述

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

### 思路

* 这道题的做法有很多，可以用hash表，可以排序，也可以用voting的方法，下面给出两种简单的实现.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 20:27:19
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 20:47:38


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 中间值一定会是超过一半的值
        return sorted(nums)[len(nums) // 2]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 超过了一半的值会使得count大于0
        majority, count = nums[0], 1
        for item in nums:
            if item == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = item
                count = 1
        return majority
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-169-Majority-Element.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-169-majority-element/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
