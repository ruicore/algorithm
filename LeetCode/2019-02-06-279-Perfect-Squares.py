# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-06 09:19:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-06 17:33:50


class Solution:
    def numSquares(self, n: 'int') -> 'int':
        # 动态规划数组，dynamic[i]表示数字i可以最少可以有i个平方数相加
        dynamic = [x for x in range(n + 1)]
        # 生成候选完全平方数，n仅可能由这些数构成
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        # 完全平方数只需要1个数相加，即自己本身
        for item in squares:
            dynamic[item] = 1
        # 动态转移方程
        for i in range(1, n + 1):
            # 将每一个位置的值和完全平方数组合
            for sq in squares:
                if i + sq <= n:
                    dynamic[i + sq] = min(dynamic[i] + 1, dynamic[i + sq])
        return dynamic[-1]

    def numSquares2(self, n: 'int') -> 'int':
        # 参考四平方和定理：https://zh.wikipedia.org/wiki/四平方和定理
        # 即每个正整数均可表示为4个整数的平方和
        # 数字4a和a需要的平方数相同
        while n % 4 == 0:
            n //= 4
        # 如果n对8取模结果为7，n一定由4个平方数组成
        if n % 8 == 7: return 4
        # 处理两个和1个平方和的情况
        i = 0
        sq = i**2
        while sq <= n:
            j = int((n - sq)**0.5)
            # n由两个平方数组成
            if sq + j * j == n:
                if i != 0 and j != 0: return 2
                else: return 1
            i += 1
            sq = i * i

        #如果执行到这里，说明n不由1，2，4个平凡数字组成，返回3
        return 3
