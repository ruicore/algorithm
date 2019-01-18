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
