# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 21:06:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 18:21:42


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        diff = 0
        while m - n:
            diff += 1
            m >>= 1
            n >>= 1
        return m << diff
