# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-05 16:35:35
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-05 16:35:35


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分查找，左边界，右边界
        left, right, middle = 1, n, 0
        while left <= right:
            middle = ((right - left) >> 1) + left
            # isBadVersion 函数由主调函数提供
            # 如果当前位置的右边
            if not isBadVersion(middle):
                # 结束条件
                if isBadVersion(middle + 1):
                    return middle + 1
                left = middle + 1
            # 如果在当前位置的左边
            else:
                right = middle - 1
        # 如果第一个元素就坏了，返回1
        if right == 0: return 1