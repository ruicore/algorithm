# LeetCode 145. Binary Tree Postorder Traversal

## Description

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

```python
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
```

## 描述

给定一个二叉树，返回它的后序遍历。

示例:

```python
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
```
### 思路

* 使用栈来模拟递归.
* 后序遍历要注意弹出的条件，当一个节点的左右子树为空或者左右子树都已经遍历过了的时候，此节点就应当被弹出.
* 我们用个last表示上一次被弹出的节点，如果last是当前节点node的子节点，说明node的左右子节点都已经遍历完毕(在栈中我们先压入niode节点，再压入node右节点，最后压入左节点，则last如果是node子节点，无论是左节点还是右节点，则node子树都遍历完了).

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-12 19:30:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-12 19:42:54


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        last, res, stack = root, [], [root]
        while stack:
            # top 指向栈顶元素
            top = stack[-1]
            # 栈顶元素弹出的条件是其左右子树同时为空或者其左右子树已经遍历过了
            if (not top.left and not top.right) or (last == top.right or last == top.left):
                top = stack.pop()
                res.append(top.val)
                last = top
            else:
                # 根据栈的特性，先进的元素后出
                if top.right:
                    stack.append(top.right)
                # 后进的元素先出
                if top.left:
                    stack.append(top.left)
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-12-145-Binary-Tree-Postorder-Traversal.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-145-binary-tree-postorder-traversal/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
