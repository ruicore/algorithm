# LeetCode 107. Binary Tree Level Order Traversal II

## Description

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

```python
    3
   / \
  9  20
    /  \
   15   7
```

return its bottom-up level order traversal as:

```pytohn
[
  [15,7],
  [9,20],
  [3]
]
```

## 描述

给定二叉树，返回其节点值的自下而上级别顺序遍历。 （即，从左到右，逐下而上）。

### 思路

* 此题目同第[102题](https://leetcode.com/problems/binary-tree-level-order-traversal)一样，都是要求按层遍历，第102题是从上往下，这一题要求从下往上.
* 因此，我们仍然按层从上往下遍历，最后在把结果反转一次即可.
* 我们使用队列，把下一层即将遍历的节点存储在队尾，这一层遍历的节点在队首，我们从队首取当前层的元素，直到当前层取完，我们进行下一层的遍历.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 12:13:55
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 12:33:53


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, queue, line = [], deque(), 0
        queue.append(root)
        while queue:
            line += 1
            # 当前层的节点个数
            count = len(queue)
            temp = []
            for _ in range(count):
                # 从左往右取当前层的节点
                top = queue.popleft()
                # 添加当前层节点的值
                temp.append(top.val)
                # 把当前层当前节点的左节点添加到队尾
                if top.left:
                    queue.append(top.left)
                # 把当前层当前节点的右节点添加到队尾
                if top.right:
                    queue.append(top.right)
            res.append(temp)
        # 最后倒转原来的顺序即可
        return [res.pop() for _ in range(line)]
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-30-107-Binary-Tree-Level-Order-Traversal-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-107-binary-tree-level-order-traversal-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
