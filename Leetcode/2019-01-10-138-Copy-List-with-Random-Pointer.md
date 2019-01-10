# LeetCode 138. Copy List with Random Pointer

## Description

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

## 描述

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深度拷贝。

### 思路

* 使用一个字典记录新旧节点之间的对应关系.
* 第一步先复制节点，第二步利用字典确定random的值.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-10 10:00:04
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-10 10:24:55

# Definition for singly-linked list with a random pointer.


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # 为空则直接返回
        if not head:
            return None
        # 用一个字典记录对应关系
        copydict, node = {}, head
        # 声明一个辅助头节点
        before = RandomListNode(0)
        while node:
            # 产生新的节点
            newnode = RandomListNode(node.label)
            # 将上一个节点指向当前节点
            before.next = newnode
            # 确定新旧节点之间的对应关系
            copydict[node] = newnode
            before = newnode
            # 指向下一个节点
            node = node.next
        # 为random赋值
        for key, value in copydict.items():
            value.random = copydict.get(key.random, None)
        return copydict[head]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-10-138-Copy-List-with-Random-Pointer.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-138-copy-list-with-random-pointer/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
