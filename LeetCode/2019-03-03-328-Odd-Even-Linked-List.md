# LeetCode 328. Odd Even Linked List

## Description

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

```py
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

Example 2:

```py
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

## 描述

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

```py
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
```

示例 2:

```py
输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL

```
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

### 思路

* 我们声明两个链表，一个叫做「奇数链表」，另一个叫做「偶数链表」，奇数链表只存储奇数的节点，偶数链表只存储偶数的节点。
* 我们依次从给定的节点中取出节点，依次添加到「奇数链表」和「偶数链表」中，最后我们将「偶数链表」添加到「奇数链表」末尾。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-03 15:03:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-03 15:59:29


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 少于两个节点的情况直接返回
        if not head or not head.next: return head
        # 记录下头节点
        oddhead, evenhead = head, head.next
        # 记录下尾节点，初始是头节点和尾节点是重合的
        oddtail, eventail = head, head.next
        node = head.next.next
        oddtail.next, eventail.next = None, None
        isodd = True
        while node:
            # 把当前节点挂到奇数链表后面
            if isodd:
                # 挂载当前节点
                oddtail.next = node
                # 剩余节点指针向后移动一个
                node = node.next
                # 尾节点向后移动一个
                oddtail = oddtail.next
                # 将尾节点的下一个节点置为空
                oddtail.next = None
                # 下一次将挂载到奇数节点后面
                isodd = False
            # 把当前节点挂到偶数节点后面
            else:
                # 挂载当前节点
                eventail.next = node
                # 剩余节点向后移动一个
                node = node.next
                # 尾节点向后移动一个
                eventail = eventail.next
                # 将尾节点的下一个节点置为空
                eventail.next = None
                # 下一次将挂载到偶数节点后面
                isodd = True
        # 偶数链将挂载到奇数链表后面
        oddtail.next = evenhead
        # 返回奇数链表的头节点
        return oddhead
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-03-328-Odd-Even-Linked-List.py) 。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-328-odd-even-linked-list/) ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-328-odd-even-linked-list/) ，作者信息和本声明.
微信公众号：techruicore 
