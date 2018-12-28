# LeetCode 98. Validate Binary Search Tree

## Description

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

```python
Input:
    2
   / \
  1   3
Output: true
```

```python

Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
```

## 描述

* 判断给定的一颗二叉树是不是有效的二叉搜索树.

### 思路

* 二叉搜索树要求根节点左边的所有节点小于根节点，根节点右边的所有节点大于根节点（二叉树的形成过程是先查找后插入，如果在二叉树中已经存在相同的值便不会插入，于是二叉树不会出现重复的值）.
* 我们给定一个范围maxvalve，minvalue，二叉树的左右子树都必须在一个这个范围之内.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-28 11:00:13
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-28 11:49:48

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recursion(root, '','')

    def recursion(self, root, maxvalue, minvalue):
        # 如果到达叶节点的子树，返回True
        if not root:
            return True
        if (maxvalue != '' and root.val >= maxvalue) or (minvalue != '' and root.val <= minvalue):
            return False
        # 判断root的左子树，左边的所有节点都必须小于根节点的值
        left = self.recursion(root.left, root.val, minvalue)
        # 判断root的右子树，右边的所有节点都必须大于根节点的值
        right = self.recursion(root.right, maxvalue, root.val)
        return left and right
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-28-98-Validate-Binary-Search-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-98-validate-binary-search-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
