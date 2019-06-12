# LeetCode 122. Best Time to Buy and Sell Stock II

## 思路

* 此题目是第[121题](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)的进阶题，同121题一样，不同的是122题可以进行多次交易.
* 我们这样考虑有在prices中，从i到k有i···j···k，从i到j一直递增，j到k先递减后递增，且有prices\[i]<\prices\[j]<\prices\[k],如果我们为了增大利润，在i买进和k卖出，则一定没有从i买进，j卖出，再从j到k中的递减最低点买入，k卖出高.
* 即我们将每一个连续递增的序列作为一个交易，从最低点买入，从最高点卖出，所以我们只需要不断的找连续的递增区间即可.

```python

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
```

* 或者用另一种表现形式，只要当前在递增，说明就可以获取利润，不过用这种方法不能记录买入和卖出的时间.

```python

class Solution:
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-02-122-Best-Time-to-Buy-and-Sell-Stock-II.py).
©本文是原创文章，欢迎转载，转载需保留[文章来源](https://www.ruicore.cn/)，作者信息和本声明.
©本文首发于[何睿的博客](https://www.ruicore.cn/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
