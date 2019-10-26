# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-26 09:30:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-26 10:18:19

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums & 1 or max(nums) > (sum_nums >> 1):
            return

        half_sum = sum_nums >> 1
        nums.sort(reverse=True)
        dp = [[False] * (half_sum + 1) for _ in range(2)]
        dp[0][0] = True
        dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            idx = i % 2
            for j in range(nums[i]):
                dp[idx][j] = dp[idx - 1][j]
            for j in range(nums[i], half_sum + 1):
                dp[idx][j] = dp[idx - 1][j] if dp[idx - 1][j] else dp[idx - 1][j - nums[i]]
            if dp[idx][-1]:
                return True

        return dp[-1][-1]
