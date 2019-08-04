# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-04 23:09:19
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-04 23:09:30

import operator
from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(operator.xor, map(ord, s + t), 0))


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
