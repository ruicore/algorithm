# LeetCode 201. Bitwise AND of Numbers Range

## Description

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

## 描述

给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

### 思路

* 本题目考察位运算.
* 相当于求第一个数和最后一个数前缀相同的部分，后面不同的部分用0补齐.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 21:06:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 18:21:42

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        diff = 0
        while m - n:
            diff += 1
            m >>= 1
            n >>= 1
        return m << diff
```

源代码文件在[这里](https://github.com/ruicore).
©本文是原创文章，欢迎转载，转载需保留[文章来源](https://www.ruicore.cn/)，作者信息和本声明.
©本文首发于[何睿的博客](https://www.ruicore.cn/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
