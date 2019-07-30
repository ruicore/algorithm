# LeetCode 382. Linked List Random Node

## Description

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

```py
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
```

## 描述

给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

示例:

```py
// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-random-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

### 思路

* 这道题的理论证明参见[维基百科](https://en.wikipedia.org/wiki/Reservoir_sampling)。
* 首先让数字 num 为链表中的头节点的值，count 置为 1；每次往后走一个节点的时候，生成一个 1 到 count 的随机数，如果生成的随机数能够整除 count，就把 num 和当前节点的值替换（条件不已经必须设置为整除 count，设为 0或者其他概率是 1/count 的数都可以），否则不替换；最后返回 num。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-30 07:41:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-30 07:46:44

import random
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        head = self.head
        num = head.val
        node = head.next
        count = 1
        while node:
            count += 1
            if random.randint(1, count) % count == 0:
                num = node.val
            node = node.next

        return num
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-07-30-383-Ransom-Note.py) 。
©本文是原创文章，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-382-linked-list-random-node/) ，作者信息和本声明.
