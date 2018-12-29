# LeetCode 104. Maximum Depth of Binary Tree

## Description

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

```python
    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3.

## 描述

* 给定一颗二叉树，返回其最大深度.
* 注意：深度从1开始计数.

### 思路

* 二叉树的题目使用递归求解比较简单.
* 最大深度 = max(左子树的最大深度 + 1，右子树的最大深度 + 1)
* 而左右子树的最大深度与求解当前位置的最大深度相同.

```python

# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 19:41:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 19:53:07

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 树的最大高度为max(左子树最大高度+1，右子树最大高度+1)
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left+1, right+1)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-29-104-Maximum-Depth-of-Binary-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-104-maximum-depth-of-binary-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
