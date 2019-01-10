# LeetCode 141. Linked List Cycle

## Description

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

## 描述

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

### 思路

* 我们使用两个指针，slow和fast，slow指针每次向后走一步，fast指针每次向后走两步，如果有环，slow和fast则一定会相遇，如果fast走到了末尾都没有相遇，说明没有环.
* slow初始为head，fast初始化为head.next.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-10 18:12:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-10 18:16:58


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype
        """
        # 如果没有节点或者只有一个节点，返回False
        if head == None or head.next == None:
            return False
        # 声明两个指针，slow指针每次走一步，fast指针每次走两步
        slow, fast = head, head.next
        while slow != fast:
            # 如果走到了末尾，返回False
            if fast == None or fast.next == None:
                return False
            # slow向后走一步
            slow = slow.next
            # fast向后走两步
            fast = fast.next.next

        return True
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-10-141-Linked-List-Cycle.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-141-linked-list-cycle/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
