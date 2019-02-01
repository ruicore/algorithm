# LeetCode 237. Delete Node in a Linked List

## Description

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

## 描述

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 
说明:

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

### 思路

* 把要删除的节点的值放到最后一个节点，删除嘴后一个节点.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 20:42:50
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 21:12:10


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 记录最后一个节点前面一个节点
        pretail = node
        # 把要删除节点的值放到最后一节点
        while node.next:
            pretail = node
            node.val, node.next.val = node.next.val, node.val
            node = node.next
        # 删除嘴后一个节点
        temp = pretail.next
        del temp
        # 最后一个节点的前一个节点next指针置为None
        pretail.next = None
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-01-237-Delete-Node-in-a-Linked-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-237-delete-node-in-a-linked-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
