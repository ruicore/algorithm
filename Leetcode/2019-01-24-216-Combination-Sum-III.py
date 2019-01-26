# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-24 06:37:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 20:38:26


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.recursion([i for i in range(1, 10)], k, n)

    def recursion(self, nums, k, _sum):
        if k <= 0: return
        if k == 1:
            if _sum in nums: return [[_sum]]
            else: return []
        res = []
        # 递归求解
        for i in range(len(nums)):
            # 从当前元素后面位置中寻找解
            for item in self.recursion(nums[i + 1:], k - 1, _sum - nums[i]):
                res.append(item + [nums[i]])
        return res
