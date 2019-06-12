# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 12:57:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 14:28:55


class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        # 如果是负数，直接返回零
        if n <= 0: return res
        # 当前位置左边的所有数，当前位置的值，当前位置右边的值
        left, right, middle, factor = 1, 1, 1, 1
        # 循环条件，当left不为零（即左边还有数的时候）
        while left:
            # 取左边部分
            left = n // (factor * 10)
            # 取当前位置的值
            middle = n // factor % 10
            # 取当前位置右边的值
            right = n % factor
            # 如果当前位置的值为0
            if middle == 0:
                res += left * factor
            # 如果当前的值为1
            elif middle == 1:
                res += left * factor + right + 1
            # 如果当前的值大于等于2
            else:
                res += (left + 1) * factor
            factor *= 10
        # 返回最终的结果
        return res