# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 21:06:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 18:50:47


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numset = set()
        newn = self.square(self.divide(n))
        # 如果求和的结果没有出现过
        while newn not in numset:
            numset.add(newn)
            newn = self.square(self.divide(newn))
            # 如果等于1，返回True
            if newn == 1: return True
        # 若求和的结果已经出现且不等于1，返回False
        return False

    # 拆分函数，返回list
    def divide(self, n):
        res = []
        while n:
            res.append(n % 10)
            n //= 10
        return res

    # 返回所有数子的平方和
    def square(self, nums):
        return sum([x**2 for x in nums])
