# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 12:35:48
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 12:50:51


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        # pre用来存储上一行的信息
        pre = [1, 1]
        if rowIndex == 1:
            return pre
        for i in range(2, rowIndex+1):
            res = [1 for _ in range(i+1)]
            for j in range(1, i):
                res[j] = pre[j]+pre[j-1]
            pre = res
        return res
