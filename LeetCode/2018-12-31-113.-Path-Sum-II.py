# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 11:00:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 11:12:15

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.recursion(root, [], res, sum)
        return res

    def recursion(self, root, path, res, target): 
        # 如果为空，则直接返回
        if not root:
            return
        # 到达叶节点，进行判断
        if not root.left and not root.right:
            path.append(root.val)
            if sum(path) == target:
                res.append(path)
            return
        # 检查左子树
        self.recursion(root.left, path+[root.val], res, target)
        # 检查右子树
        self.recursion(root.right, path+[root.val], res, target)
