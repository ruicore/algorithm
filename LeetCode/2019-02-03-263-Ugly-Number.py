# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-03 09:30:18
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-03 10:05:52


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        for factor in [2, 3, 5]:
            while not num % factor:
                num /= factor
        if num == 1: return True
        return False