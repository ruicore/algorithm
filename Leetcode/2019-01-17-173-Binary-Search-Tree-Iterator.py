# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 10:00:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-17 10:38:45


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的中序遍历
# 我们一路将二叉树的左节点压入栈，当弹出栈的时候，我们压入右节点
class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._append(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        res = self.stack.pop()
        self._append(res.right)
        return res.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.stack:
            return True
        return False

    # 辅助函数，压入栈
    def _append(self, root):
        while root:
            self.stack.append(root)
            root = root.left