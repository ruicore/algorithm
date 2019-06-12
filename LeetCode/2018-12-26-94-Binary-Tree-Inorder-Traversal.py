# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-26 15:40:49
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-26 21:10:26

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current, stack, res = root, [], []
        if not root:
            return res
        while current or stack:
            # 遍历左边
            while current:
                stack.append(current)
                current = current.left
            # 取中间值
            current = stack.pop()
            res.append(current.val)
            # 遍历右边
            current = current.right
        return res


if __name__ == "__main__":
    root = TreeNode(2)
    so = Solution()
    res = so.inorderTraversal(root)
    print(res)
