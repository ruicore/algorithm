# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 19:43:49
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 20:06:11


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        frob, fnotrob, rob, notrob = nums[0], 0, 0, 0
        for item in nums[1:]:
            _max = max(frob, fnotrob)
            frob = item + fnotrob
            fnotrob = _max
            _max = max(rob, notrob)
            rob = item + notrob
            notrob = _max
        return max(fnotrob, rob)
