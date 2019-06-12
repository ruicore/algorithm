# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-17 13:46:09
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-17 14:15:30


class Solution:
    def findMinHeightTrees(self, n: 'int',edges: 'List[List[int]]') -> 'List[int]':
        # 如果只有一个节点，直接返回当前节点
        if n == 1: return [0]
        # 路径：记录每个节点可以访问到的所有节点 type:list[set()]
        # 更一般的情况是利用字典实现，利用节点作为键，节点能够走到的所有节点
        # 组成的set作为值，但是题中得节点为从0开始的数值，因此可以用list代替字典
        paths = [set() for _ in range(n)]
        #  找到每个节点可以走到的下一个节点
        for node1, node2 in edges:
            paths[node1].add(node2)
            paths[node2].add(node1)
        # 找到所有的叶子节点
        leaves = [node for node in range(n) if len(paths[node]) == 1]
        # root用于记录剩下的节点
        roots = n
        while roots > 2:
            # 更新剩下的节点个数
            roots -= len(leaves)
            # 新的叶子节点
            newleaves = []
            for node in leaves:
                # 获取叶节点的父节点
                parent = paths[node].pop()
                # 从叶节点的父节点中删除当前节点
                paths[parent].remove(node)
                # 如果当前节点的父节点只能访问一个节点，则添加到新叶节点中
                if len(paths[parent]) == 1: newleaves.append(parent)
            leaves = newleaves
        return leaves
