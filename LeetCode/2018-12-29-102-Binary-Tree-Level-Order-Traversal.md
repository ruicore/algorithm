# LeetCode 102. Binary Tree Level Order Traversal

## Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

```python
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```python
[
  [3],
  [9,20],
  [15,7]
]
```

## 描述

* 按层遍历给定的二叉树.

### 思路

* 用一个数组currnode存储当前层的所有节点， 另一个数组nextnode存储下一层的所有节点.
* 每次遍历的时候都把下一层将遍历的节点放在nextnode中，遍历完当前层之后，将currnode置为nextnode，nextnode置为空.
* 此题可以考虑用[队列](https://zh.wikipedia.org/wiki/%E9%98%9F%E5%88%97)来减小临时数组的使用.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 14:41:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 15:16:53

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
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
            res.append(level)
            # currnode置为下一层，nextnode重置为空
            currnode, nextnode = nextnode, []
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-29-102-Binary-Tree-Level-Order-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-102-binary-tree-level-order-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
