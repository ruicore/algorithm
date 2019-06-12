# LeetCode 124. Binary Tree Maximum Path Sum

## Description

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

```python
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

```python
Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

## 描述

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

```python
输入: [1,2,3]

       1
      / \
     2   3

输出: 6
```

示例 2:

```python

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
```

### 思路

* 我们把每一个节点都作为根节点，求其左子树的最大序列，求其右子树的最大序列，选择其最大值与根节点相加，和最大值比较，即可获得最大路径.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-03 09:17:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-03 11:02:07

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = -sys.maxsize

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recursion(root)
        return self.res

    def recursion(self, root):
        # 当走到空节点的时候返回最小值
        if not root:
            return -sys.maxsize
        # 求左子树的最大序列，且仅使用一个孩子节点（最后一层即叶节点）
        left = max(0, self.recursion(root.left))
        # 求右子树的最大序列，且仅使用一个孩子节点（最后一层即也节点）
        right = max(0, self.recursion(root.right))
        # 最终结果是可以取本节点的，于是我们取其中的最大值
        self.res = max(self.res, root.val+left+right)
        # 返回的结果只能取其中一个子树，于是我么取最大值
        return root.val + max(left, right)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-03-124-Binary-Tree-Maximum-Path-Sum.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-124-binary-tree-maximum-path-sum/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
