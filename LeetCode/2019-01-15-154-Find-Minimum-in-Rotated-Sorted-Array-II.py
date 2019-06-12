# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 16:01:45
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 16:35:18


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            # 相同的值直接跳过
            while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                left += 1
            while right > 0 and nums[right] == nums[right - 1]:
                right -= 1
            middle = left + ((right - left) >> 1)
            # 判断当前的片段是否连续
            # 如果是连续递增，返回最左边的值
            if nums[left] <= nums[middle] <= nums[right]:
                return nums[left]
            # 如果是连续递减，返回最右边的值
            if nums[right] <= nums[middle] <= nums[left]:
                return nums[right]
            # 找到枢纽值的条件
            if nums[middle] < nums[middle + 1] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[0]:
                left = middle + 1
            if nums[middle] < nums[-1]:
                right = middle
        return nums[left]
