# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-20 14:32:25
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-20 14:34:24

from collections import deque


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            num = len(queue)
            for _ in range(num):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res