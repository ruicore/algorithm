# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-25 19:04:39
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 22:37:41


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 如果没有数字或者只有一个数字，则不可能有满足题意的解
        if nums == [] or len(nums) == 1: return False
        # 如果没有重复元素，也不可能有满足题意的解
        if len(nums) == len(set(nums)): return False
        # 我们用一个dict存储重复的值
        dic = {}
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = []
            dic[num].append(index)
            # 如果相同的值索引差小于等于k，返回True
            if len(dic[num]) > 1 and dic[num][-1] - dic[num][-2] <= k:
                return True
        # 如果遍历整个数组都没有找到满足条件的值，返回False
        return False