# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 16:58:04
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 17:11:49


class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        # num 数字不为零
        # num 的二级制只有一个 1
        # num 中 1 的位置出现在第 1 位，或第 3 位，或第5 ... 位
        return num != 0 and num & (
            num - 1) == 0 and num & 0b1010101010101010101010101010101 == num
