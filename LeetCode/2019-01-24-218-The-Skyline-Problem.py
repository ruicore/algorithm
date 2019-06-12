# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-24 21:17:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-25 23:30:15

import heapq
import functools
from queue import PriorityQueue as PQueue

class Rect:
    def __init__(self, x, height, isStart):
        self.x = x
        self.height = height
        self.isStart = isStart


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res, rects = [], []

        for item in buildings:
            rects.append(Rect(item[0], item[2], True))
            rects.append(Rect(item[1], item[2], False))

        heap =[]
        rects.sort(key=functools.cmp_to_key(self._sort))
        for item in rects:
            heapq.heappush(heap,item)
        # pq = PQueue()
        for item in rects:
            if item.isStart:
                if item.height > heap.max():
                    res.append((item.x, item.height))
                heap.add(item.height)
            else:
                heap.remove(item)
                if item.height > heap.max():
                    res.append((item.x, item.height))
        return res

    def _sort(self, rect1, rect2):
        if rect1.x == rect2.x:
            if rect1.isStart and rect2.isStart:
                if rect1.height < rect2.height:
                    return -1
                if rect1.height > rect2.height:
                    return 1
                return 0
            if not rect1.isStart and not rect2.isStart:
                if rect1.height < rect2.height:
                    return 1
                if rect1.height > rect2.height:
                    return -1
                return 0
            if not rect1.isStart and rect2.isStart:
                if rect1.height < rect2.height:
                    return -1
                if rect1.height > rect2.height:
                    return -1
                return 0
        else:
            if rect1.height < rect2.height:
                return -1
            if rect1.height > rect2.height:
                return 1
            return 0