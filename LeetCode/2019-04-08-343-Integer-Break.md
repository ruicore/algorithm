# LeetCode 343. Integer Break

## Description

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

## 描述

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

### 思路

* 动态规划，前五个数的最大乘积为 1, 2, 4, 6, 9，后面的第 i 个数的最大乘积，由从后往前数（包括 i 本身）的第三个数乘以 3 得到。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 17:35:39
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 18:15:43


class Solution:
    def integerBreak(self, n: int) -> int:
        # 前 5 个数的最大乘积
        tmp = [1, 2, 4, 6, 9]
        for i in range(5, n - 1):
            # 动态规划：第 i 个数 的最大乘积为 3 * 往前数第三个数
            tmp.append(3 * tmp[i - 3])
        return tmp[n - 2]

    def integerBreak2(self, n: int) -> int:
        # 思路与上面的思路一致，优化了空间
        if n == 2: return 1
        if n == 3: return 2
        tmp = [4, 6, 9]
        for i in range(n - 6):
            tmp[i % 3] *= 3
        return tmp[(n - 1) % 3]
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-08-343-Integer-Break.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-343-integer-break/) ，作者信息和本声明.
