# LeetCode 123. Best Time to Buy and Sell Stock III

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

## 描述

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

### 思路

* 此题目是[121题](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)的进阶题，不同之处在于此处放宽了条件，可以允许进行两次交易.
* 总体思路是：我们以i为分界，求在prices\[0:i]交易一次的最大值和在prices\[i:n]交易一次的最大值，然后相加即可.
* 为此，我们遍历两趟prices:

1. 首先我们正向遍历prices，以prices\[i]为卖出价，保留minprice = min(prices\[0:i])为买进价格，求得交易一次在prices\[0:i]的最大值.
2. 然后我们反向遍历prices，以prices\[i]为买进价，保留maxprice = max(prices\[i:n])为卖出价格，求得交易一次在prices\[i:n]的最大值
3. 我们将对应位置的值相加，其最大值即为交易两次的总利润最大值.

```python
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
            # 若当天什么都不做，则获得前一天的利润；
            # 若当前进行一次交易，则利润为当天价格（卖出价格）减去前面最低点的价格
            # 于是当天的最大利润为上面两种情况的最大值
            leftoright[i] = max(leftoright[i-1], prices[i]-minprice)
        maxprice = prices[-1]
        rightoleft = [0 for _ in range(nums)]
        # 再从右往左遍历，在只允许进行一次交易的前提下：求一遍最大利润
        # 即以当天价格为买入价格
        for i in range(nums-2, -1, -1):
            # 更新卖出价格的最大值
            maxprice = max(prices[i], maxprice)
            # 同上，若第i天什么都不做，则获利为第i+天的利润，
            # 若进行一次交易，则利润为当天价格减去最高卖出价格
            # 于是当天的最大利润为上面两种情况的最大值
            rightoleft[i] = max(rightoleft[i+1], maxprice-prices[i])
        # 将对应位置一一求和，即为在最多允许两次交易的情况下的最大利润
        res = [x+y for x, y in zip(leftoright, rightoleft)]
        return max(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-02-123-Best-Time-to-Buy-and-Sell-Stock-III.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-123-best-time-to-buy-and-sell-stock-iii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
