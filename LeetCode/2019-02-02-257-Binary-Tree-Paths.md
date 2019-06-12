# LeetCode 257. Binary Tree Paths

## Description

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

```python
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

## 描述

给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

```python
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
```

### 思路

* 使用深度优先遍历

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-02 20:29:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-02 20:46:54


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.__dfs(root, '')
        return self.res

    def __dfs(self, root, _str):
        # 走到None节点直接返回
        if not root:
            return
        # 如果走到叶子节点，我们将最后的结果添加到结果数组中
        if not root.left and not root.right:
            self.res.append(_str + str(root.val))
            return
        # 递归遍历左子树
        self.__dfs(root.left, _str + str(root.val) + "->")
        # 递归遍历右子树
        self.__dfs(root.right, _str + str(root.val) + "->")
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-02-257-Binary-Tree-Paths.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-257-binary-tree-paths/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
