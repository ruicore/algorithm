# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-19 18:17:49
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-19 19:30:51


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if not n: return 0
        res = 0
        for _ in range(32):
            res <<= 1
            if n & 1: res += 1
            n >>= 1
        return res