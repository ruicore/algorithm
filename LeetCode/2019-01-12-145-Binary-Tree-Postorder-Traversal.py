# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 19:30:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 19:42:54


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        last, res, stack = root, [], [root]
        while stack:
            # top 指向栈顶元素
            top = stack[-1]
            # 栈顶元素弹出的条件是其左右子树同时为空或者其左右子树已经遍历过了
            if (not top.left and not top.right) or (last == top.right or last == top.left):
                top = stack.pop()
                res.append(top.val)
                last = top
            else:
                # 根据栈的特性，先进的元素后出
                if top.right:
                    stack.append(top.right)
                # 后进的元素先出
                if top.left:
                    stack.append(top.left)
        return res
