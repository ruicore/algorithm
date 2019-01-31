# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-31 17:04:06
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-31 17:29:56


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 无论是2的多少次方，用二进制表示，只会有一个1
        res = 0
        while n > 0:
            res += (n & 1)
            n >>= 1
        return res == 1