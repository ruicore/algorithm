# LeetCode 151. Reverse Words in a String

## Description

Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

## 描述

给定一个字符串，逐个翻转字符串中的每个单词。

示例:  

输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
### 实现

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 09:50:21
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 10:01:15


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        relist = s.split(" ")
        if not relist:
            return ''
        res = ''
        for i in range(len(relist) - 1, -1, -1):
            if relist[i]:
                res += relist[i] + " "
        return res[:-1]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-15-151-Reverse-Words-in-a-String.py).
©本文首发于[何睿的博客](https://wp.me/paizn9-12I)，欢迎转载，转载需保留文章来源，作者信息和本声明.
