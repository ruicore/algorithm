# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-07 11:54:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-07 12:22:34


class Solution:
    def countBits(self, num: int) -> [int]:
        # 结果数组
        result, count = [0], 1
        while count * 2 <= num:
            # 从 resut 数组中索引对应的二进制数前面加
            # 一个 1 构成范围从 count 到 count*2 -1 的数（包括两端）
            for i in range(count, count * 2):
                result.append(1 + result[i - count])
            count *= 2
        # 处理剩下的数
        for i in range(count, num + 1):
            result.append(1 + result[i - count])
        return result