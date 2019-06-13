# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-13 14:35:51
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-13 14:42:06


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            middle = left + ((right - left) >> 1)
            tmp = middle ** 2
            if tmp == num:
                if isinstance(middle, int):
                    return True
            elif tmp < num:
                left = middle + 1
            else:
                right = middle - 1

        return False
