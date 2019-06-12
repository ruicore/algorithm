# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-09 16:31:05
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-09 16:43:17


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort(), nums2.sort()
        count1, count2 = len(nums1), len(nums2)
        i, j, res = 0, 0, []
        # 相同的部分一定在前面
        while i < count1 and j < count2:
            # 如果相等，添加到结果数组中
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i + 1, j + 1
            # 如果数组二的数大，将数组一的索引自增一次
            elif nums1[i] < nums2[j]:
                i += 1
            # 如果数组一的数大，将数组二的索引自增一次
            elif nums1[i] > nums2[j]:
                j += 1

        return res