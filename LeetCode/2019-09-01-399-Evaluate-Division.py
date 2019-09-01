# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-01 12:45:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-01 16:28:09

from typing import List
from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.__build_graph(equations, values)
        return list(map(lambda query: self.__query(graph, query[0], query[1], set()), queries))

    def __build_graph(self, equations, values):
        graph = defaultdict(dict)
        for e, v in zip(equations, values):
            root, node = e
            graph[root][node] = v
            graph[node][root] = 1 / v

        return graph

    def __query(self, garph, start, end, visited):

        if start not in garph and end not in garph:
            return -1.0
        if start == end:
            return 1.0

        visited.add(start)
        for next_ in garph[start]:
            if next_ in visited:
                continue
            tmp = self.__query(garph, next_, end, visited)
            if tmp > -1:
                return tmp * garph[start][next_]

        return -1
