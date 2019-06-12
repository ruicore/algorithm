# LeetCode 222. Count Complete Tree Nodes

## Description

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from [Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees):
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

```python
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

## 描述

给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

```python
输入: 
    1
   / \
  2   3
 / \  /
4  5 6
```

输出: 6

### 思路

* 这道题的基本思路是：我们先求左右子树的高度，如果左子树的高度等于右子树的高度，说明左子树是一颗满二叉树，右子树是一刻完全二叉树
* 如果左子树的高度不等于右子树的高度，说明右子树是一颗满二叉树，左子树不是一颗满二叉树
* 满二叉树的节点数数为2^h-1,再加上当前的根节点，则节点个数为2^h,我们在综述中加上2^h,然后我们继续递归的求解完全二叉树的节点个数即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-27 20:02:19
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-27 20:13:03


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        # 获取左子树的高度
        left = self.depth(root.left)
        # 获取右子树的高度
        right = self.depth(root.right)
        # 如果左右子树的高度相等，则左子树一定是一颗满二叉树
        if left == right:
            return 2**left + self.countNodes(root.right)
        # 如果左右子树高度不相等，则右子树一定是一颗满二叉树
        if left != right:
            return 2**right + self.countNodes(root.left)

    def depth(self, root):
        # 获取完全二叉树的高度
        if not root: return 0
        res = 0
        while root:
            res += 1
            root = root.left
        return res
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-27-222-Count-Complete-Tree-Nodes.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-222-count-complete-tree-nodes/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
