# LeetCode 173. Binary Search Tree Iterator

## Description

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 
Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

## 描述

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

示例：

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 
提示：

next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数.

### 思路

* 二叉搜索树的中序遍历时的数组有序.
* 我们用一个栈来存储二叉搜索树的左节点，每次取元素的时候从栈顶取元素，然后以该元素为根节点，将该元素的左边节点全部压入栈.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-17 10:00:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-17 10:38:45


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的中序遍历
# 我们一路将二叉树的左节点压入栈，当弹出栈的时候，我们压入右节点
class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._append(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        res = self.stack.pop()
        self._append(res.right)
        return res.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.stack:
            return True
        return False

    # 辅助函数，压入栈
    def _append(self, root):
        while root:
            self.stack.append(root)
            root = root.left
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-17-173-Binary-Search-Tree-Iterator.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-173-binary-search-tree-iterator/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
