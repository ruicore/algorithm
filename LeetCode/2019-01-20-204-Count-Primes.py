# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 21:59:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 19:19:56


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        res, isprime = 0, [True] * (n + 1)
        isprime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if isprime[i]:
                for j in range(i * i, n + 1, i):
                    isprime[j] = False
        for i in range(2, n):
            if isprime[i]: res += 1

        return res
