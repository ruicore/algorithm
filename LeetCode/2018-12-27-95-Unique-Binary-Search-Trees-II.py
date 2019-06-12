# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-27 11:03:51
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-27 17:00:23

# Definition for a binary tree node.

from pprint import pprint
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 此方法在LeetCode会产生根节点重复引用子树的错误
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.recursion(1, n)

    def recursion(self, left, right):
        # res用于存储构成的所有可能的子树
        res = []
        if left > right:
            return []
        for i in range(left, right+1):
            # 生成所有可能的左子树
            LeftNode = self.recursion(left, i-1)
            # 生成所有可能的右子树
            RightNonde = self.recursion(i+1, right)
            # 如果左右子树都为空，说明当前节点是叶子节点
            if not LeftNode and not RightNonde:
                # 在结果数组中追加叶子节点
                res.append(TreeNode(i))
            # 如果左子树为空右子树不为空
            elif not LeftNode:
                # 遍历遍历产生的所有的可能的右子树
                for item in RightNonde:
                    # 以当前节点作为根节点
                    root = TreeNode(i)
                    root.right = item
                    # 向结果中添加产生的所有子树
                    res.append(root)
                # 如果右子树为空且左子树不为空
            elif not RightNonde:
                # 遍历所有可能的的左子树
                for item in LeftNode:
                    # 以当前节点作为根节点
                    root = TreeNode(i)
                    root.left = item
                    # 向结果中添加产生的所有树
                    res.append(root)
            else:
                # 如果左右子树都不为空，将产生的所有左子树与右子树匹配
                # 遍历所有的左子树
                for i in LeftNode:
                    # 遍历所有的右子树
                    for j in RightNonde:
                        root = TreeNode(i)
                        # 添加左子树
                        root.left = i
                        # 添加右子树
                        root.right = j
                        res.append(root)
        return res


class Solution2(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.recursion(range(1, n+1))

    def recursion(self, nums):
        if len(nums) == 0:
            return [None]
        elif len(nums) == 1:
            return [TreeNode(nums[0])]
        else:
            res = []
            for i in range(0, len(nums)):
                left_trees = self.recursion(nums[:i])
                right_trees = self.recursion(nums[i+1:])
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(nums[i])
                        root.left = left
                        root.right = right
                        res.append(root)
            return res


if __name__ == "__main__":
    so = Solution2()
    res = so.generateTrees(2)
    for item in res:
        print(item)
