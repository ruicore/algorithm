# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 18:23:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 18:23:33


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 数组的个数
        length = len(nums)
        # 如果数组中没有元素或者只有一个元素，直接返回数组长度
        if length <= 1: return length
        # 动态规划，数组没个位置初始化为1
        # 表示连续递增的序列长度最下为1
        count = [1] * length
        res = 0
        for i in range(1, length):
            # 初始化为1
            _max = 1
            # 从当前位置遍历到i
            for j in range(0, i):
                # 第i个数的最大值为0到i-1中所有小于当前元素能够称的连续序列加一的最大值
                if nums[j] < nums[i]: _max = max(count[j] + 1, _max)
            # 更新当前位置的最大值
            count[i] = _max
            # 记录所有值的最大值
            res = max(res, _max)
        return res