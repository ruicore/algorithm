# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 08:29:38
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 09:04:14


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return False if self.height(root) == -1 else True

    def height(self, root):
        # 如果走到了空节点，返回0表示当前高度
        if not root:
            return 0
        # 左子树高度
        left = self.height(root.left)
        # 右子树高度
        right = self.height(root.right)
        # 如果左右子树的高度超过了1，说明以当前root为根节点的树不是平衡二叉树
        # 说明当前这整棵树就不是平衡二叉树
        if abs(left-right) > 1:
            return -1
        # 只要有一棵树不是平衡二叉树，则一直返回-1，当前的树就不是平衡二叉树
        if left == -1 or right == -1:
            return -1
        return max(left, right)+1
