# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-14 22:29:33
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-14 22:36:14


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = nums[0]
        tempsum_ = 0
        for item in nums:
            tempsum_ += item
            if tempsum_ > sum_:
                sum_ = tempsum_
            if tempsum_ < 0:
                tempsum_ = 0
        return sum_
