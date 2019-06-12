# LeetCode 187. Repeated DNA Sequences

## Description

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
Example:    
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

## 描述

所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
示例:
输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出: ["AAAAACCCCC", "CCCCCAAAAA"]

### 思路

* 题意是以10个字符构成每一个子串，寻找在字符串中出现了不止了一次的子字符串.
* 我们使用两个哈希set，wordset用于存储已经找到的子字符串，res用于存储已经出现的结果.我们以10个字符串为窗口，如果当前子字符串已经出现过在wordset中，我们就把他添加到res中，如果没有就添加到wordset中，最后我们返回list类型的res.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-18 19:56:00
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-18 20:10:34


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # wordset哈希set存储已经出现过的子字符串
        # res用于存储结果中的子字符串
        wordset, res, count = set(),set(), len(s)
        i = 0
        # 每一个窗口的长度为10
        while i + 10 <= count:
            # 如果当前字符串已经出现过，就把当前字符串添加到结果字符串中
            if s[i:i + 10] in wordset:
                res.add(s[i:i + 10])
            else:
                # 如果没有出现过，就添加到记录中
                wordset.add(s[i:i + 10])
            i += 1
        # 返回需要list类型
        return list(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-18-187-Repeated-DNA-Sequences.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-187-repeated-dna-sequences/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
