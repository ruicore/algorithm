# LeetCode 217. Contains Duplicate

## Description

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

## 描述

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

### 思路

* 这道题的解法很多，在python中，set数据结构不存储重复元素，所有我们可以把所有的元素添加到set中，如果set中元素个数与原数组中的元素个数相等说明没有重复，否则说明有重复.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-24 19:13:41
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 20:56:11


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 如果没有重复，那么这两种数据结构的元素个数应该相等
        return len(set(nums)) - len(nums) != 0
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-24-217-Contains-Duplicate.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-217-contains-duplicate/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
