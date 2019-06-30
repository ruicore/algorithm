# LeetCode 375. Guess Number Higher or Lower II

## Description

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay \$5.
Second round: You guess 7, I tell you that it's higher. You pay \$7.
Third round:  You guess 9, I tell you that it's lower. You pay \$9.

Game over. 8 is the number I picked.

You end up paying \$5 + \$7 + \$9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

## 描述

我们正在玩一个猜数游戏，游戏规则如下：

我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。

每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。

然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

示例:

n = 10, 我选择了8.

第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

游戏结束。8 就是我选的数字。

你最终要支付 5 + 7 + 9 = 21 块钱。
给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。

### 思路

* 题目中提到「当你猜了一个数之后，会告诉你，你猜的这个数和真实的数比，是大了还是小了」，但是此题目和 374 题目不同，并不会提供 guess 的 API，因为用不到。
* 这道题和被猜的数无关，只和范围 n 有关，因此函数参数里只有 n；下面对题意进行详细的解释。
* 假定 n 等于 10，需要猜的数为 g，那么 1. g 的范围是 \[1,10]（题目中明确从 1 开始）2.每次你猜的数也一定属于 \[1,10]。
* 假定 n 等于 10，需要猜的数为 1；那么猜中 1 有很多种方法；比如你一来就猜中了 1，不需要花钱；你猜 5，猜 3，猜2，猜 1，一共花了 10元；你猜 10，你猜 5，猜 3，猜 2，猜1，花了 20 元；在上面的 3 种猜法中，为了保证一定赢，你需要 20 元，记至少需要花的钱为 c1；
* 假定 n 等于 10，需要猜的数为 2；猜中 2 有很多可能，如一来就猜 2 ，不需要花钱；猜 5，猜 3，猜 2，花费了 8 元；猜 10，猜 5，猜 3，猜 2，花费了 18元；在上面的 3 种猜法中，为了保证一定赢，你需要 18 元，记至少需要花的钱为 c2；
* 同理可以获得 c3，c4 .... c10,题目要求的是 res = max(c1,c2...c10)，也就是说在范围 n 内，无论被猜的数是几，使用 res 数量的钱一定可以把这个数猜出来。
* 从上面的过程可以看到，不论被猜的数是几，我们都可以从 n 的中间值开始猜起，然后一路猜到被猜的数，这是一种猜的策略。
* 有没有更好的猜的策略呢？有的。题目要求的是：在使用这种策略下，至少需要的钱数。以下以 n 为 10为例，说明一下此时得最优策略。如下图：
![n 为 10 的路径](https://i2.wp.com/www.ruicore.cn/wp-content/uploads/2019/06/image-1.png?w=411&ssl=1)
* 当 n 为 10 时，无论被猜得数是什么，我们总是从 7 开始猜，下面给出每个一数得猜出路径；
* 7-->3-->1,10;
* 7-->3-->2,10;
* 7-->3,7;
* 7-->3-->5-->4,15;
* 7-->3-->5,10;
* 7-->3-->5-->6,15;
* 7,0;
* 7-->9-->8,16;
* 7-->9,7;
* 7-->9-->10,16;
* 最后一个数表示需要花费的钱数，可以看出，当 n 为 10 时，最少需要 16 才能保证一定赢；
* 根据题意，记被猜的数的集合为 t = \[1,n]
* 使用动态规划，dp\[left]\[right] 表示当被猜的集合 t 为 \[left,right] 时最少需要的钱数，dp\[3]\[5] = 4 表示要猜中\[3,5]中的所有数，最少需要 4 元。
* 那么 dp\[1]\[n] 表示要猜中 \[1,n] 中的所有数最少需要的钱数，也就是题意所求。
* 假定我们猜的范围为  n  到 n ，那么此时不需要花费任何的钱，因为候选集合只有 1 个数，直接猜就行；
* 假定我们猜的范围为 n-1 到 n ，如 n = 10, 猜的为范围设置为\[9,10],次数我们一定从小的数 9 开始猜，此时最少需要 9 元；
* 假定我们猜的范围为 n-2 到 n ，如 n = 10, 猜的为范围设置为\[8，9,10],次数我们一定 9 开始猜，此时最少需要 9 元；
* ...
* 为了猜中 t = \[left,right] 中的所有数；我们可以尝试以 t 中的每一个数为第一个被猜的数，找到此时猜完所有数的最坏情况；每一个 x 对应一个最坏值，所有最坏值得最小值就是 dp\[left]\[right] 的值。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-30 10:54:08
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-30 14:56:28


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for right in range(1, n + 1):
            for left in range(right - 1, 0, -1):
                # 第一个数猜 x，为了猜完 [left,right] 所有的数
                # 我们选择 max(dp[left][x - 1], dp[x + 1][right])，从而保证大的一边可以被猜完；
                # 大的一边可以被猜完，小的一边自然也可以被猜完；
                dp[left][right] = min(x + max(dp[left][x - 1], dp[x + 1][right]) for x in range(left, right))

        return dp[1][n]
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-06-30-375-Guess-Number-Higher-or-Lower-II.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-375-guess-number-higher-or-lower-ii/) ，作者信息和本声明.
