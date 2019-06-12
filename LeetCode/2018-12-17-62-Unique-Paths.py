# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-17 15:47:16
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-17 15:47:16


class Solution:
    def __init__(self):
        self.res = []

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        self.res = [[0 for _ in range(n)] for _ in range(m)]
        return self.recursion(m, n)

    def recursion(self, m, n):
        # 递归结束条件，当到达最左边的时候或者到达最上层的时候，结束递归
        if m == 1 or n == 1:
            return 1
        # 递归检查，检查当前位置是否已经遍历过，如果是则直接返回
        if self.res[m-1][n-1] > 0:
            return self.res[m-1][n-1]
        # 获得走到此位置左边的走法
        left = self.recursion(m, n-1)
        # 获得此位置右边的走法
        top = self.recursion(m-1, n)
        # 记录当前位置的走法
        self.res[m-1][n-1] = left+top
        # 返回
        return self.res[m-1][n-1]


if __name__ == "__main__":
    so = Solution()
    res = so.uniquePaths(7, 3)
    print(res)
