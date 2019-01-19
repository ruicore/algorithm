# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-19 18:24:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-19 19:29:49

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:return 0
        res =0
        for _ in range(32):
            if n & 1:res+=1
            n>>=1
        return res