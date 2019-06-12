# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 21:47:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 21:54:18


class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 中间位置的索引，最后一个位置的索引
        half, count = len(s) // 2, len(s) - 1
        for i in range(half):
            s[i], s[count - i] = s[count - i], s[i]