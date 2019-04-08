# LeetCode 345. Reverse Vowels of a String

## Description

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

## 描述

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

### 思路

* 这道题和上一道题目 [344 Reverse String](https://leetcode.com/problems/reverse-string) 做法基本一样，只是这里只需要交换原因字母。
* 找到所有的元音字母索引，第一个索引对应的元素和最后一个索引对应的元素交换，第二个和倒数第二个交换，第三个和倒数第三个交换。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 22:07:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 22:07:12


class Solution:
    def reverseVowels(self, s: str) -> str:
        # 所有的元音字母
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        index = [i for i in range(len(s)) if s[i] in vowels]
        half, count = len(index) // 2, len(index) - 1
        s = list(s)
        # 交换所有的原因字母
        for i in range(half):
            s[index[i]], s[index[count - i]] = s[index[count - i]], s[index[i]]
        return ''.join(s)
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-08-345-Reverse-Vowels-of-a-String.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-345-reverse-vowels-of-a-string/) ，作者信息和本声明.
