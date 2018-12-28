# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-28 09:26:14
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-28 10:23:43

from pprint import pprint

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 动态规划，使用二维矩阵.
        # 获取矩阵的行数和列数.
        row, col = len(s1), len(s2)
        # 如果字符串1的长度加上字符串2的长度不等于字符串3的长度
        # 则字符串3一定不可以由字符串s1和字符串s2交替构成.
        if row + col != len(s3):
            return False
        # 生成二维矩阵
        matrix = [[False for _ in range(col+1)] for _ in range(row+1)]
        # 0 0 表示从s1中取0个字符，从s2中取0个字符用来构成S3中的空字符，可以构成，则设为True.
        matrix[0][0] = True
        # 初始化第一行，当s2的当前位置与s3相等并且s2当前位置的前一串能够构成s3的字符串，设为True.
        for i in range(1, col+1):
            matrix[0][i] = True if matrix[0][i - 1] and s2[i-1] == s3[i-1] else False
        # 初始化第一列，当s1的当前位置与s3相等并且s1当前位置的前一串能够构成s3的字符串，设为True.
        for i in range(1, row):
            matrix[i][0] = True if matrix[i -1][0] and s1[i-1] == s3[i-1] else False
        for i in range(1,row+1):
            for j in range(col+1):
                # 循环遍历检查每一个位置
                # 如果当前位置的上一个位置为True，我们就尝试从s1中取出一个字符i与s3中的i+j-1比较，如果相等当前位置设为True.
                # 如果当前位置的左一个位置为True，我们就尝试从s2中取出一个字符i与s3中的i+j-1比较，如果相等当前位置设为True.
                if (matrix[i-1][j] and s1[i-1] == s3[i+j-1]) or (matrix[i][j-1] and s2[j-1] == s3[i+j-1]):
                    matrix[i][j] = True
                # 如果上一个位置为False且左一个位置为False，或者当前位置s1[i-1]与s3[i+j-1]不等且s2[j-1]与s3[i+j-1]不等,
                # 当前位置设为False
                else:
                    matrix[i][j] = False
        return matrix[row][col]

if __name__ == "__main__":
    so = Solution()
    res = so.isInterleave(s1 = "a", s2 = "b", s3 = "a")
    print(res)