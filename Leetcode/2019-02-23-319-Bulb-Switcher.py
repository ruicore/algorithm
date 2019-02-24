# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-23 18:46:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-23 19:46:07


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)

    def bulbSwitch2(self, n: int) -> int:
        count, i = 0, 3
        # 首项为3，公差为 2 的等差数列
        # n 为这些数字的和
        while n > 0:
            # 每次从 n 中去掉一项
            n -= i
            i += 2
            # 记录去掉的次数
            count += 1
        # 次数就是剩下的晾着的灯泡个数
        return count

    def bulbSwitch3(self, n: int) -> int:
        # 最直观的思路，用一个数组表示灯泡的开关情况，0 表示关，1 表示开
        # !!! 此方法会超时
        bulbs = [0 for i in range(n)]
        for i in range(n):
            j = i
            # 每轮调整 i 整数倍的位置
            while j < n:
                bulbs[j] ^= 1
                j += i + 1
        # 统计最后剩下的 1 的个数
        return bulbs.count(1)
