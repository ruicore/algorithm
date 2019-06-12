# LeetCode 114. Flatten Binary Tree to Linked List

## Description

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```python
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```python
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## 描述

给定二叉树，将其平铺展开，成为一条链表.

### 思路

* 题意是给定一颗二叉树，将其展开成为一个链表，要求原地转换，不要申请额外的空间来存储链表.\(用每个节点的右指针作为链表的指针，做指针置为空).
* 此题目使用递归求解.
* 我们假设当前节点root的左子树已经构成了一条链表，当前节点的右子树已经构成了一条链表，则:

1. 我们找到root左子树构成的链表的末尾节点node，让node.right指向root右子树.
2. 此时左子树已经完成了链表的构建，我们把root左子树挂到root右子树上.
3. 最后将左子树置为空.

* 如上进行递归调用即可,注意递归返回条件：

1. 如果当前节点为空节点，我们返回.
2. 如果当前节点没有左子树，说明右边已经构成了链表，此时我们也直接返回.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-31 11:24:07
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-31 11:48:55

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 对左边进行转换
        self.flatten(root.left)
        # 对右边进行转换
        self.flatten(root.right)
        # 如果此时左边已经没有节点，直接返回
        if not root.left:
            return
        else:
            # 首先找到左子树的最右边的节点
            node = root.left
            while node.right:
                node = node.right
            # 将跟节点右子树放到左子树的最右节点
            node.right = root.right
            # 将根节点的左子树放到根节点的右子树
            root.right = root.left
            # 将根节点的左子树置为空
            root.left = None
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-31-114-Flatten-Binary-Tree-to-Linked-List.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-114-flatten-binary-tree-to-linked-list/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
