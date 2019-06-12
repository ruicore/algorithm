# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 13:01:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 14:03:49

import sys


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        for i in range(1, rows):
            col = len(triangle[i])
            for j in range(col):
                # 如果没有越界
                if j-1 >= 0:
                    one = triangle[i-1][j-1]
                # 如果越界则置为最大值
                else:
                    one = sys.maxsize
                # 如果没有越界
                if j < i:
                    two = triangle[i-1][j]
                # 如果越界则置为最大值
                else:
                    two = sys.maxsize
                # 当前位置只能来源于当前位置对应的上一层的左右两个位置，取其最小值于当前位置的值相加，就是走到当前位置的最小路径和
                triangle[i][j] = triangle[i][j]+min(one, two)
        return min(triangle[rows-1])


if __name__ == "__main__":
    so = Solution()
    res = so.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(res)
