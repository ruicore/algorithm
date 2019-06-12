# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-05 12:24:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-05 19:45:16


class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        # 如果输入为空，返回0
        if not citations: return 0
        h = 0
        # 对输入的数据排序
        citations.sort()
        # 从后向前遍历
        for item in citations[-1::-1]:
            # 根据题意，至少有h个元素大于h
            h += 1
            # 如果出现当前元素小于h时，说明已经不满足给定的条件，函数返回
            if item < h:
                h -= 1
                break
        return h
