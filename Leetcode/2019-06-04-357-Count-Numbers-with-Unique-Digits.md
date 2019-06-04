# LeetCode 357. Count Numbers with Unique Digits

## Description

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

## 描述

给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91 
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

### 思路

* 此题目类似排列组合。
* 当 n = 1，10 的 1 次方为 10（不含），此时等价于问一个最多有 1 位数的数字，最多有多少个 unique number。
* 当 n = 2，10 的 2 次方为 100（不含），此时等价于问一个最多有 2 位数的数字，最多有多少个 unique number。
* 当 n = 1，不重复的数有 10 个，从 0 到 9 任选一个都行。
* 当 n = 2，1 位数最多有 10个；2位数的最高位不能选 0，因此有 9 种选择，次高位不能选最高位选过的，因此有 10 - 1 共 9 种选择，共 81 个；于是共计 91 个。
* 当有 3 位时，3位数的最高位有 9 种选择，次高位有 9 种选择，最末位有 8 种选择，共 405 个三位数；加上当 n 为2 的 91 个数，共496 个数。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-04 13:40:45
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-04 14:57:30


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # n 最大为 9
        n = n if n < 10 else 9
        # 当 n 为 0 时，只有 0 满足条件
        if n == 0: return 1
        # count 记录当限定位数为 i 时，能够形成的做多的 unique number 个数
        # res 记录总和
        count, res = 9, 10
        for i in range(2, n + 1):
            count *= 11 - i
            res += count

        return res
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-06-04-357-Count-Numbers-with-Unique-Digits.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留[文章来源](https://www.ruicore.cn/leetcode-357-count-numbers-with-unique-digits/) ，作者信息和本声明.
