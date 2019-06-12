# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 09:55:46
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 09:55:46

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        return self.recursion(preorder, inorder)

    def recursion(self, preorder, inorder):
        if not preorder:
            return None
        elif len(preorder) == 1 and len(inorder) == 1:
            root = TreeNode(inorder[0])
            root.left = None
            root.right = None
        else:
            value = preorder[0]
            root = TreeNode(value)
            ino = inorder.index(value)
            left = self.recursion(preorder[1:ino+1], inorder[0:ino])
            right = self.recursion(preorder[ino+1:], inorder[ino+1:])
            root.left = left
            root.right = right
        return root


if __name__ == "__main__":
    so = Solution()
    preorder, inorder = [1, 2,4,5,3,6,7], [4,2,5, 1,6,3,7]
    res = so.buildTree(preorder, inorder)
    nums, root = [], res
    while root:
        if root.left:
            temp = root.left
            while temp.right and temp.right != root:
                temp = temp.right
            if not temp.right:
                temp.right = root
                root = root.left
            if temp.right == root:
                nums.append(root.val)
                temp.right = None
                root = root.right
        else:
            nums.append(root.val)
            root = root.right
    print(nums, inorder)
