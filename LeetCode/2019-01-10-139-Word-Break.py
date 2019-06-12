# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-10 10:34:57
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-10 11:27:44


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 使用set，在set查找时间复杂度为O（1）
        wordset, nums = set(wordDict), len(s)
        # line[i]表示s[0:i]是否可以被差分
        line = [False for _ in range(nums+1)]
        line[0] = True
        for i in range(1, nums+1):
            for j in range(0, i):
                if line[j] and s[j:i] in wordset:
                    line[i] = True
                    break
        # 返回最后一个值
        return line[nums]
