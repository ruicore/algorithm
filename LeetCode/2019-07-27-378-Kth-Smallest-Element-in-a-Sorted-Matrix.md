# LeetCode 378. Kth Smallest Element in a Sorted Matrix

## Description

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

```py
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```
## 描述

给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

```py
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

#### 思路一

* 使用堆，维护一个最大堆，限定堆中的元素个数为 k ，将所有的元素依次压入堆中，当堆中元素大于 k 时，pop 出最大的元素。堆中最后一个元素即是所有。
* python3 没有实现最大堆而是实现了最小堆，我们将每一个数乘以 -1，使用最小堆来模拟最大堆。

```py
import heapq

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count_row, count_col = len(matrix), len(matrix[0])
        if not matrix:
            return 0
        heap = []
        for i in range(count_row):
            for j in range(count_col):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heap[0]
```
#### 思路二

* 使用二分法，二分的对象是数组中数字的大小范围。
* 其基本思路是：small，big 分别表示数组中最小和最大的数，midlle = （small + big）//2，统计数组中小于等于 midlle 元素的个数，记为 count；如果 count 大于等于 k，说明第 k 大的数 在 small 到 big 之间；如果 count 小于 k，说明第 k 大的数应该在 middle+1 到 big 之间；不断利用二分法，直到 small == big，此时一定有数组小于等于 small 数的个数为 k；
* 关于如何统计数组中小于的等于 k 的数，利用了 leetcode 第 74 题 [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) 的思想，其解析在[这里](https://www.ruicore.cn/leetcode-74-search-a-2d-matrix/)。

```py

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        small, big = matrix[0][0], matrix[-1][-1]
        while small < big:
            middle = small + ((big - small) >> 1)
            count = self.less_eq_than_k(matrix, middle)
            if count >= k:
                big = middle
            if count < k:
                small = middle + 1

        return small

    def less_eq_than_k(self, matrix: List[List[int]], middle: int) -> int:
        count, i, j = 0, 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= middle:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-07-27-378-Kth-Smallest-Element-in-a-Sorted-Matrix.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-378-kth-smallest-element-in-a-sorted-matrix/) ，作者信息和本声明.