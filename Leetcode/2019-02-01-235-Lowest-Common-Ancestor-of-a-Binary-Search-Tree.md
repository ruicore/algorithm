# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree

## Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

## 描述

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

### 思路

* 根据二叉搜索树的性质， lowest common ancestor 节点的值一定在p和q之间.
* 如果当前节点的值大于p和q节点的值，说明LCA在当前节点左边.
* 如果当前节点的值小于p和q节点的值，说明LCA在当前节点右边.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-01 18:26:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-01 18:44:19


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
        # 根据二叉搜索树的性质， lowest common ancestor 节点的值一定在p和q之间
        # 如果当前节点的值大于p和q节点的值，说明LCA在当前节点左边
        # 如果当前节点的值小于p和q节点的值，说明LCA在当前节点右边

        if p.val < q.val:
            return self._recursion(root, p, q)
        else:
            return self._recursion(root, q, p)

    def _recursion(self, root, p, q):
        # p节点的值一定小于q节点的值
        if p.val <= root.val <= q.val: return root
        if root.val < p.val and root.val < q.val:
            return self._recursion(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self._recursion(root.left, p, q)

```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-01-235-Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-235-lowest-common-ancestor-of-a-binary-search-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
