# LeetCode 242. Valid Anagram

## Description

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

## 描述

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

### 思路

* 字母异位词是指使用了相同的字母（种类相同，且每个种类使用的次数相等）的单词.
* 题目给定了只会使用小写字母，我们生命两个长度为26的数组，统计s和t中字母出现的次数，然后判断所有的字母是不是一一对应相等即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 16:55:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 18:05:09


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        # 题目明确只会给定26个小写字母
        scount, tcount = [0 for _ in range(26)], [0 for _ in range(26)]
        for x, y in zip(s, t):
            # 统计s中字母出现的次数
            scount[ord(x) - ord('a')] += 1
            # 统计t中字母出现的次数
            tcount[ord(y) - ord('a')] += 1
        # 返回s和t中字母出现的次数是否一一对应相等
        return scount == tcount
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-02-242-Valid-Anagram.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-242-valid-anagram/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
