# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 21:52:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-18 17:25:13


import functools


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 对数组进行排序
        nums.sort(key=functools.cmp_to_key(self._sort))
        res = ''.join(map(str, nums))
        if res[0] == '0': return '0'
        return res

    def _sort(self, num1, num2):
        # 修改排序规则
        a = str(num1) + str(num2)
        b = str(num2) + str(num1)
        if a > b: return -1
        if a < b: return 1
        return 0