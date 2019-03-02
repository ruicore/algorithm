# LeetCode 326. Power of Three

## Description

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false

## 描述

给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？

### 实现

* 使用对数函数可以不使用循环.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-02 15:38:41
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-02 15:39:03

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 3**round(math.log(n, 3)) == n if n > 0 else False
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-02-326-Power-of-Three.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-326-power-of-three/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-326-power-of-three/) ，作者信息和本声明.
微信公众号：techruicore 
