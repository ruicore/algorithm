# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 10:40:41
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 11:21:29


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        middle, left, right = 0, 0, count - 1
        while left <= right:
            # 取中间值
            middle = left + ((right - left) >> 1)
            # 如果当前是递增的序列，说明较大值在右边（不包括当前节点）
            if middle < count - 1 and nums[middle] < nums[middle + 1]:
                left = middle + 1
            # 如果当前是递减的徐磊，说明较大值在左边（包括当前节点）
            if middle < count - 1 and nums[middle] > nums[middle + 1]:
                right = middle
            # 结束条件：到达了边界或者当前值比左右两个值大
            if (middle==0 or nums[middle] > nums[middle - 1]) and (middle == count-1 or nums[middle] > nums[middle + 1]):
                return middle
        return middle
