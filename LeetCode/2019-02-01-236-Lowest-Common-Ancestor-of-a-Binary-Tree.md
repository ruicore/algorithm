# LeetCode 236. Lowest Common Ancestor of a Binary Tree

## Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

![binarytree](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

## 描述

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

### 思路

* 从根节点开始搜索，如果遇到了一个节点的值在p或q中，返回当前节点的索引到其parent,如果当前节点的值不在p或q中，我们递归的遍历当前节点的左右子树.
* 如果左子树返回不为空，右子树返回不为空，说明p，q在左右子树中（可以p在左子树，q在右子树；也可能p在右子树，q在左子树）说明当前节点就是ACL，我们返回当前节点.
* 如果左子树返回不为空，右子树返回空，说明p，q中有一个节点在左子树中，我们返回左子树返回的节点.
* 如果左子树返回空，右子树返回不为空，说明p，q中有一个节点在右子树中，我们返回右子树返回的节点.
* 如果左子树返回空，并且右子返回空，说明p没有在左右子树中，q没有在左右子树中，我们返回None.
* 详细请参考这个[视频](https://www.youtube.com/watch?v=13m9ZCB8gjw)

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 18:56:46
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 20:20:55


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 如果为空返回None
        if not root: return None
        # 如果当前节点等于p.val 或 q.val 返回当前节点索引
        if root.val == p.val or root.val == q.val: return root
        # 递归遍历左子树
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归遍历右子树
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左右都不为空，说明当前节点符合条件
        if left and right: return root
        # 如果左边不为空右边为空
        if left and not right: return left
        # 如果左边为空右边不为空
        if not left and right: return right
        # 如果左右都为空
        if not left and not right: return None
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-01-236-Lowest-Common-Ancestor-of-a-Binary-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-236-lowest-common-ancestor-of-a-binary-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
