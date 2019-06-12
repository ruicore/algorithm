# LeetCode 160. Intersection of Two Linked Lists

## Description

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

![160_statement](https://wp.me/aaizn9-135)

begin to intersect at node c1.

Example 1:

![160_example_1](https://wp.me/aaizn9-136)

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

![160_example_2](https://wp.me/aaizn9-137)

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

![160_example_3](https://wp.me/aaizn9-138)

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

## 描述

编写一个程序，找到两个单链表相交的起始节点。

### 思路

* 这道题有两种不同的写法，其基本思路是一致的.
* 在上面的示例中，相交的节点我们称之为c，如果c点前面A，B链表的节点个数是相同的，那么我们从A，B的起点同时往后走，就一定会相遇.
* 于是我们就要想办法把相交的节点前面节点数目变得一样.
* 方法一，我们分别获取链表A和链表B的长度lena和lenb，我们让其中较长的链表先走lena-lanb步(A比B长，如果B更长就是lenb-lena步)，然后让两个链表同时往后面走.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 09:55:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 10:10:29

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        # 获取链表的长度
        lena, lenb = self._lenList(headA), self._lenList(headB)
        a, b = headA, headB
        # 移动起始位置到节点个数相同的第一个点
        if lena > lenb:
            for _ in range(lena - lenb):
                a = a.next
        elif lenb > lena:
            for _ in range(lenb - lena):
                b = b.next
        # 同时往后面走
        while a != b:
            a, b = a.next, b.next
        return a

    # 辅助函数，获取链表的长度
    def _lenList(self, Node):
        res = 0
        while Node:
            res += 1
            Node = Node.next
        return res
```
* 方法二，为了获得相同个数的链表个数的效果，我们可以把链表A添加到链表B上，把链表B添加到链表B上.
* 体现的形式是先从链表A出发的节点如果走完了链表A，就接着链表B开始走，反过来先从链表B出发的链表也一样.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-16 09:55:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-16 10:10:29

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a, b = headA, headB
        # 另一种写法，为了达到从相同个数启起点，我们把a链表添加到b链表前面
        # 把b链表添加到a链表前面
        while a != b:
            if not a:
                a = headB
            elif not b:
                b = headA
            else:
                a, b = a.next, b.next
        return a
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-16-160-Intersection-of-Two-Linked-Lists.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-160-intersection-of-two-linked-lists/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
