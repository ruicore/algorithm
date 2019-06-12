# LeetCode 321. Create Maximum Number

## Description

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

```py
Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
```

Example 2:

```py
Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
```

Example 3:

```py
Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
```

## 描述

给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

```py
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
```

示例 2:

```py
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
```

示例 3:

```py
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
```

### 思路

* 子问题 1 ：对于一个给定的无序整数数组，从其中找出 k 个数构成一个新的整数，k 个数之间的相对位置不变，使得新构成的整数的值最大。我们借助栈来实现，我们即给的给定的数组的元素为 n，需要的取出的元素个数为 k，剩下的元素个数为 t = n - k，我们不断的遍历数组中的元素，如果当前元素比栈顶的元素大，并且此时剩下的可以被踢掉的元素个数 t 大于零，我们弹出栈顶元素；否则我们将当前元素压入栈顶。
* 子问题 2 ：给定两个数组，从这两个数组中交替的选数字出来，只能从前往后选，构成一个新数组，使得这个数组最大。「数组大小的比较：依次标胶每一个元素，遇到第一数大的数组大」。用两个队列来实现，如果队列 1 大于队列 2，我们弹出队列 1 的元素到结果数组中，否则弹出队列 2 的元素，直到所有的元素都被取完。
* 本题：我们从第一个数组中取 i 个元素找到一个最数组，从第二个数组中取出 k - i 个数构成最大数组，将两个数组合并构成新的数组，在所有的新的数组中我们取最大的数组。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-24 14:35:27
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-26 16:08:04

from collections import deque


class Solution:
    def maxNumber(self, nums1: [int], nums2: [int], k: int) -> [int]:
        ans = []
        for i in range(k + 1):
            # 如果已经超出了第一个数组的范围，循环结束
            if i > len(nums1): break
            # 如果 k - i 比第二个数组的元素个数更多，
            # 说明第二个数组不能够提供足够的元素，继续循环
            if k - i > len(nums2): continue
            # 产生新的组合
            newans = self._merge(self._Max(nums1, i), self._Max(nums2, k - i))
            # 取最大的组合
            ans = max(ans, newans)
        return ans

    def _Max(self, nums, k):
        # 需要去掉的个数
        drop = len(nums) - k
        stack = []
        # 遍历每一个元素
        for num in nums:
            # 如果栈不为空 并且 drop 大于零 并且 num 大于栈顶元素
            while stack and drop > 0 and num > stack[-1]:
                # 弹出栈顶元素
                stack.pop()
                # 需要弹出的元素个数减一
                drop -= 1
            stack.append(num)
        # 返回前 k 个元素
        return stack[:k]

    def _merge(self, num1, nums2):
        # 将列表转换成队列
        queue1 = deque(num1)
        queue2 = deque(nums2)
        res = []
        while queue1 and queue2:
            # 队列大小的比较
            # 对队列每个元素从前向后比较，只要有一个比较大，则该队列比较大
            if queue1 > queue2: res.append(queue1.popleft())
            else: res.append(queue2.popleft())
        # 添加队列剩下的元素
        if queue1: res += queue1
        if queue2: res += queue2
        return res
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-24-321-Create-Maximum-Number.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-321-create-maximum-number/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-321-create-maximum-number/) ，作者信息和本声明.
