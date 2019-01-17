# LeetCode 172. Factorial Trailing Zeroes

## Description

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

## 描述

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

### 实现

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 09:47:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-17 09:51:51


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n // 5
            n //= 5
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-17-172-Factorial-Trailing-Zeroes.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-172-factorial-trailing-zeroes/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
