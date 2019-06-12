# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 09:24:34
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 09:24:34


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.height(root)

    def height(self, root):
        # 到达空节点，返回0
        if not root:
            return 0
        # 当前节点左边的高度
        left = self.height(root.left)
        # 当前节点右边的高度
        right = self.height(root.right)
        # 如果root没有左子树，返回右子树的高度
        if not root.left:
            return right+1
        # 如果没有右子树，返回左子树的高度
        if not root.right:
            return left+1
        else:
            # 返回高度中的最小值
            return min(left, right)+1
