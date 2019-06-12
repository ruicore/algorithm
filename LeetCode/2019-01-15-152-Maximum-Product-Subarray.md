# LeetCode 152. Maximum Product Subarray

## Description

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

## 描述

给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

### 思路

* 在一个连续的不含零的数组中，如果有偶数个负数，则最大值为所有值的乘积（所有的数都是整数，且不含零），如果有奇数个负数，为了取得最大值我们会尽可能使得序列包含更多的数，因此我们会舍弃第一个负数左边的序列或者最后一个负数右边的序列.
* 基于这个思想，我们首先将给定的数组以0切片，切片的同时记录该片中负数的个数，然后求该片中的最大值，最后的结果为所有值的最大值.
* 求每以片的最大值的过程是，如果有偶数个负数，则返回所有数的乘积；如果有奇数个乘积，我们首先找到第一个负数和最后一个负数，然后计算从第一个负数（不包含）到最后一个负数（不包含）中间的乘积middle,然后计算第一个负数（包含）左边的乘积left，计算最后一个负数（包含）右边的乘积right，返回middle\*left，middle\*right中的较大值.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 10:11:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 12:37:11

from functools import reduce


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = nums[0], 0
        start, end = 0, 0
        for i in range(len(nums)):
            if nums[i] < 0:
                count += 1
            # 当遇到0或者到达末尾时就进行切片
            if nums[i] == 0 or i == len(nums) - 1:
                # 不包括元素num[i]本身
                end = i - 1 if nums[i] == 0 else i
                res = max(res, nums[i], self._product(start, end, count, nums))
                start, count = i + 1, 0
        return res

    def _product(self, start, end, count, nums):
        # 计算连续数字乘机最大值
        if start > end:
            return 0
        # 如果负数有偶数个，则所有值的连续相乘的积就是最大值
        if not count % 2:
            return reduce(lambda x, y: x * y, nums[start:end + 1])
        # 如果有奇数个负数，则我们应该丢掉第一个负数左边的片段或者最后一个负数右边的片段
        first, last = 0, 0
        # 寻找第一个负数的索引
        for i in range(start, end + 1):
            if nums[i] < 0:
                first = i
                break
        # 寻找最后一个负数的索引
        for i in range(end, start - 1, -1):
            if nums[i] < 0:
                last = i
                break
        # 如果第一个负数和最后一个负数不重合
        if first != last:
            # 计算从nums[first + 1:last]的乘机
            middle = reduce(lambda x, y: x * y, nums[first + 1:last])
            # 计算第一个负数左边的乘积（包括第一个负数本身）
            left = reduce(lambda x, y: x * y, nums[start:first + 1])
            # 计算最后一个负数右边的乘积（包括最后一个负数本身）
            right = reduce(lambda x, y: x * y, nums[last:end + 1])
        # 如果第一个负数和最后一个负数重合，即只有一个负数
        else:
            # 令中间的值为1
            middle = 1
            left = reduce(lambda x, y: x * y,nums[start:first]) if start != first else nums[start]
            right = reduce(lambda x, y: x * y,nums[last + 1:end + 1]) if last != end else nums[end]
        # 分别计算中间乘积与左边的乘积，中间乘积与右边的乘积
        res1, res2 = middle * left, middle * right
        # 返回最大值
        return res1 if res1 > res2 else res2
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-15-152-Maximum-Product-Subarray.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-152-maximum-product-subarray/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
