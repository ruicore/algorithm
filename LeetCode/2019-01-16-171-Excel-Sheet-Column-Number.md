# LeetCode 171. Excel Sheet Column Number

## Description

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

## 实现

* 进制转换


```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 21:43:13
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 21:50:21


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base, res, count = 1, 0, len(s)
        for i in range(count):
            res += base * (ord(s[count - i - 1]) - 64)
            base *= 26
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-171-Excel-Sheet-Column-Number.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-171-excel-sheet-column-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
