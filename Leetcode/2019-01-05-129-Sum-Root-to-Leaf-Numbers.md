# LeetCode 129. Sum Root to Leaf Numbers

## Description

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

```python
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

Example 2:

```python
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

## 描述

给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

```python
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
```

示例 2:

```python
输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
```

### 思路

* 这道题使用深度优先遍历，我们一路遍历到二叉树的叶节点，将每个值存储到list中，然后把list中的数据组成数字，加和起来.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-05 18:04:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-05 20:36:32

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.res
        self.dfs( [], root)
        return self.res

    def dfs(self,  path, root):
        # 到达叶子节点
        if not root.left and not root.right:
            path.append(str(root.val))
            self.res += int(''.join(path))
            return
        # 左子树
        if root.left:
            self.dfs( path+[str(root.val)], root.left)
        # 右子树
        if root.right:
            self.dfs( path+[str(root.val)], root.right)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-05-129-Sum-Root-to-Leaf-Numbers.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-129-sum-root-to-leaf-numbers/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
