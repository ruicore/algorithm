# LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal

## Description

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

```python
    3
   / \
  9  20
    /  \
   15   7
```

## 描述

给定一颗二叉树的前序和中序遍历，构造原二叉树。

注意：您可以假设树中不存在重复项。

例如，给定

前序遍历 = [3,9,20,15,7]
中序遍历 = [9,3,15,20,7]
返回以下二叉树：

```python
    3
   / \
  9  20
    /  \
   15   7
```

### 思路

* 此题目考察二叉树的构建.
* 使用递归求解代码简介，但是速度较慢.

```python
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

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-30-105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-105-construct-binary-tree-from-preorder-and-inorder-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
