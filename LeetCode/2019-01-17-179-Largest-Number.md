# LeetCode 179. Largest Number

## Description

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

## 描述

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

### 思路

* 对数组进行排序，我们修改排序的依据即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 21:52:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-18 17:25:13

import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 对数组进行排序
        nums.sort(key=functools.cmp_to_key(self._sort))
        res = ''.join(map(str, nums))
        if res[0] == '0': return '0'
        return res

    def _sort(self, num1, num2):
        # 修改排序规则
        a = str(num1) + str(num2)
        b = str(num2) + str(num1)
        if a > b: return -1
        if a < b: return 1
        return 0
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-17-179-Largest-Number.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-179-largest-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
