# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-05 18:04:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-05 20:36:32

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.res
        self.dfs( [], root)
        return self.res

    def dfs(self,  path, root):
        # 到达叶子节点
        if not root.left and not root.right:
            path.append(str(root.val))
            self.res += int(''.join(path))
            return
        # 左子树
        if root.left:
            self.dfs( path+[str(root.val)], root.left)
        # 右子树
        if root.right:
            self.dfs( path+[str(root.val)], root.right)