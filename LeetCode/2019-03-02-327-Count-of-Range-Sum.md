# LeetCode 327. Count of Range Sum

## Description

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

## 描述

给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3 
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

### 思路

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-02 15:54:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-02 20:40:27

import bisect


class Solution:
    def countRangeSum(self, nums: [int], lower: int, upper: int) -> int:
        presum, _sum, count = [0], 0, 0
        for num in nums:
            _sum += num
            right = bisect.bisect_right(presum, _sum - lower)
            left = bisect.bisect_left(presum, _sum - upper)
            count += right - left
            bisect.insort(presum, _sum)
        return count
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-02-327-Count-of-Range-Sum.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-327-count-of-range-sum/) ，作者信息和本声明.
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-327-count-of-range-sum/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-327-count-of-range-sum/) ，作者信息和本声明.
微信公众号：techruicore 
