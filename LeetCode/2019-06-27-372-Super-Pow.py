# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-27 20:41:08
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-27 21:26:34

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for num in b:
            res = self.pow(res, 10) * self.pow(a, num) % 1337
        return res

    def pow(self, x: int, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return x % 1337
        return x**n % 1337