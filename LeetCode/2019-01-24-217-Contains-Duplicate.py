# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-24 19:13:41
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 20:56:11


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 如果没有重复，那么这两种数据结构的元素个数应该相等
        return len(set(nums)) - len(nums) != 0
