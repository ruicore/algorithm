# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 10:11:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 12:37:11

from functools import reduce


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = nums[0], 0
        start, end = 0, 0
        for i in range(len(nums)):
            if nums[i] < 0:
                count += 1
            # 当遇到0或者到达末尾时就进行切片
            if nums[i] == 0 or i == len(nums) - 1:
                # 不包括元素num[i]本身
                end = i - 1 if nums[i] == 0 else i
                res = max(res, nums[i], self._product(start, end, count, nums))
                start, count = i + 1, 0
        return res

    def _product(self, start, end, count, nums):
        # 计算连续数字乘机最大值
        if start > end:
            return 0
        # 如果负数有偶数个，则所有值的连续相乘的积就是最大值
        if not count % 2:
            return reduce(lambda x, y: x * y, nums[start:end + 1])
        # 如果有奇数个负数，则我们应该丢掉第一个负数左边的片段或者最后一个负数右边的片段
        first, last = 0, 0
        # 寻找第一个负数的索引
        for i in range(start, end + 1):
            if nums[i] < 0:
                first = i
                break
        # 寻找最后一个负数的索引
        for i in range(end, start - 1, -1):
            if nums[i] < 0:
                last = i
                break
        # 如果第一个负数和最后一个负数不重合
        if first != last:
            # 计算从nums[first + 1:last]的乘机
            middle = reduce(lambda x, y: x * y, nums[first + 1:last])
            # 计算第一个负数左边的乘积（包括第一个负数本身）
            left = reduce(lambda x, y: x * y, nums[start:first + 1])
            # 计算最后一个负数右边的乘积（包括最后一个负数本身）
            right = reduce(lambda x, y: x * y, nums[last:end + 1])
        # 如果第一个负数和最后一个负数重合，即只有一个负数
        else:
            # 令中间的值为1
            middle = 1
            left = reduce(lambda x, y: x * y,nums[start:first]) if start != first else nums[start]
            right = reduce(lambda x, y: x * y,nums[last + 1:end + 1]) if last != end else nums[end]
        # 分别计算中间乘积与左边的乘积，中间乘积与右边的乘积
        res1, res2 = middle * left, middle * right
        # 返回最大值
        return res1 if res1 > res2 else res2
