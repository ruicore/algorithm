# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-06 21:42:13
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-06 22:54:54


class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return 0
        # 矩阵的行数和列数
        row, col = len(s), len(s)
        # 初始化矩阵，matrix[i][j]表示s[i:j+1]是否是回文字符串
        matrix = [[False for _ in range(col)] for _ in range(row)]
        # cuts[i]表示s[:i+1]最少需要的切割步数
        cuts, res = [0 for _ in range(row)], row-1
        # 遍历每一个节点
        for end in range(row):
            # s[i]最多切割i次（即i+1个字符最多需要i次切割）
            res = end
            # 检查回文字符串
            for start in range(end+1):
                # 转移条件与转移方程
                # 如果当前字符s[start]与目前正在判断的字符s[end]相等并且
                # 如果从start+1到end-1的连续字符s[start+1:end]构成的字符串是回文字符串(注意: python语法:如s[0:4]不包括末尾字符s[4]))
                # 或者start与end之间的字符小于等于1个，则cuts[i]=cuts[start-1]+1
                # 即从s[start-1]之后再次切割一次，s[i]就可以构成回文字符串.
                if s[start] == s[end] and (end-start <= 2 or matrix[start+1][end-1]):
                    res = min(res, cuts[start-1]+1) if start > 0 else 0
                    matrix[start][end] = True
            cuts[end] = res
        return res
