# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-04 11:17:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-05 16:13:51

from typing import List
from bisect import bisect_right


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        prefix_sum = self.sum_cumulative(nums)
        left, right, count = max(nums), prefix_sum[-1], len(nums)

        while left < right:
            middle = left + ((right - left) >> 1)
            if self.is_greater(prefix_sum, middle, m, count):
                left = middle + 1
            else:
                right = middle

        return right

    def sum_cumulative(self, nums):
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        return prefix_sum

    def is_greater(self, prefix_sum, max_num, m, count):

        pivot, start, group = max_num, 0, 0
        while start < count:
            start = bisect_right(prefix_sum, pivot, start)
            pivot = prefix_sum[start - 1] + max_num
            group += 1
            if group > m:
                return True

        return False
