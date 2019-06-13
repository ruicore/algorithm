# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-13 11:03:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-13 12:20:44


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or (z <= x + y and z % self.__gcd(x, y) == 0):
            return True
        return False

    def __gcd(self, x: int, y: int) -> int:
        return x if y == 0 else self.__gcd(y, x % y)
