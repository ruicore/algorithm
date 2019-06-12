# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-10 21:56:48
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-10 22:02:19


class NumArray:
    def __init__(self, nums: 'List[int]'):
        # 对给定的数组的前面的数求和
        if not nums:
            self.sum = []
        else:
            self.sum = [nums[0]] * len(nums)
            for i in range(1, len(nums)):
                self.sum[i] = self.sum[i - 1] + nums[i]

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        # 做差返回对应序列的值
        return self.sum[j] - self.sum[i - 1] if i > 0 else self.sum[j]
