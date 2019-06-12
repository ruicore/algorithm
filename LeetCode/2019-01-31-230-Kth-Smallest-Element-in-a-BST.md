# LeetCode 230. Kth Smallest Element in a BST

## Description

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

```python
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
```
Output: 1

```python
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

## 描述

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

```python
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
```

```python
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
```

### 思路
* 使用二叉树的中序遍历，当遍历到第k个节点的时候，我们结束循环返回当前节点的值.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-31 13:21:22
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-31 16:54:46


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        current = root
        while current:
            # 如果没有左子树，访问当前节点
            if not current.left:
                count += 1
                # 如果是第k个元素，返回当前元素的值
                if count == k: return current.val
                current = current.right
            else:
                # 指向子节点，一直遍历的左右边的节点
                predecessor = current.left
                while predecessor.right != current and predecessor.right:
                    predecessor = predecessor.right
                # 如果最右边的节点没有被连接，我们连接当前节点
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    # 访问当前节点
                    predecessor.right = None
                    count += 1
                    # 如果当前是第k个元素，我们返回当前节点的值
                    if count == k: return current.val
                    current = current.right
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-31-230-Kth-Smallest-Element-in-a-BST.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-230-kth-smallest-element-in-a-bst/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
