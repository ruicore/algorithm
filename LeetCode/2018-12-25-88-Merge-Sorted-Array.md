# LeetCode 88. Merge Sorted Array

## Description

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

## 描述

* 题意是给定了两个排好序的数组，让把这两个数组合并,不要使用额外的空间，把第二个数组放到第一个数组之中.
* 两个数组nums1，长度m，数组nums2，长度n，我们从两个数组的末尾，p，q开始比较，我们把较大的数放在p+q+1的位置.
* 如此循环，最后把nums2剩下的元素放到nums1即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 17:10:16
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 17:10:16


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # p,q分别指向数组的最后一个位置.
        p, q = m-1, n-1
        # 当数组不为空的才进行循环.
        while p >= 0 and q >= 0:
            # 把较大的数放在末尾
            if nums1[p] > nums2[q]:
                nums1[p+q+1] = nums1[p]
                p = p-1
            else:
                nums1[p+q+1] = nums2[q]
                q = q-1
        # 把nums2剩下的元素放在nums1中.
        nums1[:q+1] = nums2[:q+1]


if __name__ == "__main__":
    so = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    so.merge(nums1, 3, nums2, 3)
    print(nums1)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-25-88-Merge-Sorted-Array.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-88-merge-sorted-array/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
