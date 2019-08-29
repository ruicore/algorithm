# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-29 21:06:55
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-29 21:41:26


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            count += 1
            if not n % 2:
                n >>= 1
            elif n & 0b11 == 0b11 and n != 0b11:
                n += 1
            else:
                n -= 1

        return count
