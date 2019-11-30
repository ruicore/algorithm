# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-11-30 09:35:38
# @Last Modified by:   何睿
# @Last Modified time: 2019-11-30 10:10:40

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefix = set(num & mask for num in nums)
            tmp = res | (1 << i)
            for s in prefix:
                if tmp ^ s in prefix:
                    res = tmp
                    break

        return res
