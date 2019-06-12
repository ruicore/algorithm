# LeetCode 166. Fraction to Recurring Decimal

## Description

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

## 描述

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

### 实现

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 14:57:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 15:16:35


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        # 确定是不是负数
        isnegative = True if numerator * denominator < 0 else False
        # 返回商和余数
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        # 生成点号左边的部分
        s = str(quotient)
        if isnegative: s = "-" + s
        if remainder: s += '.'
        # start用于记录循环开始的位置
        start = len(s)
        nums = {remainder: start}
        while remainder:
            # 对剩下的数字进行计算
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            # 添加到已经生成的结果中
            s += str(quotient)
            # 如果当前的余数已经出现过了
            if remainder in nums:
                s = s[:nums[remainder]] + '(' + s[nums[remainder]:] + ')'
                return s
            start += 1
            nums[remainder] = start
        return s
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-166-Fraction-to-Recurring-Decimal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-166-fraction-to-recurring-decimal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
