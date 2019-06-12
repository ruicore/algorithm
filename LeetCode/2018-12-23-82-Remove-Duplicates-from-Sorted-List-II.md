# LeetCode 82. Remove Duplicates from Sorted List II

## Description

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

## 描述

给定已排序的链接列表，删除所有具有重复数字的节点，只留下原始列表中的不同数字。

### 思路

* 这道题要求删除已排序链表中所有重复的元素.
* 我们用两个指针，pre，point.pre指向第一个元素，point指向第二个元素.
* 当point指向的值和point指向的下一个元素的值相同的时，删除下一个元素，如此重复.最后阐述point本身,point指向下一个元素.
* 有如下特殊情况需要注意:
* 头节点如果重复，头节点是不会在循环中删除的.
* 当链表中只有两个元素且相同时，或者有不止两个元素，前两个元素相同，但与第三个元素不同：此时前两个元素不会被删除，需要另外删除.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-23 17:06:54
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 19:49:13

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        isclear, pre, point = False, head, head.next
        if head.val == head.next.val:
            # 记录头节点是否重复
            isclear = True
        while point and point.next:
            # 用于记录当前值是否需要清除
            if point.val == point.next.val:
                # 清除point后面所有和point相同值的元素
                while point.next and point.val == point.next.val:
                    # 指向需要删除的节点
                    temp = point.next
                    # 删除该节点
                    point.next = temp.next
                    temp.next = None
                # 清除point元素本身
                # pre的nexe指针指向point后面一个元素
                pre.next = point.next
                # point指向下一个元素
                point = point.next
                continue
            point = point.next
            pre = pre.next
        # 如果序列第一个元素和第二个元素相等，去掉这两个元素
        # 在上面的循环中，如果只有两个元素或者第三个元素与第二个元素不等，
        # 都会导致前两个相同的元素不被删除
        if head and head.next and head.val == head.next.val:
            return head.next.next
        # 在上面的循环中，如果第一个出现了重复，且重复次数超过2（即至少前三个元素相同）
        # 会把第一个元素后面重复的元素删除，其本身不会被删除
        elif isclear:
            # 如果进入到了这里，说明头节点重复，头节点后面等于头节点的所有元素已被删除.
            # 但是头节点本身并没有被删除.
            return head.next
        # 其他情况，直接返回head
        else:
            return head


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(1)
    a.next = b
    c = ListNode(2)
    b.next = c
    c.next = None
    so = Solution()
    res = so.deleteDuplicates(a)
    head = res
    while head:
        print(head.val)
        head = head.next
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-23-82-Remove-Duplicates-from-Sorted-List-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-82-remove-duplicates-from-sorted-list-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
