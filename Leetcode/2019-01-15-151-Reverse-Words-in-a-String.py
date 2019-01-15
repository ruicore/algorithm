# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 09:50:21
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 10:01:15


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        relist = s.split(" ")
        if not relist:
            return ''
        res = ''
        for i in range(len(relist) - 1, -1, -1):
            if relist[i]:
                res += relist[i] + " "
        return res[:-1]
