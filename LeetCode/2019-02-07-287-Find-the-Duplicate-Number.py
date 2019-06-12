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
