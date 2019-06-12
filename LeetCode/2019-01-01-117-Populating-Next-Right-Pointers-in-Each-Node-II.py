# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 12:01:48
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 12:02:08


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        head = root
        child, chidhead = None, None
        # head在这里控制垂直的循环，即控制从上到下二叉树的所有层
        while head:
            # head在这里控制一层的每一个节点
            while head:
                # 如果head有左节点
                if head.left:
                    # 如果head下一层的首节点已经被设置好了
                    if chidhead:
                        # 将child.next指针指向head.left节点
                        child.next = head.left
                        # child指针向后走一步
                        child = head.left
                    else:
                        # 否则我们初始化childhead指向head下面一层的首节点
                        chidhead = head.left
                        # 初始化child指向首节点
                        child = head.left
                # 如果head有右节点
                if head.right:
                    # 同理如果head下一层的首部节点已经设置
                    if chidhead:
                        # child的next指针指向右节点
                        child.next = head.right
                    else:
                        # 同理如果childhead没有设置，我们初始化childHead
                        chidhead = head.right
                    # 如上 child = head.right可以单独从两个判断种提出来，因为两种情况都需要执行
                    child = head.right
                # head指针向后走一步
                head = head.next
            # 更新head指向下一层
            head = chidhead
            # 重置指向下一层的指针
            chidhead, child = None, None
