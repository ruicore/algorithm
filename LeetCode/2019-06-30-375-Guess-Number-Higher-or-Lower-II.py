# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-30 10:54:08
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-30 14:56:28


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for right in range(1, n + 1):
            for left in range(right - 1, 0, -1):
                dp[left][right] = min(x + max(dp[left][x - 1], dp[x + 1][right]) for x in range(left, right))

        return dp[1][n]