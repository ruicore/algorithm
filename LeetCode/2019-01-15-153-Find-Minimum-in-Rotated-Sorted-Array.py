# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 13:52:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 16:00:40


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果为空，则直接返回
        if not nums:
            return 0
        # left为最左边的索引，right为最右边的索引
        left, right = 0, len(nums) - 1
        # 首先获取中间值
        middle = left + ((right - left) >> 1)
        # 如果是连续递增的请情况，返回数组的第一个值
        if nums[0] <= nums[middle] <= nums[-1]:
            return nums[0]
        # 如果是连续递减的情况，返回最后一个值
        if nums[-1] <= nums[middle] <= nums[0]:
            return nums[-1]
        while left < right:
            middle = left + ((right - left) >> 1)
            # 结束条件，交换的位置满足下面的条件
            if nums[middle] < nums[middle + 1] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[0]:
                left = middle + 1
            # 注意这里不是middle-1，因为有可能middle就是要求的枢纽位置
            if nums[middle] < nums[-1]:
                right = middle
        return nums[left]
