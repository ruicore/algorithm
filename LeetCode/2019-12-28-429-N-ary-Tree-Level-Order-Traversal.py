# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-12-28 21:23:06
# @Last Modified by:   何睿
# @Last Modified time: 2019-12-28 21:34:42


from typing import List
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            tmp = []
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                tmp.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(tmp)

        return result
