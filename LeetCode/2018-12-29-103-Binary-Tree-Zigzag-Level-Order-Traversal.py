# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-29 18:55:05
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-29 19:20:04

# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 如果子树为空，则直接返回空
        if not root:
            return []
        # 当前遍历层的所有节点，下一层将遍历的所有节点
        currnode, nextnode, res = [root], [], []
        # 数组的起始位置，数组的结束位置，当前层数的所有节点个数
        start, end, count = 0, 0, 1
        # 循环条件，只有当前层还有节点需要遍历才执行
        reverse = False
        while currnode:
            # 索引开始地址，索引结束地址
            start, end = 0, count
            # 当前层所有节点的值，count重置为0
            level, count = [], 0
            for i in range(start, end):
                # 如果当前节点有左节点
                if currnode[i].left:
                    # 左节点将在下一层遍历，放入nextnode数组
                    nextnode.append(currnode[i].left)
                    # 下一层个数自增一次
                    count += 1
                # 如果当前节点有右节点
                if currnode[i].right:
                    # 右节点将在下一层遍历，放入nextnode数组
                    nextnode.append(currnode[i].right)
                    # 下一层个数自增一次
                    count += 1
                # 存储当前节点的值
                level.append(currnode[i].val)
            # 结果数组存储当前层的所有值
            # 如果需要反转，则对结果进行反转
            if reverse:
                level.reverse()
                # 下次不需要反转，重置为False
                reverse = False
            elif not reverse:
                reverse = True
            res.append(level)
            # currnode置为下一层，nextnode重置为空
            currnode, nextnode = nextnode, []
        return res


class Solution2:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 使用队列实现
        if not root:
            return []
        # 是否需要反转，存储结果，队列
        reverse, res, queue = False, [], deque()
        queue.append(root)
        # 循环条件：队列中还有节点
        while queue:
            nums, level = len(queue), []
            # 遍历当前层的所有节点
            for _ in range(0, nums):
                current = queue.popleft()
                # 左子树
                if current.left:
                    queue.append(current.left)
                # 右子树
                if current.right:
                    queue.append(current.right)
                level.append(current.val)
            # 是否需要反转
            if reverse:
                level.reverse()
                reverse = False
            elif not reverse:
                reverse = True
            res.append(level)
        return res
