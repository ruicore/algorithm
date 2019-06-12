# LeetCode 142. Linked List Cycle II

## Description

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

![circularlinkedlist](https://wp.me/aaizn9-120)

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

![circularlinkedlist_test2](https://wp.me/aaizn9-121)

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

![circularlinkedlist_test3](https://wp.me/aaizn9-122)

Follow up:
Can you solve it without using extra space?

## 描述

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？

### 思路

* 借助上一题的思路，我们使用两个指针，分别是slow和fast，slow指针每次向后走一个，fast指针每次向后走两步.
* 此题目借鉴了求链表中倒数第k个节点的思想.
* 基本思路是先求得环中一共有多少个节点m.
* 然后slow，fast重置为head,将fast往后移动m-个节点，然后slow和fast同时往后移动，当fast.next == slow时返回slow即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 10:09:56
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 12:05:39

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        count = 1
        slow, fast = head, head.next
        while fast and fast.next:
            # 找到第一次相遇的节点
            if fast == slow:
                # 确定环中节点的个数
                fast = fast.next
                while fast and fast.next:
                    # 如果fast指针和slow指针相遇，说明环已经走完一趟
                    # 结束循环
                    if fast == slow:
                        break
                    # 否则count自增一次
                    count += 1
                    slow, fast = slow.next, fast.next.next
                # 重置slow和fast只想首节点
                slow, fast = head, head
                # 将fast往后移count-1个（即环中节点个数少一个节点）
                for _ in range(count - 1):
                    fast = fast.next
                while fast:
                    # 当fast.next 指向slow时，说明已经到达结尾
                    if fast.next == slow:
                        return slow
                    fast = fast.next
                    slow = slow.next
                return slow
            slow, fast = slow.next, fast.next.next
        # 如果遍历的所有节点fast和slow都不等，说明没有环
        return None
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-12-142-Linked-List-Cycle-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-142-linked-list-cycle-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
