# LeetCode 131. Palindrome Partitioning

## Description

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

## 描述

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

### 思路

* 此题目使用[深度优先搜索](https://zh.wikipedia.org/zh-hans/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2).
* 我们找到一个回文字符后，在剩下的字符中继续寻找回文字符串，直到结束.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-06 17:49:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-06 21:41:22


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(res, [], s)
        return res

    def dfs(self, res, path, s):
        # 递归结束条件，当s为空则将path所有的字符添加到结果数组中
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            # 判断是否是回文字符串
            sub = s[0:i]
            if sub == sub[::-1]:
                # 如果当前的字符串是回文字符串，保存当前的字符串
                # 继续判断字符串中剩下的字符哪个地方能构成回文字符串
                self.dfs(res, path+[sub], s[i:])
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-06-131-Palindrome-Partitioning.py).
©本文是原创文章，欢迎转载，转载需保留[文章来源](https://www.ruicore.cn/)，作者信息和本声明.
©本文首发于[何睿的博客](https://www.ruicore.cn/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
