# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 15:49:20
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 15:53:13


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum > target:
                right -= 1
            elif _sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
