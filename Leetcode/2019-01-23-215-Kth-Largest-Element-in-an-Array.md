# LeetCode 215. Kth Largest Element in an Array

## Description

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

## 描述

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

### 思路

* 这道题使用快速排序的分区部分，快速排序的每一次分区都随机将一个元素放置在了最终位置.
* 我们对原数组进行不断的分区，如果当前确定的元素在第k大元素的左边，我们就对当前元素右边的元素进行排序；如果当前元素在第k大元素的右边，我们就对当前元素左边的元素进行排序，直到找到第K的元素为止.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-23 22:57:06
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-26 20:23:38


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        # 
        pivot = self._quicksort(nums, left, right)
        while pivot != k - 1:
            # 如果当前确定的位置在k的左边，说明要求的元素应该在右边
            if pivot < k - 1:
                left = pivot + 1
            # 如果当前确定的位置在k的右边，说明要求的元素应该在左边
            elif pivot > k - 1:
                right = pivot - 1
            pivot = self._quicksort(nums, left, right)
        return nums[pivot]

    # 快速排序
    def _quicksort(self, nums, left, right):
        pivot, j = right, left
        for i in range(left, right):
            if nums[i] > nums[pivot]:
                if j != i:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[pivot] = nums[pivot], nums[j]
        # 返回当前已经确定元素的索引
        return j
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-23-215-Kth-Largest-Element-in-an-Array.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-215-kth-largest-element-in-an-array/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
