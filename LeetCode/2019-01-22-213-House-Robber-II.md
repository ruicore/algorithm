# LeetCode 213. House Robber II

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

## 描述

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

### 思路

* 此题目同[198题HouseRobber](https://leetcode.com/problems/house-robber)类似，不同之处是第一个房子和最后一个房子不能够同时偷.
* 为了解决这个问题，我们使用两组数据，每一组数据两个值，其中一组同198题目一样，从第一个房子开始偷(标号为0)，偷第一个房子：frob（偷当前房子）, fnotrob（不偷当前房子）;另一组数据从第二个房子开始偷rob(偷当前房子), notrob（不偷当前房子）；由于frob既偷了第一房子，又投了最后一个房子，不合题意，我们返回剩下的三个数中的最大值即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 19:43:49
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 20:06:11


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果没有房子可偷，返回0
        if not nums: return 0
        # 如果只有一个房子可以偷，返回其值
        if len(nums) == 1: return nums[0]
        # 偷第一个房子：偷当前房子，不偷当前房子;不偷第一个房子：偷当前房子，不偷当前房子
        frob, fnotrob, rob, notrob = nums[0], 0, 0, 0
        for item in nums[1:]:
            # 获取最大值
            _max = max(frob, fnotrob)
            # 偷当前房子则不能偷前一个房子
            frob = item + fnotrob
            # 不偷当前房子，则为昨天偷或不偷的最大值
            fnotrob = _max
            _max = max(rob, notrob)
            rob = item + notrob
            notrob = _max
        # 这里应该返回fnotrob, rob, notrob的最大值
        # 但是不偷第二个房子notrob一定小于等于偷第二个房子rob
        return max(fnotrob, rob)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-22-213-House-Robber-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-213-house-robber-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
