# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-20 07:58:21
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-20 08:33:22

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            # dp[i] = sum(map(lambda j: dp[i - j], filter(lambda j: i - j >= 0, nums)))
            dp[i] = sum(dp[i - j] for j in nums if i - j >= 0)

        return dp[-1]
