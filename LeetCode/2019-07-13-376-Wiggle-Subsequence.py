# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-13 07:52:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-13 08:15:12


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0

        dp = [[0, 1] for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                diff = nums[i] - nums[j]
                if diff * dp[j][0] <= 0 and diff != 0 and (dp[j][1] + 1) > dp[i][1]:
                    dp[i][0] = diff // abs(diff)
                    dp[i][1] = dp[j][1] + 1
                    break

        return dp[-1][1]

