# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 17:35:39
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 18:15:43


class Solution:
    def integerBreak(self, n: int) -> int:
        # 前 5 个数的最大乘积
        tmp = [1, 2, 4, 6, 9]
        for i in range(5, n - 1):
            # 动态规划：第 i 个数 的最大乘积为 3 * 往前数第三个数
            tmp.append(3 * tmp[i - 3])
        return tmp[n - 2]

    def integerBreak2(self, n: int) -> int:
        # 思路与上面的思路一致，优化了空间
        if n == 2: return 1
        if n == 3: return 2
        tmp = [4, 6, 9]
        for i in range(n - 6):
            tmp[i % 3] *= 3
        return tmp[(n - 1) % 3]
