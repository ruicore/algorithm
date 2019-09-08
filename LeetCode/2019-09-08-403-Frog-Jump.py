# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-08 08:01:56
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-08 09:07:52

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stages = {x: set() for x in stones}
        stages[0] = {0}
        end = stones[-1]

        for key in stones:
            steps = stages[key]
            if not steps:
                return False
            if any(map(lambda step: self.__jump(stages, step, key, end), steps)):
                return True

        return False

    def __jump(self, stages, step, start, end):

        steps = (step - 1, step, step + 1)
        for s in filter(lambda x: x > 0 and start + x in stages, steps):
            stages[start + s].add(s)
            if start + s == end:
                return True

        return False
