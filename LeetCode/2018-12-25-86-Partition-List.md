# LeetCode 86. Partition List

## Description

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

## 描述

给定链表和值x，对其进行分区，使得小于x的所有节点都在大于或等于x的节点之前.

您应该保留两个分区中每个分区中节点的原始相对顺序.

### 思路

* 这道题是快速排序分区部分的实现,要求给定一个链表和一个枢纽，对链表中的所有元素排序使得枢纽左边的元素小于枢纽，枢纽右边的元素大于等于枢纽.
* 我们把链表左边的区域看成是已排序区域，遍历右边未排序的区域，遇到了雄安与枢纽的元素就将它放到已排序区域的末尾即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-25 09:44:39
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-25 11:27:30

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 此题目是快速排序分区部分的实现，即给定一个枢纽，将数组（链表）分成左右
        # 两个部分，使得左边部分小于枢纽，右边部分大于等于枢纽
        # 数据结构为为指针的形式
        # 我们声明一个辅助的头节点
        pre = ListNode(-1)
        # 让辅助的头节点指向head头节点
        # point指向需要判断的节点，pre指向point前面一个节点
        pre.next, point = head, head
        # res用于存储结果，inplace表示已到达最终位置节点的最后一个节点
        res, inplace = pre, pre
        # 当point不为空，继续执行
        while point:
            # 如果当前位置小于枢纽，且当前位置是已经到达最终位置的节点
            # 继续执行
            if point.val < x and inplace == point or point.val >= x:
                point = point.next
                pre = pre.next
            # 如果当前位置小于枢纽，且没有到达最终位置
            else:
                # temp指向需要交换位置的节点
                temp = point
                # pre指向需要被交换节点的后面一个节点
                pre.next = temp.next
                # 被交换的节点next指针指向已经到达最终位置节点的后面一个节点
                temp.next = inplace.next
                # 已经到达最终位置的最后一节点指向被交换的节点
                inplace.next = temp
                # 记录已经到达最终位置节点的值向后挪一位
                inplace = temp
                point = pre.next

        return res.next
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-25-86-Partition-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-86-partition-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
