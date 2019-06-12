# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 12:11:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 12:21:44


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 如果行数等于0，则返回空
        if numRows == 0:
            return []
        # 如果行数为1，则最终结果只有一行
        elif numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        # 生成一行的数
        for i in range(2, numRows):
            res.append([1 for _ in range(i+1)])
            # 当前位置的值等于上一行当前位置的值+上一行当前位置前一个位置的值
            for j in range(1, i):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        return res
