# LeetCode 147. Insertion Sort List

## Description

Sort a linked list using insertion sort.

![Insertion-sort-example-300px](https://wp.me/aaizn9-12q)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

```C
Example 1:
Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

## 描述

对链表进行插入排序。

插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

### 思路

* [插入排序](https://zh.wikipedia.org/zh-hans/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F).
* 维护一个链表，newhead记录已排好序的头节点，tail记录以排序的尾节点。每次从头节点开始查找，找到未排节点应该插入的位置即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-13 14:03:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-13 14:49:30


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 空节点或者只有一个节点直接返回
        if not head or not head.next:
            return head
        # 使用一个辅助节点
        newhead = ListNode(0)
        # 辅助节点指向头节点
        newhead.next = head
        tail, node = head, head.next
        while node:
            compare = newhead
            # 从头开始遍历找到插入的位置，插入排序是稳定的排序算法，如果节点不需要移动则不移动节点
            while compare.next.val <= node.val and compare.next != node:
                compare = compare.next
            # 移动节点
            if compare.next != node:
                tail.next = node.next
                node.next = compare.next
                compare.next = node
            # 如果当前节点不需要移动，则当前节点是尾节点，更新tail=node
            else:
                tail = node
            node = tail.next

        return newhead.next
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-13-147-Insertion-Sort-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-147-insertion-sort-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
