# LeetCode 367. Valid Perfect Square

## Description

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

## 描述

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False

### 思路

* 用二分法对一个正数开方，如果存在一个正整数 t ，并且 t 的平方等于给定的数，说明该数是完全平方数。
* 考察基本的二分法。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-13 14:35:51
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-13 14:42:06


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            middle = left + ((right - left) >> 1)
            tmp = middle ** 2
            if tmp == num:
                return True
            elif tmp < num:
                left = middle + 1
            else:
                right = middle - 1

        return False
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-06-13-367-Valid-Perfect-Square.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-367-valid-perfect-square/) ，欢迎转载，转载需保留 文章来源 ，作者信息和本声明.
