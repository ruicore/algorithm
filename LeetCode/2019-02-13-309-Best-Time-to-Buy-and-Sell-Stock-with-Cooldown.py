# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-13 14:21:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-13 17:36:21

import sys


class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        # 少于两天无法进行交易
        if len(prices) < 2: return 0
        colldown, hold, sold = 0, -sys.maxsize, 0
        for day in range(len(prices)):
            oldhold = hold
            # 当天持有：当天可以什么都不做，持有昨天持有的股票
            # 或者当天买进股票
            # 所以：当天价值可以来自前一天持有的价值，或者前一天休息今天买入的价值
            hold = max(oldhold, colldown - prices[day])
            # 当天休息：当天的价值可以来自于前一天休息的价值
            # 或者前一天卖出的价值
            colldown = max(colldown, sold)
            # 当天卖出：当前价值来自前一天持有加上今天的价值
            sold = oldhold + prices[day]
        return max(colldown, sold)