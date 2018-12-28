# LeetCode 99. Recover Binary Search Tree

## Description

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

```python

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
```

```python
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

## 描述

* 一个二叉搜索树的两个节点被交换了，使得此二叉搜索树出现了错误，要求是把这两个值换回来.

### 思路

* 此题使用中序遍历，找到被错误地交换的两个节点，把它们的值交换回来即可.

```python

# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-28 12:15:59
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-28 18:50:58

# Definition for a binary tree node.

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 是否为第一次遍历，第一个不符合的节点，第二个不符合的节点
        isfirst, first, second, pre = True, None, None, TreeNode(-sys.maxsize-1)
        while root:
            # 如果root有左子树
            if root.left:
                # 另temp指向root的左子树
                temp = root.left
                # 当temp有右子树并且temp的右子树没有指向root节点
                while temp.right and temp.right != root:
                    temp = temp.right
                # 如果temp已经走到了最右边
                if not temp.right:
                    # 如果第一次到达子树的右边，进行建桥操作
                    temp.right = root
                    # root指向子树
                    root = root.left
                # 如果temp的右子树已经指向了root根节点，说明已经遍历过当前节点，进行拆桥操作
                if temp.right == root:
                    # 拆桥
                    temp.right = None
                    if pre.val > root.val and isfirst:
                        first = pre
                        isfirst = False
                    if pre.val > root.val and not isfirst:
                        second = root
                    pre = root
                    root = root.right
            else:
                if pre.val > root.val and isfirst:
                    first = pre
                    isfirst = False
                if pre.val > root.val and not isfirst:
                    second = root
                pre = root
                root = root.right
        # 找到了两个元素，进行交换.
        if first and second:
            first.val, second.val = second.val, first.val
        return
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-28-99-Recover-Binary-Search-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-99-recover-binary-search-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
