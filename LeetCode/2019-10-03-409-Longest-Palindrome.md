# LeetCode 409. Longest Palindrome

## Description

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

## 描述

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 统计所有单词出现的次数。
* 出现了偶数次的单词都以用来构成回文字符串，构成奇数次的单词减一次构成回文字符串。可以把奇数次的字符方中间，不需要和其它字符对应。因此奇数次的字符可以加一。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-03 14:41:25
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-03 14:56:07

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt_dict = Counter(s)
        a = sum(cnt_dict.values())
        b = sum(1 for x in cnt_dict.values() if x & 1)

        return a if b == 0 else a - b + 1
```

©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-409-longest-palindrome/) ，作者信息和本声明.
