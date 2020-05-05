# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2020-05-01 17:30:03
# @Last Modified by:   何睿
# @Last Modified time: 2020-05-01 19:54:16

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.sumRoot(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def sumRoot(self, root, pre, sum_):

        if not root:
            return 0
        pre += root.val

        left = self.sumRoot(root.left, pre, sum_)
        right = self.sumRoot(root.right, pre, sum_)

        return (pre == sum_) + left + right
