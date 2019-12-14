# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-12-14 10:29:10
# @Last Modified by:   何睿
# @Last Modified time: 2019-12-14 10:39:51


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        return self.dfs(grid, 0, 0, len(grid))

    def dfs(self, grid, h, w, N):

        total = sum([grid[h + i][w + j] for i in range(N) for j in range(N)])   # 求取当前方格内的和

        if total == 0:                                              # 如果方格内所有元素都是0
            return Node(False, True, None, None, None, None)        # 构造一个值为False的叶子节点

        elif total == N * N:                                        # 如果方格内所有元素都是1
            return Node(True, True, None, None, None, None)         # 构造一个值为True的叶子节点

        else:                                                       # 说明方格内有0有1
            root = Node('*', False, None, None, None, None)         # 构造一个值为"*"的中间结点
            n = N // 2                                              # 求方格的一半
            root.topLeft = self.dfs(grid, h, w, n)                       # 构建左上子树
            root.topRight = self.dfs(grid, h, w + n, n)                    # 构建右上子树
            root.bottomLeft = self.dfs(grid, h + n, w, n)                  # 构建左下子树
            root.bottomRight = self.dfs(grid, h + n, w + n, n)               # 构建右下子树
            return root
