# LeetCode 206. Reverse Linked List

## Description

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## 描述

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

### 实现

* 考察基本的链表操作

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-21 12:02:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 20:17:25


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return None
        new_head = None
        head_next = head.next
        while head and head_next:
            head.next = new_head
            new_head = head
            head = head_next
            head_next = head_next.next
        head.next = new_head
        new_head = head
        return new_head
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-21-206-Reverse-Linked-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-206-reverse-linked-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
