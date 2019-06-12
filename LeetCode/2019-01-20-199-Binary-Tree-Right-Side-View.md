# LeetCode 199. Binary Tree Right Side View

## Description

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

## 描述

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

### 思路

* 这道题可以使用二叉树的广度优先遍历.
* 我们每一次都遍历二叉树的一行，把最后一个元素的值取出来即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 14:32:25
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 14:34:24

from collections import deque


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            num = len(queue)
            for _ in range(num):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-20-199-Binary-Tree-Right-Side-View.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-199-binary-tree-right-side-view/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
