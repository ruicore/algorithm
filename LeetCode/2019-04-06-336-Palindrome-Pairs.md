# LeetCode 336. Palindrome Pairs

## Description

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: \["abcd","dcba","lls","s","sssll"]
Output: \[\[0,1],\[1,0],\[3,2],\[2,4]] 
Explanation: The palindromes are \["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: \["bat","tab","cat"]
Output: \[\[0,1],\[1,0]] 
Explanation: The palindromes are \["battab","tabbat"]

## 描述

给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: \["abcd","dcba","lls","s","sssll"]
输出: \[\[0,1],\[1,0],\[3,2],\[2,4]] 
解释: 可拼接成的回文串为 \["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: \["bat","tab","cat"]
输出: \[\[0,1],\[1,0]] 
解释: 可拼接成的回文串为 \["battab","tabbat"]

### 思路

* 构建字典，字典的键为单词，值为单词的索引。
* 遍历每一个单词，对每一个单词进行切片，组成 prefix 和 subfix。
* 如果 prefix 本身是回文字符串，我们检查 subfix 的反转是否在字典中，如果在，说明可以构成一个满足题意的回文字符串，我们将该键的值，当前单词的索引构成一个组合（注意顺序）。
* 如果 subfix 是一回文字符串，我们检查 prefix 的反抓是否在字典中，如果在，说明可以构成一个满足题意的回文字符串，我们将当前单词的索引，该键的值构成一个组个（注意顺序）
* 注意在检查回文字符串的时候，注意重复。
 
```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-06 12:11:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-07 10:20:01


class Solution:
    def palindromePairs(self, words: [str]) -> [[int]]:
        # 结果数组
        result = []
        # 字典，用于获取索引
        worddict = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            count = len(word)
            for j in range(count + 1):
                # 获取字段的前半部分，后半部分
                prefix, subfix = word[:j], word[j:]
                # 前半部分的反转，后半部分的反转
                reprefix, resubfix = prefix[::-1], subfix[::-1]
                # 如果前半部分是 palindrome 并且后半部分的反转在字典中
                if prefix == reprefix and resubfix in worddict:
                    m = worddict[resubfix]
                    # 不能取到字符本身
                    if m != i: result.append([m, i])
                # 如果后半部分是回文字符串，并且前半部分的逆序在字典中
                if j != count and subfix == resubfix and reprefix in worddict:
                    result.append([i, worddict[reprefix]])
        return result
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-06-336-Palindrome-Pairs.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-336-palindrome-pairs/) ，作者信息和本声明.
