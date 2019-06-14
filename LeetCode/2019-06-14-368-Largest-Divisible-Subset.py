# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-14 11:17:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-14 13:09:36

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []

        max_count, end = 1, 0
        count, path = [1] * len(nums), [0] * len(nums)

        nums.sort()
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and count[j] + 1 > count[i]:
                    count[i] = count[j] + 1
                    path[i] = j
            if count[i] >= max_count:
                max_count = count[i]
                end = i

        res = []
        for _ in range(max_count):
            res.append(nums[end])
            end = path[end]

        return res