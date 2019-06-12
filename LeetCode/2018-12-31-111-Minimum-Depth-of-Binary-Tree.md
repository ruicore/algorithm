# LeetCode 111. Minimum Depth of Binary Tree

## Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

```python
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
```

## 描述

* 给定一棵二叉树，返回其最短深度.
* 题目要求是返回一颗二叉树从根节点到到所有叶节点中，深度最小的值.

### 思路

* 我们不断的求当前节点左右子树的高度.
* 如果当前节点为空，我们返回0.
* 要注意的是：如果当前节点没有左子树我们需要返回右子树的高度，因为深度必须到达叶节点.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 09:24:34
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 09:24:34


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.height(root)

    def height(self, root):
        # 到达空节点，返回0
        if not root:
            return 0
        # 当前节点左边的高度
        left = self.height(root.left)
        # 当前节点右边的高度
        right = self.height(root.right)
        # 如果root没有左子树，返回右子树的高度
        if not root.left:
            return right+1
        # 如果没有右子树，返回左子树的高度
        if not root.right:
            return left+1
        else:
            # 返回高度中的最小值
            return min(left, right)+1
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-31-111-Minimum-Depth-of-Binary-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-111-minimum-depth-of-binary-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
