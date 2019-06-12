# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-12 10:44:38
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-12 11:06:24


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 如果只有一个值，直接返回
        if len(nums) == 1:
            return [nums]
        # 声明最终需要返回的答案
        res = []
        # 遍历数组中的元素
        for i, num in enumerate(nums):
            # 去掉已经遍历的元素
            subnum = nums[:i]+nums[i+1:]
            # 把刚刚去掉的元素和剩下的元素所有可能的结果相加
            for subres in self.permute(subnum):
                res.append([num]+subres)
        return res
