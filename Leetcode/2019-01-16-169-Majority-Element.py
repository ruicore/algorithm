# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 20:27:19
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 20:47:38


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 中间值一定会是超过一半的值
        return sorted(nums)[len(nums) // 2]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 超过了一半的值会使得count大于0
        majority, count = nums[0], 1
        for item in nums:
            if item == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = item
                count = 1
        return majority
