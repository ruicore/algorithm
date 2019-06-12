# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-02 10:17:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-02 10:17:16


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nums, i, profit = len(prices), 0, 0
        # 寻找波峰和波谷，i需要遍历到最后一个位置的前一个值
        while i < nums-1:
            # 寻找波谷
            while i < nums-1 and prices[i] >= prices[i+1]:
                i += 1
            # 在此时买进
            valley = i
            # 寻找波峰
            while i < nums-1 and prices[i] <= prices[i+1]:
                i += 1
            # 在此时卖出
            peak = i
            # 获取利润
            profit += prices[peak]-prices[valley]
        return profit


class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            # 只要在涨就可以获取利润，有这种方法，可以获得最大利润，但是没有记录在什么时候买进，什么时候卖出
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit


if __name__ == "__main__":
    so = Solution()
    res = so.maxProfit([7, 1, 5, 3, 6, 4])
    print(res)
