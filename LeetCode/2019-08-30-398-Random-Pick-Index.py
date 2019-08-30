# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-30 19:55:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-30 20:17:06

import heapq
import random

from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.arrays = nums

    def pick(self, target: int) -> int:
        hep = []
        for i, v in enumerate(self.arrays):
            if v == target:
                heapq.heappush(hep, (random.random(), i))
        _, index = heapq.heappop(hep)
        return index

    def pick2(self, target: int) -> int:

        n, res = 0, 0
        for x in filter(lambda x: x[1] == target, enumerate(self.arrays)):
            n += 1
            if random.randint(1, n) == n:
                res = x[0]

        return res
