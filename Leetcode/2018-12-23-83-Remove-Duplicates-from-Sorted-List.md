# LeetCode 83. Remove Duplicates from Sorted List

## Description

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

## 描述

给定已排序的链接列表，删除所有重复项，使每个元素只出现一次。

### 思路

* 此题目思路清晰，很简单.
* 维护一个指针，当当前指针元素的值与当前元素指向下一个元素的值相同时，删除下一个元素.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-23 21:18:30
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 21:19:39

class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            # 如果相等则删除
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                # 否则p指向下一个元素
                p = p.next
        return head
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-23-83-Remove-Duplicates-from-Sorted-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-83-remove-duplicates-from-sorted-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
