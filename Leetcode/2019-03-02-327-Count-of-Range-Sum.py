# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-02 15:54:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-02 20:40:27

import bisect


class Solution:
    def countRangeSum(self, nums: [int], lower: int, upper: int) -> int:
        presum, _sum, count = [0], 0, 0
        for num in nums:
            _sum += num
            right = bisect.bisect_right(presum, _sum - lower)
            left = bisect.bisect_left(presum, _sum - upper)
            count += right - left
            bisect.insort(presum, _sum)
        return count