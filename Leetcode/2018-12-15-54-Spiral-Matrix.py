# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-15 15:10:04
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-15 15:45:27


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        row, col = len(matrix), len(matrix[0])
        rowtop, coleft, rowbot, colright = 0, 0, row-1, col - 1
        while rowbot > rowtop and coleft < colright:
            for i in range(coleft, colright):
                res.append(matrix[rowtop][i])
            for i in range(rowtop, rowbot):
                res.append(matrix[i][colright])
            for i in range(colright, coleft, -1):
                res.append(matrix[rowbot][i])
            for i in range(rowbot, rowtop, -1):
                res.append(matrix[i][coleft])
            rowtop += 1
            rowbot -= 1
            coleft += 1
            colright -= 1
        if rowtop == rowbot:
            for i in range(coleft, colright+1):
                res.append(matrix[rowtop][i])
        elif coleft == colright:
            for i in range(rowtop, rowbot+1):
                res.append(matrix[i][coleft])
        return res

if __name__ == "__main__":
    so = Solution()
    res = so.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(res)
