# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-14 20:40:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-14 21:57:33


class Solution:
    def minPatches(self, nums: [int], n: int) -> int:
        # tmp 表示所有数字的和，count表示需要添加数字，i 为索引
        # 定义[0,8) 8 为和的边界
        tmp, count, i = 0, 0, 0
        # 循环条件
        while tmp < n:
            # 如果 num[i] 在当前和的范围之内，那么把 num[i] 添加到
            # 当前的和范围内是最经济的做法
            if i < len(nums) and nums[i] <= tmp + 1:
                tmp += nums[i]
                i += 1
            # 否则，我们需要把当前和的边界的数字作为一个新的数字添加到和中
            else:
                tmp += tmp + 1
                count += 1
        return count