# LeetCode 108. Convert Sorted Array to Binary Search Tree

## Description

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

```python
      0
     / \
   -3   9
   /   /
 -10  5
```

## 描述

给定一个数组，其中元素按升序排序，将其转换为高度平衡的BST。

对于这个问题，高度平衡的二叉树被定义为:二叉树中每个节点的两个子树的深度从不相差超过1。

例：

给定排序数组：[ -  10，-3,0,5,9]，

一个可能的答案是：[0，-3,9，-10，null，5]，它代表以下高度平衡的BST：

```python
      0
     / \
   -3   9
   /   /
 -10  5
```

## 思路

* 二叉树的题目使用递归求解比较简单.
* 为了构造一棵平衡二叉树，我们每次都从给定数组的中间取值作为根节点，然后以当前值左边的所有值作为当前节点的左子树.
* 当前值右边的所有节点作为当前节点的右子树.
* 递归返回条件是已经取完了数组中的所有数，没有其它数可取，此时我们返回空节点.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 13:18:09
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 13:30:43


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        return self.recursion(0, len(nums)-1, nums)

    def recursion(self, left, right, nums):
        # 递归结束条件，当left大于right时,返回空节点
        if left > right:
            return None
        # 取中间值作为当前根节点
        middle = left+((right-left) >> 1)
        # 声明根节点
        root = TreeNode(nums[middle])
        # 生成左子树
        leftree = self.recursion(left, middle-1, nums)
        # 生成右子树
        rightree = self.recursion(middle+1, right, nums)
        root.left = leftree
        root.right = rightree
        # 返回根节点
        return root
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-30-108-Convert-Sorted-Array-to-Binary-Search-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-108-convert-sorted-array-to-binary-search-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
