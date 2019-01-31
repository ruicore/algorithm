# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-31 11:47:21
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-31 12:39:14


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        # 候选参数1，候选参数2，初始化可以为任意值，只要保证num1 != num2 即可
        num1, num2 = 0, 1
        count1, count2 = 0, 0
        for item in nums:
            # 如果当前元素和第一个元素相等，第一个元素的投票数（权重）加一
            if item == num1:
                count1 += 1
            # 如果当前元素和第二个元素相等，第二个元素的投票数（权重）加一
            elif item == num2:
                count2 += 1
            # 如果第一个元素还没有被投票，将第一个元素置为当前元素
            # 并且将其权重置为1
            elif count1 == 0:
                num1 = item
                count1 = 1
            # 如果第二个元素没有被投票，将第二个元素置为当前元素
            # 并且将其权重置为1
            elif count2 == 0:
                num2 = item
                count2 = 1
            # 否则说明候选元素1和元素2存在且不和当前元素相等，
            # 则元素1和元素2的投票数（权重）减一
            else:
                count1 -= 1
                count2 -= 1
        # 满足条件的元素只可能出现在num1和num2中，我们检查这两个元素是否出现了超过len(nums)//3次
        return [num for num in (num1, num2) if nums.count(num) > len(nums) // 3]
