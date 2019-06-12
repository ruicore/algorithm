# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 19:41:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 19:53:07

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 树的最大高度为max(左子树最大高度+1，右子树最大高度+1)
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left+1, right+1)
