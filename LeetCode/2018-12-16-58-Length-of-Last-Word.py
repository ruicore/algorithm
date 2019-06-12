# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-16 16:59:53
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-16 17:09:53

import re

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            split_words = s.split()
            return len(split_words[-1])
        except:
            return 0
            
        