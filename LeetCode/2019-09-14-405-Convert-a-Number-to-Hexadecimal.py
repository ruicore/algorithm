# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-14 10:47:02
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-14 11:07:11


class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = 0xffffffff + 1 + num

        transfer = "0123456789abcdef"
        res = []
        while num:
            res.append(transfer[num % 16])
            num >>= 4

        return ''.join(reversed(res)) or '0'
