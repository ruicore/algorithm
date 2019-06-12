# LeetCode 153. Find Minimum in Rotated Sorted Array

## Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

## 描述

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

### 思路

* 此题目考察[二分法](https://zh.wikipedia.org/zh-hans/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95).
* 二分法的关键是判断需搜索的值是在当前位置的左边还是当前位置的右边.
* 此题目中，在没有重复的情况下，一个递增的序列从某个位置p旋转，最小值会小于新数组的左右两端的数值,会使得从数组不在连续递增.反过来说，如果某一段数组连续递增，那么转换的枢纽一定不在此段中.
* 因此，我们计算中间值，如果数组nums\[middle]>nums\[0],说明从0到middle（包括）一直在递增，那么要求的枢纽一定在middle（不包括middle本身）右边.
* 同理如果，nums\[middle]<\nums[-1]（-1表示最后一个元素），说明从middle到最后一个元素一直在递增，那么要求的枢纽一定在middle左边（包括middle本身，因为middle可能是枢纽本身）.
* 最后找到了middle会满足nums\[middle] < nums\[middle + 1] < nums\[middle - 1]

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-15 13:52:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-15 16:00:40


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果为空，则直接返回
        if not nums:
            return 0
        # left为最左边的索引，right为最右边的索引
        left, right = 0, len(nums) - 1
        # 首先获取中间值
        middle = left + ((right - left) >> 1)
        # 如果是连续递增的请情况，返回数组的第一个值
        if nums[0] <= nums[middle] <= nums[-1]:
            return nums[0]
        # 如果是连续递减的情况，返回最后一个值
        if nums[-1] <= nums[middle] <= nums[0]:
            return nums[-1]
        while left < right:
            middle = left + ((right - left) >> 1)
            # 结束条件，交换的位置满足下面的条件
            if nums[middle] < nums[middle + 1] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[0]:
                left = middle + 1
            # 注意这里不是middle-1，因为有可能middle就是要求的枢纽位置
            if nums[middle] < nums[-1]:
                right = middle
        return nums[left]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-15-153-Find-Minimum-in-Rotated-Sorted-Array.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-153-find-minimum-in-rotated-sorted-array/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
