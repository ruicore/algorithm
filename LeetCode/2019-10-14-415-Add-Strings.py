# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-10-14 19:42:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-10-14 19:47:43


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self._int(num1) + self._int(num2))

    def _int(self, num):
        res = 0
        cnt = 1
        for s in num[::-1]:
            res += cnt * (ord(s) - ord('0'))
            cnt *= 10
        return res
