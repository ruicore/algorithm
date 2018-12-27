# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-27 17:11:58
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-27 17:51:07


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0 for _ in range(n+1)]
        nums[0] = 1
        nums[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                # 递归关系式
                nums[i] += nums[i-j-1]*nums[j]
        return nums[n]
