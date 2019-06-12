# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-28 20:30:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-28 20:39:41


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 如果为空，直接返回
        if root: return
        # 转换左子树
        left = self.invertTree(root.left)
        # 转换右子树
        right = self.invertTree(root.right)
        # 交换左右子树
        root.left, root.right = right, left
        return root
