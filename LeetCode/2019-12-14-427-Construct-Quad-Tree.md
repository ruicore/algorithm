# LeetCode 427. Construct Quad Tree

## Description

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:

It can be divided according to the definition above:

The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.

Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.

## 描述

我们想要使用一棵四叉树来储存一个 N x N 的布尔值网络。网络中每一格的值只会是真或假。树的根结点代表整个网络。对于每个结点, 它将被分等成四个孩子结点直到这个区域内的值都是相同的.

每个结点还有另外两个布尔变量: isLeaf 和 val。isLeaf 当这个节点是一个叶子结点时为真。val 变量储存叶子结点所代表的区域的值。

你的任务是使用一个四叉树表示给定的网络。下面的例子将有助于你理解这个问题：

给定下面这个8 x 8 网络，我们将这样建立一个对应的四叉树：

由上文的定义，它能被这样分割：

对应的四叉树应该像下面这样，每个结点由一对 (isLeaf, val) 所代表.

对于非叶子结点，val 可以是任意的，所以使用 * 代替。

提示：

N 将小于 1000 且确保是 2 的整次幂。
如果你想了解更多关于四叉树的知识，你可以参考这个 wiki 页面。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-quad-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
### 思路

```py
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

        # 求取当前方格内的和
        total = sum([grid[h + i][w + j] for i in range(N) for j in range(N)])   

        # 如果方格内所有元素都是0,构造 False 节点
        if total == 0:                                              
            return Node(False, True, None, None, None, None)        
        # 如果全部为 1，构造 True节点
        elif total == N * N:                                        
            return Node(True, True, None, None, None, None) 
        # 否则拆分方格子，分别构造        
        else:                                                       
            root = Node('*', False, None, None, None, None)       
            n = N // 2                                              
            root.topLeft = self.dfs(grid, h, w, n)                       
            root.topRight = self.dfs(grid, h, w + n, n)                    
            root.bottomLeft = self.dfs(grid, h + n, w, n)  
            root.bottomRight = self.dfs(grid, h + n, w + n, n)               
            return root

```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-12-14-427-Construct-Quad-Tree.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-427-construct-quad-tree/) ，作者信息和本声明.
