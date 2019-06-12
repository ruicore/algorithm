# LeetCode 109. Convert Sorted List to Binary Search Tree

## Description

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

```python
      0
     / \
   -3   9
   /   /
 -10  5
```

## 描述

给定一个链表，其中元素按升序排序，将其转换为高度平衡的BST。

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

### 思路

* 此题目与[108题](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)类似，只不过给定的原始数据由108题的数组，变成了链表，链表的元素不支持随机访问，导致取中间值不能够通过索引来取得.
* 这里着重说明以下取链表中间值的操作：我们用两个指针slow和fast，slow指针每次向后走一个位置，fast指针每次向后走两个位置，当fast到达末尾时，slow就到达了中间位置.
* 注意结束条件：由于fast指针是被允许走到end位置的，于是就不能用fast.next.next == end 来作为结束条件.由于fast指针每次能够向后走两步，于是fast.enxt == end 时就应该结束循环，fast == end 时 也应该结束循环.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 13:57:09
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 15:47:35


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        return self.recursion(head, None)
    # 链表从start开始，到end结束，左闭右开，[start,end),包括start节点，不包括end节点

    def recursion(self, start, end):
        # 取中间值作为当前根节点
        middle = self.serachmid(start, end)
        # 递归结束条件，当left大于right时,返回空节点
        if not middle:
            return None
        # 声明根节点
        root = TreeNode(middle.val)
        # 生成左子树
        leftree = self.recursion(start, middle)
        # 生成右子树
        rightree = self.recursion(middle.next, end)
        root.left = leftree
        root.right = rightree
        # 返回根节点
        return root
    # 寻找中间值
    def serachmid(self, start, end):
        # 搜索一个链表的中间值
        if start == end:
            return None
        if start.next == end:
            return start
        slow, fast = start, start.next
        # 因为fast每次需要向后走两步，而fast.next.next == end时，fast是被允许走到end的
        # 于是就不能用fast.next.enxt == end 作为结条件，结束条件为fast.next != end and fast !=end:
        while fast and fast.next and fast.next != end and fast !=end:
            slow = slow.next
            fast = fast.next.next
        return slow
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-30-109-Convert-Sorted-List-to-Binary-Search-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-109-convert-sorted-list-to-binary-search-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
