# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-11-13 20:51:10
# @Last Modified by:   何睿
# @Last Modified time: 2018-11-13 20:51:10


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for item in S:
            if item == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(item)
        for item in T:
            if item == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(item)
        return stack_s == stack_t
