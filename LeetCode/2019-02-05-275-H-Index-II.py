# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-05 12:27:25
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-05 19:58:17


class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        # 如果给定的数组为空，返回0
        if not citations: return 0
        count = len(citations)
        # 采用二分查找的思想
        left, right, milldle = 0, count - 1, 0
        while left <= right:
            # 去掉左边的所有非零项
            while left < count and citations[left] == 0:
                left += 1
            milldle = ((right - left) >> 1) + left
            # 如果当前位置元素值大于等于从当前位置往后数（包括当前元素）的元素个数
            if citations[milldle] >= (count - milldle):
                right = milldle - 1
            # 如果当前位置元素值小于从当前位置往后数（包括当前元素）的元素个数            
            elif citations[milldle] < (count - milldle):
                left = milldle + 1
        # 返回元素个数
        return count - left
