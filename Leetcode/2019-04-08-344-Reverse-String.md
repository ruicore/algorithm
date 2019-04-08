# LeetCode 344. Reverse String

## Description

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

## 描述

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

### 思路

* 第一个位置的元素和嘴后一个位置的元素交换，第二个和倒数第二个，第三个和倒数第三个 ...

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 21:47:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 21:54:18


class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 中间位置的索引，最后一个位置的索引
        half, count = len(s) // 2, len(s) - 1
        for i in range(half):
            s[i], s[count - i] = s[count - i], s[i]
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-08-344-Reverse-String.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-344-reverse-string/) ，作者信息和本声明.
