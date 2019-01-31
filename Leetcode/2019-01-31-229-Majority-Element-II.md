# LeetCode 229. Majority Element II

## Description


Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

## 描述

给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

### 思路

* 这道题使用[Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)算法.
* 我们另num1为第一个候选数字，num2为第二个候选数字，count1表示num1获得的投票数，count2表示num2的投票数.
* 基本操作过程如下：1.如果当前数字等于num1，我们让count1加一；2.如果当前数字等于num2，我们让count2加一；3,如果当前元素不等于num1且不等于num2，如果count1为0，我们把当前元素付给num1，并将count1置为1；4.如果当前元素不等于num1且不等于num2，如果count2为0，我们把当前元素付给num2，并将count2置为1 5. 否则（即如果当前元素不等于num1且不等于num2，并且count1和count2）我们将count1和count2自减一次.
* 可能出现了大于len(nums)//3次的元素只可能出现在num1和num2中，我们检查num1是否出现了大于len(nums)//3次，num2是否出现了大于len(nums)//3次.
* 返回出现次数大于len(nums)//3次的元素.

```python
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-31-229-Majority-Element-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-229-majority-element-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
