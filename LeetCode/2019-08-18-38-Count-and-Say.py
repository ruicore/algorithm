# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-18 09:49:01
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-18 09:51:29

from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            result = ''.join([str(len(list(g))) + key for key, g in groupby(result)])

        return result
