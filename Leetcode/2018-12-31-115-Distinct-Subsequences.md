# LeetCode 115. Distinct Subsequences

## Description

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

```python
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```

Example 2:

```python

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```

## 描述

给定字符串S和字符串T，计算S的不同子序列的数量，使其其等于T.

字符串的子序列是一个新字符串，它是通过删除一些（可以是无）字符而不干扰其余字符的相对位置而从原始字符串形成的。 （即，“ACE”是“ABCDE”的子序列，而“AEC”不是）。

### 思路

* 题意是将S作为来源字符串，T作为目标字符串，从S种按顺序地取出不同字符，使其等于T，每个字符只能取一次.
* 此题目使用[动态规划](https://zh.wikipedia.org/zh-hans/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92).
* 我们令 row = len(t)+1, col = len(s)+1,我们声明一个二维矩阵matrix\[row]\[col].(以下字符串s和t下标从1开始)
* matrix\[i]\[j] 表示从S\[1:j]中取字符串构成T\[1:i]一共有多少种取法.

1. 假设我们已经知道了matrix\[i]\[j-1], matrix\[i-1]\[j-1]的值.
2. 为了求得matrix\[i]\[j]，我们思考matrix\[i]\[j-1]表示在s\[1:j-1]取字符变成t\[1:i]的方法数，而这里的所有方法在把s\[1:j]变成t\[1:i]同样适用\(因为我们只是在来源字符串后面增加了一个字符)，我们再思考如果s\[j]==t\[i],那么把s\[1:j-1]变成t\[1:i-1]的取法在把s\[1:j]变成t\[1:i]一样适用(因为此时我们相当于只是在两个字符串后面增加了一个相等的字符).
3. 如果s\[j]!=t\[i],则只有matrix\[i]\[j-1]种取法.

* 即转移方程为

$$  matrix[row][col] = matrix[row-1][col-1] + matrix[row][col-1]  \quad **or**  \quad matrix[row][col] = matrix[row][col-1] $$

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 15:52:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 17:07:43


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # 我们人为的在s和t中的首位置增加一个空字符
        # 行数和列数
        # 以目标字符串t作为行数，来源字符串s作为列数（反之也可以）
        row, col = len(t)+1, len(s)+1
        # 初始花二维矩阵
        matrix = [[0 for _ in range(col)] for _ in range(row)]
        # 矩阵的matrix[0][0]置为1，表示从来源字符串中取空个字符串够成目标字符串中的空个字符有1种方法
        matrix[0][0] = 1
        # 初始化第一行，表示从来源字符串s中取字符构成目标字符串t的第一个字符（空字符）只有1种方法
        for i in range(1, col):
            matrix[0][i] = 1
        # 初始化第第一列，表示取来源字符串中的第一个字符（空字符）构成t[1:i]有0种方法
        for i in range(1, row):
            matrix[i][0] = 0
        for i in range(1, col):
            for j in range(1, row):
                # 如果当前来源字符s[i-1]与目标字符t[j-1]相等
                if t[j-1] == s[i-1]:
                    matrix[j][i] = matrix[j-1][i-1]+matrix[j][i-1]
                else:
                    matrix[j][i] = matrix[j][i-1]
        # 最终结果存储在矩阵右下角
        return matrix[row-1][col-1]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-31-115-Distinct-Subsequences.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-115-distinct-subsequences/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
