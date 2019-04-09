# LeetCode 349. Intersection of Two Arrays

## Description

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

## 描述

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

### 思路

* python 内置 set 集合可以完成交运算，然后再转换为 List 即可。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-09 16:11:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-09 16:15:56


class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        # python 内置集合运算
        return list(set(nums1) & set(nums2))
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-09-349-Intersection-of-Two-Arrays.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-349-intersection-of-two-arrays/) ，作者信息和本声明.
