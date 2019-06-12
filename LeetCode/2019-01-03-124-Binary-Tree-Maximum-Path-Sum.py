# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-03 09:17:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-03 11:02:07

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = -sys.maxsize

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recursion(root)
        return self.res

    def recursion(self, root):
        # 当走到空节点的时候返回最小值
        if not root:
            return -sys.maxsize
        # 求左子树的最大序列，且仅使用一个孩子节点（最后一层即叶节点）
        left = max(0, self.recursion(root.left))
        # 求右子树的最大序列，且仅使用一个孩子节点（最后一层即也节点）
        right = max(0, self.recursion(root.right))
        # 最终结果是可以取本节点的，于是我们取其中的最大值
        self.res = max(self.res, root.val+left+right)
        # 返回的结果只能取其中一个子树，于是我么取最大值
        return root.val + max(left, right)
