# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 09:48:06
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 10:48:32


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.recursion(root, 0, sum)

    def recursion(self, root, _sum, target):
        # 如果为空
        if not root:
            # 如果总和与目标值相等，返回True
            if _sum == target:
                return True
            # 否则返回False
            else:
                return False
        _sum += root.val
        # 计算左子树
        left = self.recursion(root.left, _sum, target)
        # 计算右子树
        right = self.recursion(root.right, _sum, target)
        # 在没有左子树的情况下，才返回右子树的值
        if not root.left:
            return right
        # 在没有右子树的情况下，才返回左子树的值
        if not root.right:
            return left
        else:
            # 任意一个满足条件就行
            return left or right
