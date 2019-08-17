# LeetCode 392. Is Subsequence

## Description

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

## 描述

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 依次检查 s 中的每个字符是否出现在 t 中，并且要求 s 中后面的字符的在 t 中出现的位置对应递增。
* 当有很多个 s ，只有一 t 个时，可以考虑用字典对 t 建立索引。键为 t 中的字符，值为 t 对应字符出现过的所有索引（递增）。
* 查询 s 中的字符时，使用二分搜索，要求 s 中后一个字符的在 t 中的索引大于前一个字符的索引。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-17 13:53:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-17 14:34:16

import bisect
from collections import defaultdict


class Solution:
    def __init__(self):
        self.__isinit = False
        self.__dict = defaultdict(list)

    def __build(self, t):
        for index, char in enumerate(t):
            self.__dict[char].append(index)
        self.__isinit = True

    def isSubsequence(self, s: str, t: str) -> bool:
        if not self.__isinit:
            self.__build(t)

        next_ = -1
        for char in s:
            next_ = self.__check(char, next_)
            if next_ == -1:
                return False

        return True

    def __check(self, char, index):
        if char not in self.__dict:
            return -1
        next_ = bisect.bisect_right(self.__dict[char], index)
        return self.__dict[char][next_] if next_ < len(self.__dict[char]) else -1
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-08-17-392-Is-Subsequence.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-392-is-subsequence/) ，作者信息和本声明.
