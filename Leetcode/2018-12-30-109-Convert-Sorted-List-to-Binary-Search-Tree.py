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

