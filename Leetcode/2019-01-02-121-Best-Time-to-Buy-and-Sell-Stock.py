# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-02 09:19:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-02 09:38:19


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minprices, minp, profit = [prices[0]], prices[0], 0
        # 假设在第0-i天之间买进，则一定会在最低点买进
        for i in range(1, len(prices)):
            minp = prices[i] if prices[i] < minp else minp
            minprices.append(minp)
        # 如果在当天卖出，则可以获得多少利润，取最大值
        for i in range(len(prices)):
            temp = prices[i]-minprices[i]
            profit = temp if profit < temp else profit
        return profit


class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # profits用于记录第i-1天买入，第i天卖出可以获得的利润
        profits = []
        for i in range(1, len(prices)):
            profits.append(prices[i]-prices[i-1])
        profit, temp = 0, 0
        # 此题目转化为求连续的天数利润之和，使其和最大
        for i in range(0, len(profits)):
            temp += profits[i]
            profit = temp if temp > profit else profit
            temp = 0 if temp < 0 else temp
        return profit
