# LeetCode 92. Reverse Linked List II

## Description

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

```python
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

## 描述

* 给定一个链表，反转指定的子序列.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-26 11:44:18
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-26 13:36:47


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 需要交换的次数
        move, reverse = m-1, n-m
        # pre初始化指向第一个被换节点的前一个节点，point初始化为第一个被换节点
        # 声明一个辅助头节点
        res = ListNode(0)
        pre, point = res, head
        pre.next = head
        # 把pre，point放到指定位置
        while move > 0:
            pre = pre.next
            point = point.next
            move -= 1
        # 需要交换的次数
        while reverse:
            temp = point.next
            point.next = temp.next
            temp.next = pre.next
            pre.next = temp
            reverse -= 1
        return res.next
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-26-92-Reverse-Linked-List-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-92-reverse-linked-list-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
