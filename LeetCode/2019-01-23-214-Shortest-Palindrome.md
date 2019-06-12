# LeetCode 214. Shortest Palindrome

## Description

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"

## 描述

给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"

### 思路

* 我们先找到给定的字符串中的最大回文字符串（字符串必须从左端开始），然后将字符串中剩余的字符串反转添加到原字符串头部即可.
* 关于如何找到从起点开始的最长回文字符串，最直观的方式是从字符串最右边开始判断，直到找到回文字符串，这样做可行，但是会超时.
* 我们使用KMP算法中初始化next数组的算法来解决此题目,有关KMP算法的详细解释，请参考这个[视频](https://www.youtube.com/watch?v=V5-7GzOfADQ).
* 我们另s\`=原字符串s的反转，我们将s和s\`用一个特殊字符（如"$"）连接起来，根据KMP的next定义，next\[i]=j表示字符串从索引i位置，往前数（包括本身i）,有j个字符与从字符串开头数起的j个字符一一对应相同.于是next的最后一个位置的值next\[-1]就表示从最后一个位置往前数起有next\[-1]字符与从字符串开头的next[\-1]字符一一相等.也就求得了原字符串中回文字符串的个数.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-23 19:08:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-25 22:38:27

class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # KMP next 数组
        _next = [0] * (2 * len(s) + 1)
        # 重新拼接字符串
        news = s + "$" + "".join(list(reversed(s)))
        j = 0
        # 构造_next数组
        for i in range(1, len(news)):
            if news[i] == news[j]:
                _next[i] = j + 1
                j += 1
            else:
                while j != 0 and news[i] != news[j]:
                    j = _next[j - 1]
                if news[i] == news[j]:
                    _next[i] = j + 1
                    j += 1
        return news[len(s) + 1:len(s) + len(s) - _next[-1] + 1] + s
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-23-214-Shortest-Palindrome.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-214-shortest-palindrome/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
