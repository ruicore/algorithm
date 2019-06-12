# LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal

## Description

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

```python
    3
   / \
  9  20
    /  \
   15   7
```

## 描述

给定一颗二叉树的中序和后续遍历，构造原二叉树。

注意：您可以假设树中不存在重复项。

例如，给定

中序遍历 = [9,3,15,20,7]
后序遍历 = [9,15,7,20,3]

返回以下二叉树：

```python
    3
   / \
  9  20
    /  \
   15   7
```

### 思路

* 此题目考察二叉树的构建，类型同第105题完全一致.
* 使用递归求解代码简介，但是速度较慢.

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-30-106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-106-construct-binary-tree-from-inorder-and-postorder-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
