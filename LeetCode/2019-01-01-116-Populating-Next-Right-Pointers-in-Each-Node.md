# LeetCode 116. Populating Next Right Pointers in Each Node

## Description

Given a binary tree

```c
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

```python
     1
   /  \
  2    3
 / \  / \
4  5  6  7
```

After calling your function, the tree should look like:

```python
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
```

## 描述

给定一颗二叉树，填充每一个节点的next指针使其指向右侧节点。 如果没有下一个右侧节点，则下一个指针应设置为NULL。

### 思路

* 这道题同按层遍历二叉树非常类似，但是使用了队列，不符合题中空间复杂度O(1)的要求.
* 下面使用了队列.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 09:47:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 10:02:57

# Definition for binary tree with next pointer.

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


from collections import deque


class Solution:
    # @param root, a tree link node
    # @return nothing
    # ！！！此方法申请了额外的空间
    def connect(self, root):
        if not root:
            return
        # 声明一个队列
        queue = deque()
        # 将根节点放入队首
        queue.append(root)
        while queue:
            # 取出队首节点
            first = queue.popleft()
            # 获取当前层剩余的个数
            nums = len(queue)
            # 如果当前节点左子节点不为空
            if first.left:
                # 将当前节点的左子节点放入队尾
                queue.append(first.left)
            # 如果当前节点的右子节点不为空
            if first.right:
                # 将当前节点的右子节点放入队尾
                queue.append(first.right)
            # 遍历当前层的剩余节点
            for _ in range(nums):
                sec = queue.popleft()
                if sec.left:
                    queue.append(sec.left)
                if sec.right:
                    queue.append(sec.right)
                first.next = sec
                first = sec
            # 将最后一个节点置为None
            first.next = None
```

* 我们可以使用三个指针来达到空间复杂度O(1)的情况，我们使用head记录已经将每一个节点连接起来的一层，childhead记录正在操作层的头指针，child用于遍历当前正在操作的指针.
* 如果childhead为空，我们初始化childhead，child指向head的第一个子节点.
* 如果childhead已经被赋值，我们保持它不变，让child指向head第一个还没有被指向的节点.
* 当head的左右字节点处理完成之后，我们令head=head.next.

```python

class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        head = root
        child, chidhead = None, None
        # head在这里控制垂直的循环，即控制从上到下二叉树的所有层
        while head:
            # head在这里控制一层的每一个节点
            while head:
                # 如果head有左节点
                if head.left:
                    # 如果head下一层的首节点已经被设置好了
                    if chidhead:
                        # 将child.next指针指向head.left节点
                        child.next = head.left
                        # child指针向后走一步
                        child = head.left
                    else:
                        # 否则我们初始化childhead指向head下面一层的首节点
                        chidhead = head.left
                        # 初始化child指向首节点
                        child = head.left
                # 如果head有右节点
                if head.right:
                    # 同理如果head下一层的首部节点已经设置
                    if chidhead:
                        # child的next指针指向右节点
                        child.next = head.right
                    else:
                        # 同理如果childhead没有设置，我们初始化childHead
                        chidhead = head.right
                    # 如上 child = head.right可以单独从两个判断种提出来，因为两种情况都需要执行
                    child = head.right
                # head指针向后走一步
                head = head.next
            # 更新head指向下一层
            head = chidhead
            # 重置指向下一层的指针
            chidhead, child = None, None
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-01-116-Populating-Next-Right-Pointers-in-Each-Node.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-116-populating-next-right-pointers-in-each-node/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
