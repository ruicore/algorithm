# LeetCode 74. Search a 2D Matrix

## Description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

## 描述

编写一个有效的算法，搜索m×n矩阵中的值。 此矩阵具有以下属性:

每行中的整数从左到右排序.
每行的第一个整数大于前一行的最后一个整数.

### 思路

* 给定一个排好序的二维数组，查找一个值，如果该值在数组中返回Ture，不在返回False.
* 此题目考察[二分法](https://zh.wikipedia.org/zh-hans/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95).

```python
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

```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-21-74-Search-a-2D-Matrix.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-74-search-a-2d-matrix/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
