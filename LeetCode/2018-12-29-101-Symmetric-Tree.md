# LeetCode 101. Symmetric Tree

## Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

```python
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following [1,2,2,null,3,null,3] is not:

```python
    1
   / \
  2   2
   \   \
   3    3
```

## 描述

* 给定一棵二叉树，判断此二叉树是否左右对称.

### 思路

* 树的题目使用递归求解的情况比较多，也相对比较简单.
* 令给定的树的左子树为p，右子树为p，对称的意思是p的左子树和q的右子树相等，p的右子树和q的左子树相等.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 09:30:27
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 09:42:54

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 如果为空树，返回ture
        if not root:
            return True
        return self.recursion(root.left, root.right)

    def recursion(self, p, q):
        # 如果两个子树都为空，返回True
        if p == None and q == None:
            return True
        # 如果有一个子树为空，另一个子树不为空，返回False
        if (p == None and q != None) or (p != None and q == None):
            return False
        # 能够到达这里，说明两个子树都不为空，如果值不相等，返回False
        if p.val != q.val:
            return False
        # 判断当前子树p的左子树与子树q的右子树是否为镜像子树
        leftree = self.recursion(p.left, q.right)
        # 判断当前子树p的右子树与子树q的左子树是否为镜像子树
        rightree = self.recursion(p.right, q.left)
        return leftree and rightree
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-29-101-Symmetric-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-101-symmetric-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
