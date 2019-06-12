# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 23:27:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 23:29:33


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        b = num % 9
        return b if b != 0 else 9
