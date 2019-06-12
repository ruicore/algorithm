# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-13 17:19:45
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-13 19:05:32


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 如果n等于0，则不论x为何值，返回1
        if n == 0:
            return 1
        # 如果n为负数，则转换为(1/x)^(-n)的形式
        if n < 0:
            x = 1/x
            n = -n
        # 初始化res为1
        res = 1
        while n > 1:
            # 如果n为奇数，res则需要乘以x一次
            if n % 2:
                res *= x
            # x自乘一次
            x *= x
            # n整除2
            n //= 2
        return res*x


if __name__ == "__main__":
    so = Solution()
    res = so.myPow(2, 10)
    print(res)
