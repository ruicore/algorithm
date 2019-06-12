# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-31 13:21:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-31 16:54:46


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        current = root
        while current:
            # 如果没有左子树，访问当前节点
            if not current.left:
                count += 1
                # 如果是第k个元素，返回当前元素的值
                if count == k: return current.val
                current = current.right
            else:
                # 指向子节点，一直遍历的左右边的节点
                predecessor = current.left
                while predecessor.right != current and predecessor.right:
                    predecessor = predecessor.right
                # 如果最右边的节点没有被连接，我们连接当前节点
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    # 访问当前节点
                    predecessor.right = None
                    count += 1
                    # 如果当前是第k个元素，我们返回当前节点的值
                    if count == k: return current.val
                    current = current.right
