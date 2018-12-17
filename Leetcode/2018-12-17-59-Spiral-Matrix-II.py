# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-17 08:57:56
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-17 09:34:05


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        rowtop, coleft, rowbot, colright = 0, 0, n-1, n-1
        while rowbot > rowtop and coleft < colright:
            for i in range(coleft, colright):
                res[rowtop][i] = num
                num += 1
            for i in range(rowtop, rowbot):
                res[i][colright] = num
                num += 1
            for i in range(colright, coleft, -1):
                res[rowbot][i] = num
                num += 1
            for i in range(rowbot, rowtop, -1):
                res[i][coleft] = num
                num += 1
            rowtop += 1
            rowbot -= 1
            coleft += 1
            colright -= 1
        if n % 2:
            for i in range(coleft, colright+1):
                res[rowtop][i] = num
                num += 1
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.generateMatrix(3)
    print(res)
