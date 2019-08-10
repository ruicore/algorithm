# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-10 08:12:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-10 08:31:09


class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.leftright(n)

    def leftright(self, n):
        if n <= 2:
            return n
        if n & 1 == 1:  # 奇数
            return 2 * self.rightleft((n - 1) >> 1)
        else:
            return 2 * self.rightleft(n >> 1)

    def rightleft(self, n):
        if n <= 2:
            return 1
        if n & 1 == 1:
            return 2 * self.leftright((n - 1) >> 1)
        else:
            return 2 * self.leftright(n >> 1) - 1
