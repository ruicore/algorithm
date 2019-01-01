# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-01 09:47:40
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-01 10:02:57

# Definition for binary tree with next pointer.


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


from collections import deque


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        # 声明一个队列
        queue = deque()
        # 将根节点放入队首
        queue.append(root)
        while queue:
            # 取出队首节点
            first = queue.popleft()
            # 获取当前层剩余的个数
            nums = len(queue)
            # 如果当前节点左子节点不为空
            if first.left:
                # 将当前节点的左子节点放入队尾
                queue.append(first.left)
            # 如果当前节点的右子节点不为空
            if first.right:
                # 将当前节点的右子节点放入队尾
                queue.append(first.right)
            # 遍历当前层的剩余节点
            for _ in range(nums):
                sec = queue.popleft()
                if sec.left:
                    queue.append(sec.left)
                if sec.right:
                    queue.append(sec.right)
                first.next = sec
                first = sec
            # 将最后一个节点置为None
            first.next = None
