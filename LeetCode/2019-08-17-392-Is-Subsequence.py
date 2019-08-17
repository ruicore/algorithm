# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-17 13:53:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-17 14:34:16

import bisect
from collections import defaultdict


class Solution:
    def __init__(self):
        self.__isinit = False
        self.__dict = defaultdict(list)

    def __build(self, t):
        for index, char in enumerate(t):
            self.__dict[char].append(index)
        self.__isinit = True

    def isSubsequence(self, s: str, t: str) -> bool:
        if not self.__isinit:
            self.__build(t)

        next_ = -1
        for char in s:
            next_ = self.__check(char, next_)
            if next_ == -1:
                return False

        return True

    def __check(self, char, index):
        if char not in self.__dict:
            return -1
        next_ = bisect.bisect_right(self.__dict[char], index)
        return self.__dict[char][next_] if next_ < len(self.__dict[char]) else -1
