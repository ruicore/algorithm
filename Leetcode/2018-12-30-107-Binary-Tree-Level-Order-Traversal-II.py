# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-30 12:13:55
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-30 12:33:53


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, queue, line = [], deque(), 0
        queue.append(root)
        while queue:
            line += 1
            # 当前层的节点个数
            count = len(queue)
            temp = []
            for _ in range(count):
                # 从左往右取当前层的节点
                top = queue.popleft()
                # 添加当前层节点的值
                temp.append(top.val)
                # 把当前层当前节点的左节点添加到队尾
                if top.left:
                    queue.append(top.left)
                # 把当前层当前节点的右节点添加到队尾
                if top.right:
                    queue.append(top.right)
            res.append(temp)
        # 最后倒转原来的顺序即可
        return [res.pop() for _ in range(line)]
