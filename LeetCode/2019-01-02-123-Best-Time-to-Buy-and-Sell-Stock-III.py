# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-02 11:47:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-02 11:47:47


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nums = len(prices)
        if nums <= 1:
            return 0
        leftoright = [0 for _ in range(nums)]
        minprice = prices[0]
        # 先从左往右遍历，在只允许进行一次交易的前提下：求一遍最大利润
        # 即以当前价格为卖出价格
        for i in range(1, nums):
            # 更新买入价格的最小值
            minprice = min(minprice, prices[i])
            # 从第0天到第i天，获取最大利润
            # 若当天什么都不做，则获得前一天的利润；若当前进行一次交易，则利润为当天价格（卖出价格）减去前面最低点的价格
            # 于是当天的最大利润为上面两种情况的最大值
            leftoright[i] = max(leftoright[i-1], prices[i]-minprice)
        maxprice = prices[-1]
        rightoleft = [0 for _ in range(nums)]
        # 再从右往左遍历，在只允许进行一次交易的前提下：求一遍最大利润
        # 即以当天价格为买入价格
        for i in range(nums-2, -1, -1):
            # 更新卖出价格的最大值
            maxprice = max(prices[i], maxprice)
            # 同上，若第i天什么都不做，则获利为第i+天的利润，若进行一次交易，则利润为当天价格减去最高卖出价格
            # 于是当天的最大利润为上面两种情况的最大值
            rightoleft[i] = max(rightoleft[i+1], maxprice-prices[i])
        # 将对应位置一一求和，即为在最多允许两次交易的情况下的最大利润
        res = [x+y for x, y in zip(leftoright, rightoleft)]
        return max(res)
