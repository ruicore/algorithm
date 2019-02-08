# LeetCode 287. Find the Duplicate Number

## Description

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

## 描述

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

### 思路

#### 1. 二分法

* 我们用left，right来表示重复的数字所在的范围.对于一组连续递增的数（如1，2，3，4……n），我们取中间值middle，middle把这组数分成了左右两边（我们把middle归为左边）,则
* 1.如果有奇数个，则左边数的个数 == 右边数的个数+1，这时我们添加一个数使得原数组出现重复，如果重复的数落在了左边，则左边的数>右边的数；如果重复的数出现在了右边，则左边数的个数 == 右边数的个数.
* 2.如果有偶数个，则左边数的个数 == 右边的个数，这时我们添加一个数使得原数组出现重复，如果重复的数落在了左边，则左边的数>右边的数；如果重复的数出现在了右边，则左边数的个数 < 右边数的个数.
* 所以如果重复的数出现在左边，则一定有左边数的个数>右边的数的个数；如果重复的数出现在右边，则左边数的个数<=右边数的个数.
* 于是对于题中给定的数组，我么用count来统计小于等于middle的数，如果count<=middle(middle刚好表示数组左边的数的个数)，说明重复的数在middle的右边，即重复的数比middle大，我们更新left=middle+1；如果count>middle说明重复的数比middle小，我们更新right = middle-1

#### 2.环形链表

* 这道题与可以转换为[142题Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)
![LeetCode 287. Find the Duplicate Number](https://www.ruicore.cn/wp-content/uploads/2019/02/LeetCode-287.-Find-the-Duplicate-Number.svg)
* 如上图，我们将第一个索引初始化为0，然后将数组0号元素的值作为下一次访问的索引，如此下去，会发现访问会形成一个环，并且重复元素为环的第一个位置.

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-07 16:19:11
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 19:29:25


class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        # 二分法，left，right初始化数组的范围
        # left，right并不指向元素的索引，而是表示重复的数字所在的范围
        left, right = 1, len(nums) - 1
        while left <= right:
            # count用来统计小于等于middle的数的个数
            count = 0
            middle = ((right - left) >> 1) + left
            # 统计小于等于middle的元素的个数
            for num in nums:
                if num <= middle: count += 1
            # 如果小于等于middle的数字个数大于middle，说明重复的数字比middle小
            if count > middle: right = middle - 1
            # 如果小于等于middle的数字个数小于middle，说明重复的数字比middle大
            if count <= middle: left = middle + 1
            # 我们不断缩小left，right的区间，直到最后找到重复的数字
        return left

    def findDuplicate2(self, nums: 'List[int]') -> 'int':
        # 方法二把这道题转换成了一个带环的链表，求环的起始位置
        slow, fast = 0, 0
        while True:
            # slow指针每次向后走一步
            slow = nums[slow]
            # fast指针每次向后走两步
            fast = nums[nums[fast]]
            if slow == fast: break
        fast = 0
        # fast和slow一定会在头部相遇
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-07-287-Find-the-Duplicate-Number.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-287-find-the-duplicate-number/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
