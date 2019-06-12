# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-19 15:35:20
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-19 16:11:26


class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        """
        :type n: int
        :rtype: int
        """
        # 处理特殊情况，如果n为1或者primes为空，返回1
        if n < 2 or not primes: return 1
        # 声明一个数组，用于存储获取的丑数
        uglynum = [1]
        # 辅助变量，primes的个数，当前生成的丑数的个数
        num, count = len(primes), 1
        # index数组用于存储primes中每个数上一次产生有效数的下一个位置
        index = [0 for _ in range(num)]
        while count < n:
            # 动态规划，用primes中的每个数从上一次产生有效位置的地方产生下一个数
            _next = [primes[i] * uglynum[index[i]] for i in range(num)]
            # 下一个丑数是产生的丑数中最小的数
            uglynext = min(_next)
            # 更新索引值
            for i in range(num):
                if uglynext == _next[i]: index[i] += 1
            uglynum.append(uglynext)
            count += 1
        # 返回最后一个丑数
        return uglynum[-1]
