# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-08 14:01:53
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-08 14:45:23

from collections import deque


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque()
        # 遍历得到所有的元素
        self._get_elements(nestedList)
        # 统计元素的个数
        self.count = len(self.queue)

    def _get_elements(self, nestedList):
        for item in nestedList:
            # isInteger 方法是 NestedIterator 类提供的方法
            # 如果是整型，将该数组添加到双端队列中
            if item.isInteger():
                self.queue.append(item.getInteger())
                # 如果是一个 List ，递归调用 _get_elements
            else:
                self._get_elements(item.getList())
        return

    def next(self):
        """
        :rtype: int
        """
        hasnext = self.hasNext()
        if hasnext:
            self.count -= 1
            # 返回下一个元素
            return self.queue.popleft()
        return False

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0