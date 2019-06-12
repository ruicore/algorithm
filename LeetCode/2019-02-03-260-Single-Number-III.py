# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-03 09:02:18
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-03 09:02:18


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        diff = 0
        for num in nums:
            diff ^= num
        # 制造分离因子
        diff = diff & (~(diff - 1))
        for num in nums:
            if (num & diff) == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
