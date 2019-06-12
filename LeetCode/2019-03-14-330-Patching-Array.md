# LeetCode 330. Patching Array

## Description

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0

## 描述

给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。

示例 1:

输入: nums = [1,3], n = 6
输出: 1 
解释:
根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
所以我们最少需要添加一个数字。
示例 2:

输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加 [2, 4]。
示例 3:

输入: nums = [1,2,2], n = 5
输出: 0

### 思路

* 贪心算法，每次都取最小的值把范围扩大更大。
* 对于给定的一个数组，假设前 k 个数字的和为 tmp （前 k 个数为 num\[0] ~ num\[k-1]），也就是说从 0 到 tmp 的所有的数我们都可以取到。
* 我们要扩大这个范围，如果 num\[k] 比 tmp + 1大，如果这个时候直接把 num\[k] 添加到数组中，那么 \[tmp+1,num\[k])之间的和是无法构造得到的。
* 于是我们将此时的边界 tmp + 1 作为需要的新的数添加到数组中；如果num\[k] 小于等于 tmp + 1，我们直接把 num\[k] 添加的数组中扩边界。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-14 20:40:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-14 21:57:33


class Solution:
    def minPatches(self, nums: [int], n: int) -> int:
        # tmp 表示所有数字的和，count表示需要添加数字，i 为索引
        # 定义[0,8) 8 为和的边界
        tmp, count, i = 0, 0, 0
        # 循环条件
        while tmp < n:
            # 如果 num[i] 在当前和的范围之内，那么把 num[i] 添加到
            # 当前的和范围内是最经济的做法
            if i < len(nums) and nums[i] <= tmp + 1:
                tmp += nums[i]
                i += 1
            # 否则，我们需要把当前和的边界的数字作为一个新的数字添加到和中
            else:
                tmp += tmp + 1
                count += 1
        return count
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-14-330-Patching-Array.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-330-patching-array/) ，作者信息和本声明.
