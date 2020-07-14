# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-12 21:52:42
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-12 23:29:11

from typing import List


def get_change(costs: List, money: int) -> int:

    # 为了简短，对 costs 和 money 各自乘以 2 并转换为 int 的操作没有写出
    dp = [[0] * (money + 1) for _ in range(len(costs))]
    for i in range(1, money // costs[0] + 1):
        dp[0][i * costs[0]] = 1

    for i in range(1, len(costs)):
        for j in range(1, money + 1):
            dp[i][j] = sum(dp[i - 1][j - x * costs[i]] for x in range(j // costs[i] + 1))
            # 如果刚好 j 能够整除 costs[i]，说明可以构成一种买法
            if j % costs[i] == 0: dp[i][j] += 1

    return sum(dp[-1])
