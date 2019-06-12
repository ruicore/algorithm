# LeetCode 205. Isomorphic Strings

## Description


Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

## 描述

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true

### 思路

* 这道题我们使用一个字典，键为s中的字符，值为t中的字符，我们要求键和值要一一对应.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-21 11:56:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 19:36:15


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 字典，键为s中的字符，值为t中的字符
        # 键和值必须一一对应
        res = {}
        for x, y in zip(s, t):
            # 若键存在，则其值一定要和y相等
            if x in res:
                if not res.get(x) == y: return False
            else:
                # 若y已经作为其他键的值，直接返回False，因为这里要求键值一一对应
                if y in res.values(): return False
                else: res[x] = y
        # 上面的条件都满足，返回True
        return True
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-21-205-Isomorphic-Strings.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-205-isomorphic-strings/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
