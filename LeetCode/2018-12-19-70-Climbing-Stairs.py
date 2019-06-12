# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-19 15:20:20
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-19 15:59:32


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 如果只有一层，返回1
        if n == 1:
            return 1
        # 如果有两层，返回2
        if n == 2:
            return 2
        total, preone, pretwo = 0, 2, 1
        # 循环遍历，到达当前的层数的路径数 = 前一层的路径数+前两层的路径数
        for _ in range(3, n+1):
            total = preone + pretwo
            pretwo, preone = preone, total

        return total
