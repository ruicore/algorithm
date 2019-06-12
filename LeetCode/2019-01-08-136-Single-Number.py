# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-08 09:48:14
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-08 10:18:15

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =0
        for num in nums:
            res ^=num
        return res

