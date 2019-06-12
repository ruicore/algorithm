# LeetCode 300. Longest Increasing Subsequence

## Description

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: \[10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is \[2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

## 描述

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: \[10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 \[2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。

### 思路

* 这道题目使用动态规划.
* 状态：声明一个同给定数组一样长度的数组count，数组的每个位置的值表示以当前位置的数为最后一个数，当前位置（包括当前位置）的前面的数构成串的最长递增串中数字的个数，即nums\[3]=2表示前四个数中，以nums\[3]为最后一个数的最大递增串中数字的个数为2.
* 转移方程：对于第n个位置，由于我们已经知道了0到n-1每个位置的值，所以如果当前位置的元素大与0到n-1中的某个元素，当前数就能够添加到对应串的后面，即如果nums\[n]大于nums\[3],那么数nums\[n]就可以添加到串nums\[3]的后面，所以nums\[n]就可能为nums\[3]+1,对于nums\[4],nums\[5]也是同样的道理，所以count\[n]为数组nums从0到n-1中所有小于nums\[n]的数对应的count值加一的最大值.
* 最终结果：count数组的最大值
```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 18:23:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 18:23:33


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 数组的个数
        length = len(nums)
        # 如果数组中没有元素或者只有一个元素，直接返回数组长度
        if length <= 1: return length
        # 动态规划，数组没个位置初始化为1
        # 表示连续递增的序列长度最下为1
        count = [1] * length
        res = 0
        for i in range(1, length):
            # 初始化为1
            _max = 1
            # 从当前位置遍历到i
            for j in range(0, i):
                # 第i个数的最大值为0到i-1中所有小于当前元素能够称的连续序列加一的最大值
                if nums[j] < nums[i]: _max = max(count[j] + 1, _max)
            # 更新当前位置的最大值
            count[i] = _max
            # 记录所有值的最大值
            res = max(res, _max)
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-08-300-Longest-Increasing-Subsequence.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-300-longest-increasing-subsequence/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
