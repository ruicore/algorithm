# LeetCode 121. Best Time to Buy and Sell Stock

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

```python
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

Example 2:

```python
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## 描述

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果您最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意您不能在买入股票前卖出股票。

示例 1:

```python
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

示例 2:

```python
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

### 思路

#### 思路一

* 此题的本质就是在给定的未排序的数组中，找到两个数nums\[i]和nums\[j],使得i<\j并且使得nums\[j]-nums\[i]最大.
* 我么假设一共有n天，并且我们假设必须在第i天之前（包括第i天）买入，必须在第i+1到第n天之间卖出。那么关于买入价格，我们一定会选择 k= Min(nums\[0:i]),因为如果有任意一天的价格低于k，我们完全应该选择买入价格更低的那一天，因为这样会使得利润更大。同理，关于卖出价格，我们一定会选择 S = Max(nums\[i+1:n]),因为如果由价格更高的一天，我们完全应该在价格更高的一天卖出，这样才能保证利润最高.
* 于是，我们找到了以i为分界的最佳买入时机和最佳卖出时机，i有n个不同取值，我们取其中利润最高的那次一次即可.
* 首先我们正向遍历数组，确定在第i天之前买入，我们会选择买入的价格（即找nums\[0:i]的最小值）.
* 然后我们逆向遍历数组，确定在第i+1到第n天之间卖出我们会选择的最高价格（即找nums\[i+1:n]之间的最大值）.(**这里可以稍微优化以下，减少空间的占用).
* 最后一次我们做差，返回最大值即可.

```python
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
```

#### 思路二

* 我们假设我们都在第i-1天买入，第i天卖出，我们求得此利润.
* 要找最大利润，即是找一个连续的几天，使得获利最大.

```python

class Solution:
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-02-121-Best-Time-to-Buy-and-Sell-Stock.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-121-best-time-to-buy-and-sell-stock/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
