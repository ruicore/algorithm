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
        # 也可以用循环，如 maxProduct2，但是在 python 中 itertools.combinations 更快
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
