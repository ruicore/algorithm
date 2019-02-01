# LeetCode 233. Number of Digit One

## Description

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

## 描述

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6 
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

### 思路

* 这道题是找规律的题目.
* 我们每一位每一位进行运算.
* 如上图，以百位middle为例：
1.如果百位为0，则我们另百位为1，个位和十位构成的数字right从0取到99，有100种取法，前面部分的构成的数字从0取到9765，一共有9766中取法，也就是说在给定值的百位为0情况下，小于该数字的所有数字中，百位为1的有9766\*100个数字.
2.如果百位本身为1，那么个位和十位构成的数字right从0取到99，有仍然有100种取法，前面部分的构成的数字从0取到9765，一共有9766中取法，百位本身为1，我们另百位前面所有的数不变，仍然有19（right）种取法，所以在定值的百位为0情况下，小于该数字的所有数字中，百位为1的有9766\*100+right个数字.
3.如果给定的百位数大于1，可以分析得出一共有（right+1)\*100种取法.
4.同理其他情况也一样.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 12:57:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 14:28:55


class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        # 如果是负数，直接返回零
        if n <= 0: return res
        # 当前位置左边的所有数，当前位置的值，当前位置右边的值
        left, right, middle, factor = 1, 1, 1, 1
        # 循环条件，当left不为零（即左边还有数的时候）
        while left:
            # 取左边部分
            left = n // (factor * 10)
            # 取当前位置的值
            middle = n // factor % 10
            # 取当前位置右边的值
            right = n % factor
            # 如果当前位置的值为0
            if middle == 0:
                res += left * factor
            # 如果当前的值为1
            elif middle == 1:
                res += left * factor + right + 1
            # 如果当前的值大于等于2
            else:
                res += (left + 1) * factor
            factor *= 10
        # 返回最终的结果
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-01-233-Number-of-Digit-One.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-233-number-of-digit-one/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
