# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 09:47:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-17 09:51:51


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n // 5
            n //= 5
        return res
