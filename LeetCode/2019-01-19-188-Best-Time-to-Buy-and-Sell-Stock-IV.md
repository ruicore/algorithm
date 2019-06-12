# LeetCode 188. Best Time to Buy and Sell Stock IV

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

## 描述

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

### 思路

![LeetCode 188-Best Time to Buy and Sell Stock IV-1](https://wp.me/aaizn9-14e)
* 这道题使用动态规划.
* 我们用一个二维矩阵trans，矩阵的列表示交易的价格，矩阵的行表示交易的次数，矩阵的值表示当前能够获得的最大利润.如上图所示，第一行表示进行0次交易，获得的利润为0；第一列表示在第一天（索引为0）进行交易，只有一天无法进行完整的交易，所以活力为0.
* 以允许3次交易，第3天为例，trans\[3]\[3],我们有如下的选择：
* 1，在这一天我们什么什么都不做，于是我们获得昨天tans\[3]\[2]的利润 
* 2.我们以今天的价格为卖出价，以第0天为买进价，则可以获得利润pri1 = pries\[3]-prices\[0](占用一次交易次数)+trans\[2][0]\(截止第0天，交易2次获得最大利润)
* 3.我们以今天的价格为卖出价，以第1天为买进价，则可以获得利润pri2 = pries\[3]-prices\[1](占用一次交易次数)+trans\[2][1]\(截止第1天，交易2次获得最大利润)
* 4.我们以今天的价格为卖出价，以第2天为买进价，则可以获得利润pri3 = pries\[3]-prices\[2](占用一次交易次数)+trans\[2][2]\(截止第2天，交易2次获得最大利润)
* 于是tans\[3]\[3] = max(tans\[3]\[2],pri1,pri2,pri3)
* 同理tans\[3]\[4]的最大值：
* 1，在这一天我们什么什么都不做，于是我们获得昨天tans\[3]\[3]的利润 
* 2.我们以今天的价格为卖出价，以第0天为买进价，则可以获得利润pri1 = pries\[4]-prices\[0](占用一次交易次数)+trans\[2][0]\(截止第0天，交易2次获得最大利润)
* 3.我们以今天的价格为卖出价，以第1天为买进价，则可以获得利润pri2 = pries\[4]-prices\[1](占用一次交易次数)+trans\[2][1]\(截止第1天，交易2次获得最大利润)
* 4.我们以今天的价格为卖出价，以第2天为买进价，则可以获得利润pri3 = pries\[4]-prices\[2](占用一次交易次数)+trans\[2][2]\(截止第2天，交易2次获得最大利润)
* 5.我们以今天的价格为卖出价，以第2天为买进价，则可以获得利润pri4 = pries\[4]-prices\[3](占用一次交易次数)+trans\[2][3]\(截止第3天，交易2次获得最大利润)
* 这样我们就可以求得第k次交易的最大值.
* 我们将-prices\[0](占用一次交易次数)+trans\[2][0]记为P1，-prices\[1](占用一次交易次数)+trans\[2][1]记为P2，-prices\[2](占用一次交易次数)+trans\[2][2]记为P3
* 时间复杂度O(n^3)，我们发现观察上面的过程可以发现，在判断tans\[3]\[3]的值的时候，其中P1，P2，P3，已经被计算过，而我们要求的值
* tans[3][4]= max(tans\[3]\[3],pries\[4]+P1,pries\[4]+P2,pries\[4]+P3,pries\[4]-prices\[3](占用一次交易次数)+trans\[2][3]).
* tans[3][4]= max(tans\[3]\[3],pries\[4]+max(P1,P2,P3,-prices\[3](占用一次交易次数)+trans\[2][3])).
* 于是我们可以首先计算max(P1,P2,P3,-prices\[3](占用一次交易次数)+trans\[2][3])=maxdiff，这样就可以减少一次循环.
* 空间复杂度O(n^2),通过上面的描述发现，每次在被允许k次交易的时候，我们只需要知道第k-1次交易的信息，k-2，k-3已经不需要知道了，所以我们只用生成一个两行的矩阵即可.
* 还需要注意的是，n天最多可以进行n/2取整次交易，当给定的交易次数k>=n/2时,题目相当于转换成了可以被允许进行无限次交易.

```python
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-19-188-Best-Time-to-Buy-and-Sell-Stock-IV.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-188-best-time-to-buy-and-sell-stock-iv/)，欢迎转载，转载需保留文章来源，作者信息和本声明.