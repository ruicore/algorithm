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
