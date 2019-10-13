# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-13 20:27:38
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-13 20:55:02

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        bucket = [float("-inf"), float("-inf"), float("-inf")]
        for num in nums:
            for i in range(3):
                if num > bucket[i]:
                    self._update(i, num, bucket)
                    break
                if num == bucket[i]:
                    break

        return bucket[-1] if bucket[-1] != float("-inf") else bucket[0]

    def _update(self, i, num, bucket):
        if i == 0:
            bucket[1], bucket[2] = bucket[0], bucket[1]
            bucket[0] = num
        elif i == 1:
            bucket[2] = bucket[1]
            bucket[1] = num
        elif i == 2:
            bucket[2] = num
