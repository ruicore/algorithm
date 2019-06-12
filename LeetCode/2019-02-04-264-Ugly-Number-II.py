# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-04 13:35:56
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-04 14:25:45


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglynum = [1]
        # i:2的次数，j:3的次数，k：5的次数，count：丑数的个数
        i, j, k, count = 0, 0, 0, 1
        while count < n:
            # 我们以对应的上一个数为基底，分别对应乘上2，3，5，
            uglyi, uglyj, uglyk = uglynum[i] * 2, uglynum[j] * 3, uglynum[k] * 5
            # 然后我们选择最小的数
            uglynext = min(uglyi, uglyj, uglyk)
            # 我们更新基地
            if uglynext == uglyi: i += 1
            if uglynext == uglyj: j += 1
            if uglynext == uglyk: k += 1
            uglynum.append(uglynext)
            count += 1
        # 返回最后一个数字
        return uglynum[-1]
