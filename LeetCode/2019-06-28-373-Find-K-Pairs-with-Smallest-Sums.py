# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-28 10:56:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-28 11:40:14

from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # 处理异常情况
        if not nums1 or not nums2:return []

        heap = list()
        len1, len2 = len(nums1), len(nums2)

        # k 对最小数对的和，所有的数一定都落在 nums1 和 nums2 的前 k 个数中
        num = k if len2 > k else len2

        # 将第一个数组的第一个数与第二个数组的前 k 个数组合
        for i in range(num):
            heappush(heap, (nums1[0]+nums2[i], 0, i))
        count = 0
        res = list()

        # 取 k 个有效数对

        while heap and count < k:
            
            # 最小数对是 (nums1[i], nums2[j])
            _sum, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            count += 1
            if i + 1 < len1:
                # 取到了最小数对 (nums1[i], nums2[j])
                # 我们将比最小数对大的最小数对 (nums1[i+1], nums2[j]) 压入堆中
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        del heap

        return res
