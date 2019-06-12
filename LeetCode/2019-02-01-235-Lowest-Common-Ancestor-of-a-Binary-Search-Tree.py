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
