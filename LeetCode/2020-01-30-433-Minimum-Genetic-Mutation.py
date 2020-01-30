# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-01-30 11:43:15
# @Last Modified by:   何睿
# @Last Modified time: 2020-01-30 12:11:17

import collections
from typing import List


class Solution:
    def _valid_next(self, current: str, next_: str):
        return sum(1 for c, n in zip(current, next_) if c != n) == 1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = collections.deque()
        queue.append([start, '', 0])

        while queue:
            current, previous, steps = queue.popleft()
            if current == end:
                return steps
            for item in bank:
                if item != previous and self._valid_next(current, item):
                    queue.append([item, current, steps + 1])

        return -1
