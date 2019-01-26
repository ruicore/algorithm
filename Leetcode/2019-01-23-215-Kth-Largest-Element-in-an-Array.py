# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-23 22:57:06
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 20:23:38


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        # 
        pivot = self._quicksort(nums, left, right)
        while pivot != k - 1:
            # 如果当前确定的位置在k的左边，说明要求的元素应该在右边
            if pivot < k - 1:
                left = pivot + 1
            # 如果当前确定的位置在k的右边，说明要求的元素应该在左边
            elif pivot > k - 1:
                right = pivot - 1
            pivot = self._quicksort(nums, left, right)
        return nums[pivot]

    # 快速排序
    def _quicksort(self, nums, left, right):
        pivot, j = right, left
        for i in range(left, right):
            if nums[i] > nums[pivot]:
                if j != i:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[pivot] = nums[pivot], nums[j]
        # 返回当前已经确定元素的索引
        return j
