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