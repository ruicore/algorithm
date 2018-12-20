# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-20 10:42:47
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-20 11:30:31

import sys
from pprint import pprint


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 获取字符串word1和字符串word2的长度
        numword1, numword2 = len(word1), len(word2)
        # 如果字符串word1长度为0，则字符串1变成字符串2需要numword2步
        if numword1 == 0:
            return numword2
        # 如果字符串2长度为0，则字符串1变成字符串0需要numword1步
        if numword2 == 0:
            return numword1
        # 声明结果数组
        res = []
        # 初始化二维矩阵，每一个位置都初始化为Int类型的最大值
        for _ in range(numword1+1):
            res.append([sys.maxsize for _ in range(numword2+1)])
        # 初始化矩阵第一行，表示一个空字符变成当前长度的字符需要几步
        for row in range(numword1+1):
            res[row][0] = row
        # 初始化矩阵第一列，表示一个空字符变成当前字符需要几步
        for col in range(numword2+1):
            res[0][col] = col
        # 遍历二维数组的每一个位置
        for row in range(1, numword1+1):
            for col in range(1, numword2+1):
                # 如果两个字符串当前字符相等
                if word1[row-1] == word2[col-1]:
                    res[row][col] = min(res[row][col-1]+1,
                                        res[row-1][col-1], res[row-1][col]+1)
                # 如果两个字符当前字符不相等
                else:
                    res[row][col] = min(res[row][col-1]+1,
                                        res[row-1][col-1]+1, res[row-1][col]+1)
        # 返回最后一个位置的值
        return res[numword1][numword2]


if __name__ == "__main__":
    so = Solution()
    res = so.minDistance("intention", "execution")
    pprint(res)
