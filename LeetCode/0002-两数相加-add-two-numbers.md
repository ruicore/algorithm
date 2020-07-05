
### 题目描述

* > 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


* 同时从 l1，l2 中取值，用一个变量 carry 表示进位的情况。
* 只要 l1 不为空，或者 l2 不为空，或者 carry 不等于 0，则需要继续向后做加法。

```py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 两个数相加，需要进位的情况
        carry = 0
        # 声明一个空节点
        root = tmp = ListNode(None)

        # 两个链表中任意一个不为空或者 carry 不为 0
        while l1 or l2 or carry:

            # 取 l1 和 l2 链表中的值
            v1, v2 = 0, 0
            # 取 l1 中的值
            if l1:
                v1 = l1.val
                l1 = l1.next
            # 取 l2 中的值
            if l2:
                v2 = l2.val
                l2 = l2.next

            # 和 10 做除法，如 1，5 = divmod(15,10),则当前的位置值为 5，并进一位
            carry, value = divmod(v1 + v2 + carry, 10)
            # 生成新节点
            tmp.next = ListNode(value)
            # 指向下一个节点
            tmp = tmp.next

        return root.next
```

## 与我联系

* 如果有任何问题，欢迎交流联系

<img src="../wechat.jpeg" width = "220" align=center />