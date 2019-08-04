# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-04 22:45:02
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-04 23:08:14


class Solution(object):
    def lengthLongestPath(self, input):

        max_length = 0
        dot, blank = '.', ''
        stack = [(-1, 0)]  # -1 表示目录深度，0 表示当前所有字符串的长度

        for name in input.split("\n"):
            level = name.count('\t')
            name = name.replace('\t', blank)
            # 去当前的目录深度
            while stack and level <= stack[-1][0]:  # 如果一样深，或者当前目录的层级更浅
                stack.pop()
            if dot not in name:  # 如果是目录
                stack.append((level, len(name) + stack[-1][1] + 1))
            else:  # 如果是文件
                max_length = max(max_length, len(name) + stack[-1][1])

        return max_length
