# LeetCode 239. Sliding Window Maximum

## Description

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

```python
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

## 描述

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

```python
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### 思路

* 这道题方法不唯一，我们这里借助单调非递增双端队列来实现.
* 队列按非递增排列，最大值在队首，每次插入值num的时候，我们从后面开始检查，把所有比num小的值从队列尾部删除，把num插入到队尾.
* 每次取值的时候，取出队首位置的值即可,如果队首的值等于当前位置前面k-1个位置的值，说明队首元素在下一次元素入队的时候将超出窗格的容纳范围，我们弹出队首元素.

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-02-239-Sliding-Window-Maximum.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-239-sliding-window-maximum/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
