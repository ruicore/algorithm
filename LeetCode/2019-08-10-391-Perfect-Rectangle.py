# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-10 12:09:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-10 12:09:46

from typing import List
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        point_table = defaultdict(int)

        area = 0
        for line in rectangles:
            leftx, lefty, rightx, righty = line
            point_table[(leftx, lefty)] += 1
            point_table[(rightx, righty)] += 1
            point_table[(leftx, righty)] += 1
            point_table[(rightx, lefty)] += 1
            area += (rightx - leftx) * (righty - lefty)

        vertex = [x for x in point_table if point_table[x] & 1]
        if len(vertex) != 4:
            return False

        min_, max_ = min(vertex), max(vertex)
        (minx, miny), (maxx, maxy) = min_, max_

        return (maxx - minx) * (maxy - miny) == area
