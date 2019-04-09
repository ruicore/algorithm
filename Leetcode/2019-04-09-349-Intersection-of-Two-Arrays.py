# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-09 16:11:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-09 16:15:56


class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        # python 内置集合运算
        return list(set(nums1) & set(nums2))