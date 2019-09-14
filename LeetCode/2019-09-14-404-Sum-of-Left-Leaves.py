# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-14 08:23:43
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-14 08:33:06

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.__traversal(root)
        return self.res

    def __traversal(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val
        self.__traversal(root.left)
        self.__traversal(root.right)
