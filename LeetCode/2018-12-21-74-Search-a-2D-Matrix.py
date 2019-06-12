# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-21 10:33:47
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-21 10:56:40


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 如果矩阵为空，返回False
        if not matrix or not matrix[0]:
            return False
        # 二分法遍历，首先确定target在哪一行
        left, right, middle = 0, len(matrix)-1, 0
        while left <= right:
            middle = left+((right-left) >> 1)
            if matrix[middle][0] < target:
                left = middle+1
            elif matrix[middle][0] > target:
                right = middle-1
            else:
                return True
        row = right
        left, right = 0, len(matrix[0])-1
        # 二分法遍历，确定当前值在哪一个位置
        while left <= right:
            middle = left+((right-left) >> 1)
            if matrix[row][middle] < target:
                left = middle+1
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                return True
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.searchMatrix(
        [[]], 1001)
    print(res)
