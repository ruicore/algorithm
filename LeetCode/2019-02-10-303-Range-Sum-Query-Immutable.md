# LeetCode 303. Range Sum Query - Immutable

## Description

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

```py
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

## 描述

给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

```py
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

### 思路

* 使用动态规划.
* 创建一个新数组sum，数组位置i的值表示给定数组0到i的和.这样当要求i到j的值是返回sum\[j]-sum\[i]即可.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-10 21:56:48
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-10 22:02:19


class NumArray:
    def __init__(self, nums: 'List[int]'):
        # 对给定的数组的前面的数求和
        if not nums:
            self.sum = []
        else:
            self.sum = [nums[0]] * len(nums)
            for i in range(1, len(nums)):
                self.sum[i] = self.sum[i - 1] + nums[i]

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        # 做差返回对应序列的值
        return self.sum[j] - self.sum[i - 1] if i > 0 else self.sum[j]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-10-303-Range-Sum-Query-Immutable.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-303-range-sum-query---immutable/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
