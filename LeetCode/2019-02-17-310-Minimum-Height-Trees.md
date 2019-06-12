# LeetCode 310. Minimum Height Trees

## Description

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

```py
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
```

Example 2 :

```py
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
```

Note:

* According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
* The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## 描述

对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

注意：

该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。

你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。

示例 1:

```py
输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

输出: [1]
```

示例 2:

```py
输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

输出: [3, 4]
```

说明:

* 根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
* 树的高度是指根节点和叶子节点之间最长向下路径上边的数量。
### 思路

* 最小高度树的根节点是图中最长路径的中间节点.
* 我们用一个 List\[set()] 的结构存储每个节点可以访问到的其他节点。一般情况下应该使用字典，以节点为键，能够遍历到的节点组成的哈希set为键，但由于题中的节点是从0开始的数字，我们可以用 List 来代替，索引就是键。
* 最长路径的中间节点最多会有两个：最长路径有奇数个节点，则中间节点有 1 个；最长路径有偶数个节点，则中间节点有 2 个。
* 基本思路是:找到所有的叶子节点，去掉所有叶子节点，找到新的所有叶子节点，去掉所有叶子节点 ... 直到剩下的节点个数小于等于2个。

```py
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
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-17-310-Minimum-Height-Trees.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-310-minimum-height-trees/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
