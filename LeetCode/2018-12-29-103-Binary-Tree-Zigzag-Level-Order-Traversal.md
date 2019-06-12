# LeetCode 103. Binary Tree Zigzag Level Order Traversal

## Description

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

```python
    3
   / \
  9  20
    /  \
   15   7
```

```python
[
  [3],
  [20,9],
  [15,7]
]
```

## 描述

给定二叉树，返回其节点值的Z字形级别遍历。 （即，从左到右，然后从右到左进行下一级别并在之间交替）。

### 思路

* 此题目同上一题[102题](https://leetcode.com/problems/binary-tree-level-order-traversal)思路完全一致，我们只需要加一个判断来确定当前层是否需要反转即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 18:55:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 19:20:04

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 如果子树为空，则直接返回空
        if not root:
            return []
        # 当前遍历层的所有节点，下一层将遍历的所有节点
        currnode, nextnode, res = [root], [], []
        # 数组的起始位置，数组的结束位置，当前层数的所有节点个数
        start, end, count = 0, 0, 1
        # 循环条件，只有当前层还有节点需要遍历才执行
        reverse = False
        while currnode:
            # 索引开始地址，索引结束地址
            start, end = 0, count
            # 当前层所有节点的值，count重置为0
            level, count = [], 0
            for i in range(start, end):
                # 如果当前节点有左节点
                if currnode[i].left:
                    # 左节点将在下一层遍历，放入nextnode数组
                    nextnode.append(currnode[i].left)
                    # 下一层个数自增一次
                    count += 1
                # 如果当前节点有右节点
                if currnode[i].right:
                    # 右节点将在下一层遍历，放入nextnode数组
                    nextnode.append(currnode[i].right)
                    # 下一层个数自增一次
                    count += 1
                # 存储当前节点的值
                level.append(currnode[i].val)
            # 结果数组存储当前层的所有值
            # 如果需要反转，则对结果进行反转
            if reverse:
                level.reverse()
                # 下次不需要反转，重置为False
                reverse = False
            elif not reverse:
                reverse = True
            res.append(level)
            # currnode置为下一层，nextnode重置为空
            currnode, nextnode = nextnode, []
        return res
```

* 以下用python的队列实现了一遍

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 18:55:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 19:20:04

# Definition for a binary tree node.

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 使用队列实现
        if not root:
            return []
        # 是否需要反转，存储结果，队列
        reverse, res, queue = False, [], deque()
        queue.append(root)
        # 循环条件：队列中还有节点
        while queue:
            nums, level = len(queue), []
            # 遍历当前层的所有节点
            for _ in range(0, nums):
                current = queue.popleft()
                # 左子树
                if current.left:
                    queue.append(current.left)
                # 右子树
                if current.right:
                    queue.append(current.right)
                level.append(current.val)
            # 是否需要反转
            if reverse:
                level.reverse()
                reverse = False
            elif not reverse:
                reverse = True
            res.append(level)
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-29-103-Binary-Tree-Zigzag-Level-Order-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-103-binary-tree-zigzag-level-order-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
