# LeetCode 94. Binary Tree Inorder Traversal

## Description

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

```python
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]
```

Follow up: Recursive solution is trivial, could you do it iteratively?

## 描述

* 遍历二叉树，使用非递归的形式.

```python
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-26-94-Binary-Tree-Inorder-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-94-binary-tree-inorder-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
