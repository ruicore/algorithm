# LeetCode 318. Maximum Product of Word Lengths

## Description

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

```py
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
```

Example 2:

```py
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
```

Example 3:

```py
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
```

## 描述

给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

```py
输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
```

示例 2:

```py
输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
```

示例 3:

```py
输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
```

### 思路

* 基本思路很简单：对给定的单词两两组合，如果这两个单词没有相同的字符，记下者两个单词长度值的乘积，返回最大值。
* 如何判断两个单词是否使用了相同的单词：我们使用位运算，整形有 32 位，字符只有 26 个。
* 我们让二进制的数第一位表示 a ，第二位表示 b ... 第 26 位表示 z 。如果某个字母在给定的单词中出现了，我们记字母对应位置的二进制位 1 。
* 如果两个单词没有使用相同的字母，那么这两个单词对应的二进制按位与一定为 0 ，因为两个单词没有使用相同的字母，所以二进制中的 1 都是错开的。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-23 13:14:24
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-23 14:24:48

import itertools


class Solution:
    def maxProduct(self, words) -> int:
        # bits 是字典，键为单词 word 对应的二进制码，值为一个二进制码对应的最长单词
        # 最长单词：单词 a，aa，aaa，aaaa，对应的二进制码都是 0b1，为了获得最大的乘积
        # 我们取最长的单词 aaaa，所以 0b1 对应 4
        bits = {}
        for word in words:
            #  获取单词单词对应的 二进制码，有点类似哈希，但是不完全相同
            bit = self.getBit(word)
            # 建立键值对，这样可以避免多次 len(word)
            # 值为最长单词的长度
            bits[bit] = max(bits.get(bit, 0), len(word))
        # 对一个列表的所有元素进行两两组合
        # 也可以用循环，如 maxProduct2 中示例
        # 但是在 python 中 itertools.combinations 更快
        com = itertools.combinations(bits.keys(), r=2)
        # 对所有组合中单词没有重复的求乘积，这里也可以写成循环的形式
        # 但是在 python 中列表解析式的执行速度更快
        return max([bits[x] * bits[y] for x, y in com if x & y == 0] or [0])

    def maxProduct2(self, words) -> int:
        res = 0
        bits = [self.getBit(word) for word in words]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bits[i] & bits[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

    def getBit(self, word):
        bit = 0
        # 按位或
        # 字母 a 对一二进制第 1 位，b 对应第 2 位 ... z 对应 第 26 位
        for char in word:
            bit = bit | (1 << (ord(char) - 97))
        return bit
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-23-318-Maximum-Product-of-Word-Lengths.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-318-maximum-product-of-word-lengths/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-318-maximum-product-of-word-lengths/) ，作者信息和本声明.
