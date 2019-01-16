# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 21:43:13
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 21:50:21


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base, res, count = 1, 0, len(s)
        for i in range(count):
            res += base * (ord(s[count - i - 1]) - 64)
            base *= 26
        return res
