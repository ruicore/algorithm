# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-03 14:41:25
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-03 14:56:07

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt_dict = Counter(s)
        a = sum(cnt_dict.values())
        b = sum(1 for x in cnt_dict.values() if x & 1)

        return a if b == 0 else a - b + 1
