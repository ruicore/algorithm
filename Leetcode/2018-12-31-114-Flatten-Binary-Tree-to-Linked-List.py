# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 11:24:07
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 11:48:55

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 对左边进行转换
        self.flatten(root.left)
        # 对右边进行转换
        self.flatten(root.right)
        # 如果此时左边已经没有节点，直接返回
        if not root.left:
            return
        else:
            # 首先找到左子树的最右边的节点
            node = root.left
            while node.right:
                node = node.right
            # 将跟节点右子树放到左子树的最右节点
            node.right = root.right
            # 将根节点的左子树放到根节点的右子树
            root.right = root.left
            # 将根节点的左子树置为空
            root.left = None
