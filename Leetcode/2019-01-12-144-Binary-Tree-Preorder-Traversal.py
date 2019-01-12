# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 18:59:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 19:18:42


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 如果为空则返回一个空的数组
        if not root:
            return
        stack, res = [root], []
        while stack:
            # 先取根节点
            top = stack.pop()
            res.append(top.val)
            # 根据栈后进先出的特点，先将right指针压入栈，则right值后出来
            if top.right:
                stack.append(top.right)
            # 后入栈则先出
            if top.left:
                stack.append(top.left)