# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-27 20:02:19
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-27 20:13:03


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        # 获取左子树的高度
        left = self.depth(root.left)
        # 获取右子树的高度
        right = self.depth(root.right)
        # 如果左右子树的高度相等，则左子树一定是一颗满二叉树
        if left == right:
            return 2**left + self.countNodes(root.right)
        # 如果左右子树高度不相等，则右子树一定是一颗满二叉树
        if left != right:
            return 2**right + self.countNodes(root.left)

    def depth(self, root):
        # 获取完全二叉树的高度
        if not root: return 0
        res = 0
        while root:
            res += 1
            root = root.left
        return res
