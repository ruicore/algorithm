# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 09:30:27
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 09:42:54

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 如果为空树，返回ture
        if not root:
            return True
        return self.recursion(root.left, root.right)

    def recursion(self, p, q):
        # 如果两个子树都为空，返回True
        if p == None and q == None:
            return True
        # 如果有一个子树为空，另一个子树不为空，返回False
        if (p == None and q != None) or (p != None and q == None):
            return False
        # 能够到达这里，说明两个子树都不为空，如果值不相等，返回False
        if p.val != q.val:
            return False
        # 判断当前子树p的左子树与子树q的右子树是否为镜像子树
        leftree = self.recursion(p.left, q.right)
        # 判断当前子树p的右子树与子树q的左子树是否为镜像子树
        rightree = self.recursion(p.right, q.left)
        return leftree and rightree
