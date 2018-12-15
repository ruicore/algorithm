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
        # 如果矩阵为空，直接返回空
        if not matrix:
            return []
        # 结果数组，用来保存最终答案
        res = []
        # row表示行数，col表示列数
        row, col = len(matrix), len(matrix[0])
        # 第一行行索引，第一列列索引，最后一行行索引，最后一列列索引
        rowtop, coleft, rowbot, colright = 0, 0, row-1, col - 1
        # 循环条件，当矩阵剩余不止一行且不止一列时，才进行循环
        while rowbot > rowtop and coleft < colright:
            # 取第一行
            for i in range(coleft, colright):
                res.append(matrix[rowtop][i])
            # 取最后一列
            for i in range(rowtop, rowbot):
                res.append(matrix[i][colright])
            # 取最后一行
            for i in range(colright, coleft, -1):
                res.append(matrix[rowbot][i])
            # 取第一列
            for i in range(rowbot, rowtop, -1):
                res.append(matrix[i][coleft])
            # 第一行字减一次，进入下一行
            rowtop += 1
            # 最后一行自减一次，进入上一行
            rowbot -= 1
            # 第一列自减一次，进入第二列
            coleft += 1
            # 最后一列自减一次，进入前一列
            colright -= 1
        # 如果最后还剩一行
        if rowtop == rowbot:
            for i in range(coleft, colright+1):
                res.append(matrix[rowtop][i])
        # 如果最后还剩一列
        elif coleft == colright:
            for i in range(rowtop, rowbot+1):
                res.append(matrix[i][coleft])
        return res


if __name__ == "__main__":
    so = Solution()
    res = so.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(res)
