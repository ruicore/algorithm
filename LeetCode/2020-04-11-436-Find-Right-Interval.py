# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-04-11 16:08:04
# @Last Modified by:   何睿
# @Last Modified time: 2020-04-11 16:34:06


from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        index_dict = {}
        for index, interval in enumerate(intervals):
            starts.append(interval[0])
            index_dict[interval[0]] = index

        starts.sort()

        return list(self._binary_find(starts, interval[1], index_dict) for interval in intervals)

    def _binary_find(self, nums, target, index_dict):

        if target in index_dict:
            return index_dict[target]

        left, right = 0, len(nums) - 1
        middle = left + (right - left) // 2
        while left <= right:
            if nums[middle] >= target and (middle == 0 or nums[middle - 1] < target):
                return index_dict[nums[middle]]
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] >= target and (middle == 0 or nums[middle - 1] >= target):
                right = middle - 1
            middle = left + (right - left) // 2

        return -1
