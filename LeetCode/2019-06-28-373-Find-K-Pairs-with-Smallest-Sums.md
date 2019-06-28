# LeetCode 373. Find K Pairs with Smallest Sums

## Description

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

```py
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

Example 2:

```py
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

Example 3:

```py
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
```

## 描述

给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

示例 1:

```py
输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

示例 2:

```py
输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

示例 3:

```py
输入: nums1 = [1,2], nums2 = [3], k = 3 
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
```

### 思路

* 使用小顶堆。
* 首先将 nums1 的第一个数和 nums2 的前 k 个数组合，并存入索引，构成（nums1\[0]+nums\[i],0,i）结构，存入堆中。
* 每次从堆中取出最小元素对，假定此时的最小元素对由 nums1\[i] 和 nums2\[j] 构成；由于我们已经 nums2 中的前 k 个元素压入了堆中， 那么在 nums1 和 nums2 剩下的元素中，大于元素对 （nums1\[i] + nums2\[j]，i，j） 的最小元素对就是 （nums1\[i+1] + nums2\[j]，i+1，j），我们将此压入堆中。
* 重复上面的步骤直到取出了 k 个元素对（或者堆空）。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-28 10:56:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-28 11:40:14

from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # 处理异常情况
        if not nums1 or not nums2:return []

        heap = list()
        len1, len2 = len(nums1), len(nums2)

        # k 对最小数对的和，所有的数一定都落在 nums1 和 nums2 的前 k 个数中
        num = k if len2 > k else len2

        # 将第一个数组的第一个数与第二个数组的前 k 个数组合
        for i in range(num):
            heappush(heap, (nums1[0]+nums2[i], 0, i))
        count = 0
        res = list()

        # 取 k 个有效数对

        while heap and count < k:
            
            # 最小数对是 (nums1[i], nums2[j])
            _sum, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            count += 1
            if i + 1 < len1:
                # 取到了最小数对 (nums1[i], nums2[j])
                # 我们将比最小数对大的最小数对 (nums1[i+1], nums2[j]) 压入堆中
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        del heap

        return res
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-06-28-373-Find-K-Pairs-with-Smallest-Sums.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-373-find-k-pairs-with-smallest-sums/) ，作者信息和本声明.
