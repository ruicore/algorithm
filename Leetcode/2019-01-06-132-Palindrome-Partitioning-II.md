# LeetCode 132. Palindrome Partitioning II

## Description

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

```python
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

## 描述

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

### 思路

![LeetCode 132. Palindrome Partitioning II](https://wp.me/aaizn9-119)

* 此题主要使用[动态规划](https://zh.wikipedia.org/zh-hans/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92).
* 我们用一个row,col=len(s),len(s)的二维矩阵matrix来存储状态,matrix\[i]\[j]表示s\[i:j+1]是否是一个回文字符串.
* 初始状态：matrix\[i]\[j]均为False.
* 转移方程：我们要求s\[0:j]需要切割多少次才能使得都变成回文字符串,i<\j,若s\[i]==s\[j],并且s\[i+1:j-1]是回文字符串，则s\[i:j]是回文字符串，那么我们只需要在s\[i-1]分割一次，就可以把s\[j]都分割成回文字符串.
* 即若s\[i]==s\[j] and s[i+1:j-1] 是回文字符串 则：cust\[j]=cuts\[i-1]+1
* 我们继续思考，如果i和j之间只相隔一个单词或者i和j之间没有单词，则s\[i;j]也是回文字符串.
* 即转移方程为：若s\[i]==s\[j] and (s[i+1:j-1]是回文字符串 或 i，j之间相隔小于等于1个单词）则：cust\[j]=cuts\[i-1]+1.
* 结果：cuts的最后一个元素.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-06 21:42:13
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-06 22:54:54


class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return 0
        # 矩阵的行数和列数
        row, col = len(s), len(s)
        # 初始化矩阵，matrix[i][j]表示s[i:j+1]是否是回文字符串
        matrix = [[False for _ in range(col)] for _ in range(row)]
        # cuts[i]表示s[:i+1]最少需要的切割步数
        cuts, res = [0 for _ in range(row)], row-1
        # 遍历每一个节点
        for end in range(row):
            # s[i]最多切割i次（即i+1个字符最多需要i次切割）
            res = end
            # 检查回文字符串
            for start in range(end+1):
                # 转移条件与转移方程
                # 如果当前字符s[start]与目前正在判断的字符s[end]相等并且
                # 如果从start+1到end-1的连续字符s[start+1:end]构成的字符串是回文字符串(注意: python语法:如s[0:4]不包括末尾字符s[4]))
                # 或者start与end之间的字符小于等于1个，则cuts[i]=cuts[start-1]+1
                # 即从s[start-1]之后再次切割一次，s[i]就可以构成回文字符串.
                if s[start] == s[end] and (end-start <= 2 or matrix[start+1][end-1]):
                    res = min(res, cuts[start-1]+1) if start > 0 else 0
                    matrix[start][end] = True
            cuts[end] = res
        # 或者 cuts[end]
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-06-132-Palindrome-Partitioning-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-132-palindrome-partitioning-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
