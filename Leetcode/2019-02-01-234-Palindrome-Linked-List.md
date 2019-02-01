# LeetCode 234. Palindrome Linked List

## Description

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

## 描述

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

### 思路

* 我们将链表的前半部分反转，形成两个链表.
* 然后对链表进行比较.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 14:30:29
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 14:43:18


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 如果为空或者只有一个节点，说明是回文链表
        if not head or not head.next: return True
        # 新链表1的头节点，fast指针一次走两步，新链表1的头节点，链表二的头节点
        head1, fast, before, head2 = head, head, head, head.next
        # 我们将链表的前半部分反转
        while fast and fast.next and fast.next.next:
            # fast一次走两步
            fast = fast.next.next
            # 将前面链表的节点指向链表二头节点
            head1 = head2
            # 将链表二头节点往后挪一个
            head2 = head2.next
            # 将当前节点作为链表1的头节点
            head1.next = before
            # befor指向头节点
            before = head1
        # 如果是奇数个节点，原链表的中间节点不需要匹配
        if not fast.next:
            head1 = head1.next
        while head2:
            # 只要有一个节点的值不等就返回False
            if not head1.val == head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        # 如果能够通过上面的判断，返回True
        return True
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-01-234-Palindrome-Linked-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-234-palindrome-linked-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
