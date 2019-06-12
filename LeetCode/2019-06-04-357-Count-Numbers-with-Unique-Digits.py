# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-04 13:40:45
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-04 14:57:30


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # n 最大为 9
        n = n if n < 10 else 9
        # 当 n 为 0 时，只有 0 满足条件
        if n == 0: return 1
        # count 记录当限定位数为 i 时，能够形成的做多的 unique number 个数
        # res 记录总和
        count, res = 9, 10
        for i in range(2, n + 1):
            count *= 11 - i
            res += count

        return res
