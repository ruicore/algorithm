# LeetCode 203. Remove Linked List Elements

## Description

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

## 描述

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

### 实现

* 本题目考察基本的链表操作.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 21:12:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 21:23:10


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 添加一个辅助节点
        node = ListNode(0)
        node.next = head
        res = node
        while node and node.next:
            if node.next.val == val:
                temp = node.next
                node.next = temp.next
                del temp
            else:
                node = node.next
        return res.next
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-20-203-Remove-Linked-List-Elements.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-203-remove-linked-list-elements/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
