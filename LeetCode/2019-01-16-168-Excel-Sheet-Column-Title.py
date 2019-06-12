# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 18:54:24
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 19:00:18


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 此题目相当于进制转换
        s = []
        while n > 0:
            # 索引转换
            n -= 1
            s.append(chr(65 + int(n % 26)))
            n = n // 26
        return ''.join(reversed(s))
