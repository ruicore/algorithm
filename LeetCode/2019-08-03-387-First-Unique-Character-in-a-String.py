# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-03 21:18:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-03 21:35:58

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = len(s)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            left, right = s.find(char), s.rfind(char)
            if left != -1 and left == right:
                res = min(res, left)

        return -1 if res == len(s) else res
