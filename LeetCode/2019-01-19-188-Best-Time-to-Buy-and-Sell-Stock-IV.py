# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-19 12:53:32
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-19 14:31:38


class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #交易次数为0或者交易天数小于2时无法进行交易，返回0
        if len(prices) < 2 or k == 0:
            return 0
        # n天最多可以交易n//2次，当允许的交易次数大于这个天数的时候，这道题就转换
        # 成了不限制交易次数
        if k >= (len(prices) // 2):
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        # 生命矩阵，动态规划
        # 为了避免出现内存超出限制，根据本题的特点，矩阵只需要两行就够了
        row, col = 2, len(prices)
        trans = [[0 for _ in range(col)] for _ in range(row)]
        # 进行k次交易
        for i in range(k):
            maxdiff = trans[i % 2][0] - prices[0]
            for j in range(1, col):
                maxdiff = max(maxdiff, trans[i % 2][j - 1] - prices[j - 1])
                trans[(i + 1) % 2][j] = max(trans[(i + 1) % 2][j - 1],maxdiff + prices[j])
        return max(trans[0][col - 1], trans[1][col - 1])
