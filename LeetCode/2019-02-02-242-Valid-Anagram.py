# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 16:55:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 18:05:09


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        # 题目明确只会给定26个小写字母
        scount, tcount = [0 for _ in range(26)], [0 for _ in range(26)]
        for x, y in zip(s, t):
            # 统计s中字母出现的次数
            scount[ord(x) - ord('a')] += 1
            # 统计t中字母出现的次数
            tcount[ord(y) - ord('a')] += 1
        # 返回s和t中字母出现的次数是否一一对应相等
        return scount == tcount
