# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-28 19:06:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-28 19:12:16

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 如果第一个树和第二个树都是空，说明两个树是相等的，返回True.
        if not p and not q:
            return True
        # 如果有一个数为空另一个树不为空，说明两个树一定不会相等
        if not p or not q:
            return False
        # 如果两个树的节点值不相等，则两条树不会相等，返回False
        if p.val != q.val:
            return False
        # 如果以上条件都通过了，说明两个树的当前节点相等
        # 我们分别判断这两条树的左子树是否相等，右子树是否相等
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        # 返回最终结果
        return left and right