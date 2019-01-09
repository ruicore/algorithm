# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-09 22:05:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-09 22:05:35


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one
