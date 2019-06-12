# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 13:01:11
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 13:45:27


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        # 从矩阵的右上角开始寻找（左下角也可以）
        # 从右上角开始，如果向左走则所有的元素递减；如果向下走所有的元素递增
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            # 如果相等，返回True
            if matrix[row][col] == target: return True
            # 如果当前位置元素更大，由于当列的元素都大于当前元素
            # 即target不在当前列中，col自减一次
            if matrix[row][col] > target: col -= 1
            # 如果当前位置的元素更小，由于当前元素在行的末尾
            # （当前元素后面的元素已经被列判定给否定了）
            # 当前元素前面的元素前面的元素都小于当前元素
            # 即target不在当前行中，row自增一次
            if matrix[row][col] < target: row += 1
        return False