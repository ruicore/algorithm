# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-11 08:21:24
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-11 09:52:45

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        if not nums:
            return 1
        for i in range(length):
            while 0 < nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                n = nums[i] - 1
                nums[i], nums[n] = nums[n], nums[i]

        for i, n in enumerate(nums, 1):
            if i != n:
                return i
        else:
            return n + 1

        return
