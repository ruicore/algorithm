# LeetCode 404. Sum of Left Leaves

## Description

Find the sum of all left leaves in a given binary tree.

Example:

```py
    3
   / \
  9  20
    /  \
   15   7
```

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

## 描述

计算给定二叉树的所有左叶子之和。

示例：

```py
    3
   / \
  9  20
    /  \
   15   7
```

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

### 思路

* 使用任意一种方式遍历二叉树，找到左叶子结点的时候，将其值进行加和即可。
* 判断是否为左叶子节点的方法是：判断节点有左节点，并且左节点的左右节点为空；

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-14 08:23:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-14 08:33:06

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.__traversal(root)
        return self.res

    def __traversal(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val
        self.__traversal(root.left)
        self.__traversal(root.right)
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-09-14-404-Sum-of-Left-Leaves.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-404-sum-of-left-leaves/) ，作者信息和本声明.
