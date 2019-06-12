# LeetCode 128. Longest Consecutive Sequence

## Description

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## 描述

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

### 思路

* 此题目使用哈希表.
* 以数字为键，值为以当前数字为边界的最长字串（若当前数字在左边则为左边界，在右边则为右边界）,构造字典（哈希表）mydict.
* 给定数组nums,假设我们已经知道了leftborfer = mydict\[nums\[i-1]]为边界的最长子串个数（无论nums\[i-1]为左边界还是右边界），rightborder = mydict\[nums\[i+1]]为边界的最长子串个数，则nums\[i]所在的最长字串为length = leftborfer + 1 + rightborfer.
* 然后我们更新此连续串的边界长度mydict\[nums\[i]- leftborfer]=length,mydict\[nums\[i] + rightborfer]=length.
* 我们返回其中的最大值即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-05 16:22:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-05 17:14:04

from pprint import pprint


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 哈希表，结果
        mydict, res, = {}, 0
        # 遍历所有数字
        for item in nums:
            # 重复的数字不算
            if item in mydict:
                continue
            # 获取当前数字左边一个数字构成的最大连续串，若不存在则返回0
            leftborder = mydict.get(item-1, 0)
            # 获取当前数字右边一个数字构成的最大连续串，如不存在则返回0
            rightborder = mydict.get(item+1, 0)
            # 连续串的长度更新为左右最大连续串加一
            length = leftborder+rightborder+1
            mydict[item] = length
            res = max(res, length)
            # 更新左边界
            mydict[item-leftborder] = length
            # 更新右边界
            mydict[item+rightborder] = length
        return res

```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-05-128-Longest-Consecutive-Sequence.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-128-longest-consecutive-sequence/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
