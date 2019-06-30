# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-28 16:24:44
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-28 16:29:54

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        num = left + ((right - left) >> 1)
        res = guess(num)
        if res == 0: return num

        while res:
            if res == 1:
                left = num + 1
            if res == -1:
                right = num - 1
            num = left + ((right - left) >> 1)
            res = guess(num)

        return num