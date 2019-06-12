# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-27 19:47:01
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-27 19:47:01

import collections


class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]