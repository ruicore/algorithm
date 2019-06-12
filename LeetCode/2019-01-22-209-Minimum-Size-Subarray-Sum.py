# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 11:37:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 11:37:16

import sys


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 初始化长度
        length = sys.maxsize
        _sum, left, right = 0, 0, 0
        while right < len(nums):
            _sum += nums[right]
            # 如果当前的和已经大于等于s
            if _sum >= s:
                # 我们将左指针向右移动，和小于s时跳出
                while _sum >= s and left <= right:
                    _sum -= nums[left]
                    left += 1
                # 更新长度
                length = min(right - left + 2, length)
            right += 1
        # 如果length始终没有发生改变返回0，否则返回length本身
        return length if length != sys.maxsize else 0
