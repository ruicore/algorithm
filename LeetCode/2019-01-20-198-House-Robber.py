# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 12:32:39
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 14:07:25


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob, notrob = 0, 0
        for item in nums:
            temp = max(rob, notrob)
            rob = item + notrob
            notrob = temp
        return max(rob, notrob)
