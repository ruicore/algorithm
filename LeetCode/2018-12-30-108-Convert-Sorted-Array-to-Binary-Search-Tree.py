# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 13:18:09
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 13:30:43


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        return self.recursion(0, len(nums)-1, nums)

    def recursion(self, left, right, nums):
        # 递归结束条件，当left大于right时,返回空节点
        if left > right:
            return None
        # 取中间值作为当前根节点
        middle = left+((right-left) >> 1)
        # 声明根节点
        root = TreeNode(nums[middle])
        # 生成左子树
        leftree = self.recursion(left, middle-1, nums)
        # 生成右子树
        rightree = self.recursion(middle+1, right, nums)
        root.left = leftree
        root.right = rightree
        # 返回根节点
        return root
