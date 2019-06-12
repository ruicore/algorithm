# LeetCode 350. Intersection of Two Arrays II

## Description

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = \[1,2,2,1], nums2 = \[2,2]
Output: \[2,2]
Example 2:

Input: nums1 = \[4,9,5], nums2 = \[9,4,9,8,4]
Output: \[4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

## 描述

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = \[1,2,2,1], nums2 = \[2,2]
输出: \[2,2]
示例 2:

输入: nums1 = \[4,9,5], nums2 = \[9,4,9,8,4]
输出: \[4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

### 思路

* 对数组进行排序。
* 对每个数组分别用一个指针 i，j，如果 i，j 指向的元素相等，则将这个元素放入到结果数组中，i， j 同时向后走一步。
* 如果 i 所在的元素大，则 j 向后走一步。
* 如果 j 所在的元素大，则 i 向后走一步。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-09 16:31:05
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-09 16:43:17


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort(), nums2.sort()
        count1, count2 = len(nums1), len(nums2)
        i, j, res = 0, 0, []
        # 相同的部分一定在前面
        while i < count1 and j < count2:
            # 如果相等，添加到结果数组中
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i + 1, j + 1
            # 如果数组二的数大，将数组一的索引自增一次
            elif nums1[i] < nums2[j]:
                i += 1
            # 如果数组一的数大，将数组二的索引自增一次
            elif nums1[i] > nums2[j]:
                j += 1

        return res
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-09-350-Intersection-of-Two-Arrays-II.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-350-intersection-of-two-arrays-ii/) ，作者信息和本声明.
