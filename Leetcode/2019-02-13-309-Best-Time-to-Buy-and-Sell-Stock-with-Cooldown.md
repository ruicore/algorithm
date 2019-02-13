# LeetCode 309. Best Time to Buy and Sell Stock with Cooldown

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

* You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
* After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day).

Example:

```py
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

## 描述

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

* 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
* 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:

```py
输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
```

### 思路

* 这道题使用动态规划。
* 状态：colldown 表示当天休息能够获得的最大价值，hold 表示当天持有股票能够获得的最大价值，sold 表示当天持有股票能够获得的最大价值。
* 初始状态：colldown = 0, hold = －∞, sold = 0。
* 状态转移方程：colldown ：如果当前休息，那么当前的价值可以来自于前一天休息或者前一天卖出股票（前一天买进股票不会产生收益），所以 colldown = max(colldown, sold)；hold ：如果当天选择继续持有股票，则当天可以选择继续持有昨天的股票，或者昨天休息今天买进股票，所以hold = max(oldhold, colldown - prices\[i]); sold :当天卖出股票，则其价值只能来自于昨天买进今天卖出 sold = oldhold + prices\[i]。

```py
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-13-309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-309-best-time-to-buy-and-sell-stock-with-cooldown/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
