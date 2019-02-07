# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-07 13:55:55
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-07 14:07:46


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # 获取第一个0的索引
        first = 0
        while first < len(nums):
            if nums[first] == 0:
                break
            first += 1
        # 如果0已经在嘴后一个位置或者没有0
        if first >= len(nums) - 1:
            return
        # 把第一个0和0后面的非零数替换
        # 并将first自增一次，指向下一个0
        for i in range(len(nums)):
            if nums[i] and i > first:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1