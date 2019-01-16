# LeetCode 168. Excel Sheet Column Title

## Description

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

## 描述

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

### 思路

* 这道题目相当于进制转换.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 18:54:24
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 19:00:18


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 此题目相当于进制转换
        s = []
        while n > 0:
            # 索引转换
            n -= 1
            s.append(chr(65 + int(n % 26)))
            n = n // 26
        return ''.join(reversed(s))
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-168-Excel-Sheet-Column-Title.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/168-excel-sheet-column-title/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
