# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-28 11:00:13
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-28 11:49:48

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recursion(root, '','')

    def recursion(self, root, maxvalue, minvalue):
        # 如果到达叶节点的子树，返回True
        if not root:
            return True
        if (maxvalue != '' and root.val >= maxvalue) or (minvalue != '' and root.val <= minvalue):
            return False
        # 判断root的左子树，左边的所有节点都必须小于根节点的值
        left = self.recursion(root.left, root.val, minvalue)
        # 判断root的右子树，右边的所有节点都必须大于根节点的值
        right = self.recursion(root.right, maxvalue, root.val)
        return left and right
