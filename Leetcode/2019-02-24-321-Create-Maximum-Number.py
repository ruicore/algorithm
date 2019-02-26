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