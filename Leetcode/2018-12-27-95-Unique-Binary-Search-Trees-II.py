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
        res = []
        if left > right:
            return []
        for i in range(left, right+1):
            LeftNode = self.recursion(left, i-1)
            RightNonde = self.recursion(i+1, right)
            if not LeftNode and not RightNonde:
                res.append(TreeNode(i))
            elif not LeftNode:
                for item in RightNonde:
                    root = TreeNode(i)
                    root.right = item
                    res.append(root)
            elif not RightNonde:
                for item in LeftNode:
                    root = TreeNode(i)
                    root.left = item
                    res.append(root)
            else:
                for i in LeftNode:
                    for j in RightNonde:
                        root = TreeNode(i)
                        root.left = i
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
    so = Solution()
    res = so.generateTrees(3)
    for item in res:
        print(item)
