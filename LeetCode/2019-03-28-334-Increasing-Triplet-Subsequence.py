# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-28 10:02:55
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-28 11:08:49


class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        # 声明三个索引变量，用于记录满足条件的之
        i, j, k = 0, 1, 1
        # 元素的个数
        count = len(nums)
        # 找到数组中最前面递增的两个数
        while i < count and j < count and nums[i] >= nums[j]:
            i += 1
            j += 1
        # k 更新为 j 后面的那一个数
        k = j + 1
        while k < count:
            # 如果 nums[k] 比 nums[j] 大，说明已经有三个数满足条件
            if nums[k] > nums[j]: return True
            # 如果 nums[k] 在 nums[i] 和 nums[j] 中间，我们丢掉 nums[j]
            # 更新现有的 j 为 k，因为如果接下来有个数比 nums[j]大，那么一定比 nums[k] 大
            if nums[i] < nums[k] <= nums[j]: j = k
            # 如果 nums[k] 比 nums[i] 还小，我们更新 i 
            if nums[k] <= nums[i]: i = k
            k += 1
        # 前面没有满足条件的数，返回 False
        return False