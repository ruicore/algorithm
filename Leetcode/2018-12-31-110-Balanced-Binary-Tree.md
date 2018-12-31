# LeetCode 110. Balanced Binary Tree

## Description

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

```python
    3
   / \
  9  20
    /  \
   15   7
```

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

```python
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

Return false.

## 描述

* 给定一颗二叉树，判断此树是不是平衡二叉树.
* 平衡二叉树的条件是：当前节点的左右子树高度差不超过1，且左右子树都是平衡二叉树.

### 思路

* 我们递归的不断求解当前节点左右子树的高度，我们用-1来表示以当前节点为根节点的树不是平衡二叉树.
* 如果当前子树的左右节点高度差超过1，我们返回-1表示当前求解的树不是平衡二叉树.
* 只要我们返回的左右子树的高度中有-1，我们就一直返回-1.
* 最后在主调函数中我们检查返回值是否为-1，若是说明此树不是平衡二叉树.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 08:29:38
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 09:04:14


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return False if self.height(root) == -1 else True

    def height(self, root):
        # 如果走到了空节点，返回0表示当前高度
        if not root:
            return 0
        # 左子树高度
        left = self.height(root.left)
        # 右子树高度
        right = self.height(root.right)
        # 如果左右子树的高度超过了1，说明以当前root为根节点的树不是平衡二叉树
        # 说明当前这整棵树就不是平衡二叉树
        if abs(left-right) > 1:
            return -1
        # 只要有一棵树不是平衡二叉树，则一直返回-1，当前的树就不是平衡二叉树
        if left == -1 or right == -1:
            return -1
        return max(left, right)+1
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-31-110-Balanced-Binary-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-110-balanced-binary-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
