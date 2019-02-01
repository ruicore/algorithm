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
