# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 20:29:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 20:46:54


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.__dfs(root, '')
        return self.res

    def __dfs(self, root, _str):
        # 走到None节点直接返回
        if not root:
            return
        # 如果走到叶子节点，我们将最后的结果添加到结果数组中
        if not root.left and not root.right:
            self.res.append(_str + str(root.val))
            return
        # 递归遍历左子树
        self.__dfs(root.left, _str + str(root.val) + "->")
        # 递归遍历右子树
        self.__dfs(root.right, _str + str(root.val) + "->")
