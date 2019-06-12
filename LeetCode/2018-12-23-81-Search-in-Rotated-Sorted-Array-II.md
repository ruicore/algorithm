# LeetCode 81. Search in Rotated Sorted Array II

## Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

## 描述

假设按升序排序的数组在事先未知的某个枢轴处旋转。
(例如, [0,0,1,2,2,5,6] 可能变成 [2,5,6,0,0,1,2]).
给定一个要搜索的目标值T， 如果该目标值能在数组中找到则返回true，否则返回false。

例1： 输入：nums = [2,5,6,0,0,1,2]，target = 0 输出：true

例2：输入：nums = [2,5,6,0,0,1,2]，target = 3 输出：false

跟进：

这是在旋转排序数组中搜索的后续问题，其中nums可能包含重复项。
这会影响运行时复杂性吗？ 怎么样和为什么？

### 思路

* 这一题和第33题思路很相似，是[33题](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)的递进题.
* 这道题的变体是数组中可能出现重复元素.
* 我们首先让left指向重复序列的最后一个元素，right指向重复序列的第一个元素.
* 然后我们计算中间值索引middle，如果中间值nums\[middle]==T返回Ture.
* 如果中间值大于等于nums\[left]:如果T在nums\[left]与nums\[middle]之间，我们更新right = middle-1；否则我们更新left = middle+1.
* 如果中间值小于nums\[right]\(由于上边取了等于，这里便可以不用再取等于):如果T在nums\[middle]与nums\[right]之间,我们更新left = middle+1；否则我们更新right = middle -1
* 如果当left大于right时没有找到，我们返回False.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-23 11:15:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 16:13:18


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left, right, middle = 0, len(nums)-1, 0
        # 循环条件，只有当left小于等于right时，循环才执行
        while left <= right:
            # 从左边开始，找到连续相等的数字的最后一个值
            while left < right and nums[left] == nums[left+1]:
                left += 1
            # 从右边开始，找到连续相等的数字的第一个值
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            # 取中间值
            middle = left+((right-left) >> 1)
            print(left, right, middle)
            # 如果中间值和要找的值相等，则返回Ture
            if nums[middle] == target:
                return True
            # 如果左边的数字是连续的
            elif nums[left] <= nums[middle]:
                # 如果target在连续的区间之内
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # 如果右边的区间是连续的
            elif nums[middle] < nums[right]:
                # 如果target在连续的区间之内
                if nums[middle] < target <= nums[right]:
                    left = middle+1
                else:
                    right = middle-1
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.search(nums=[3, 1], target=0)
    print(res)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-23-81-Search-in-Rotated-Sorted-Array-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-81-search-in-rotated-sorted-array-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
