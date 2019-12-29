# LeetCode 430. Flatten a Multilevel Doubly Linked List

## Description

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

```py
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:
```


After flattening the multilevel linked list it becomes:


Example 2:
```py
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:
```
```py
The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
```
Example 3:

```py
Input: head = []
Output: []
```

How multilevel linked list is represented in test case:

```py
We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
```

### 思路

* 使用循环，从头开始遍历，将子链看成一个整体，将整体向上移动一层。
* 继续向后遍历，如果遇到子链，将其看作一层，将其整体向上移动，如此循环下去，直至结束。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-12-29 10:57:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-12-29 11:05:17


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        current = head
        while current:
            if current.child:
                _next = current.next  # 当前节点的后一个节点
                last = current.child  # 当前节点的自节点
                while last.next:
                    last = last.next  # 如果有子节点，找到子节点的最后一个节点
                current.next = current.child
                current.next.prev = current  # 将自节点向上提高一层
                current.child = None
                last.next = _next
                if _next:
                    _next.prev = last
            current = current.next

        return head
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-12-29-430-Flatten-a-Multilevel-Doubly-Linked-List.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-430-flatten-a-multilevel-doubly-linked-list/) ，作者信息和本声明.
