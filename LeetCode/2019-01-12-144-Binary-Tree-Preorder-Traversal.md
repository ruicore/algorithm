# LeetCode 144. Binary Tree Preorder Traversal

## Description

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

```python
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
```

## 描述

给定一个二叉树，返回它的 前序 遍历。

示例:

```python
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
```
### 思路

* 我们用栈来模拟递归.
* 根据栈后进先出的特点，先将right子节点压入栈，后将左边节点压入栈.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 18:59:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 19:18:42


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 如果为空则返回一个空的数组
        if not root:
            return
        stack, res = [root], []
        while stack:
            # 先取根节点
            top = stack.pop()
            res.append(top.val)
            # 根据栈后进先出的特点，先将right指针压入栈，则right值后出来
            if top.right:
                stack.append(top.right)
            # 后入栈则先出
            if top.left:
                stack.append(top.left)
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-12-144-Binary-Tree-Preorder-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-144-binary-tree-preorder-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
