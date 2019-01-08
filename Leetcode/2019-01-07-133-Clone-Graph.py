# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-07 16:11:20
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-08 17:07:43

# Definition for a undirected graph node

import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # 广度优先遍历
        if not node:
            return None
        # 声明一个dict用于存储对应关系
        # 声明一个队列用于存储下一层将要处理的节点
        Nodedict, queue = {}, collections.deque()
        queue.append(node)
        Nodedict[node] = None

        # 第一个循环复制节点
        while queue:
            original = queue.popleft()
            newnode = UndirectedGraphNode(original.label)
            # 下一层将要处理的节点
            Nodedict[original] = newnode
            for item in original.neighbors:
                # 还没有遍历的节点
                if item not in Nodedict:
                    queue.append(item)
                    Nodedict[item] = None
        # 添加每一个节点能够走到的所有节点
        for Node in Nodedict:
            newnode = Nodedict[Node]
            for item in Node.neighbors:
                newnode.neighbors.append(Nodedict.get(item))
        return Nodedict[node]
