# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 09:56:05
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 12:40:56

from collections import deque

# 实现一个单调非递增队列，继承于deque
class MonotonicQueue(deque):
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        # 注意这里不能取等号
        while self.queue and num > self.queue[-1]:
            self.queue.pop()
        self.queue.append(num)
        return True


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 如果nums为空或者k小于等于0，返回空
        if not nums or k <= 0: return []
        res = []
        mq = MonotonicQueue()
        # 先将前面的k-1个数字放入到队列中
        for i in range(0, k - 1):
            mq.push(nums[i])
        for i in range(k - 1, len(nums)):
            mq.push(nums[i])
            # 队首为最大元素
            res.append(mq.queue[0])
            # 如果窗格的最左边元素等于最大元素，说明最大元素在下一次循环中将超出
            # 窗格的范围，于是我们弹出这个值
            if nums[i - k + 1] == mq.queue[0]: mq.queue.popleft()
        return res
