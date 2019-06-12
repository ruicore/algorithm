# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 11:21:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 11:21:05

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        return self.recursion(inorder, postorder)

    def recursion(self, inorder, postorder):
        #
        if not inorder:
            return None
        elif len(inorder) == 1 and len(postorder) == 1:
            root = TreeNode(inorder[0])
            root.left = None
            root.right = None
        else:
            value = postorder[-1]
            root = TreeNode(value)
            ino = inorder.index(value)
            left = self.recursion(inorder[0:ino], postorder[0:ino])
            right = self.recursion(inorder[ino+1:], postorder[ino:-1])
            root.left = left
            root.right = right
        return root


if __name__ == "__main__":
    so = Solution()
    postorder , inorder = [9,15,7,20,3], [9,3,15,20,7]
    res = so.buildTree(inorder, postorder)
    nums, root = [], res
    # 二叉树的中序遍历morris方法
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
