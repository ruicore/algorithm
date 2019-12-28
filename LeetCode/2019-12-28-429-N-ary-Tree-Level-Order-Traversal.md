# LeetCode 429. N-ary Tree Level Order Traversal

## Description

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
![narytreeexample](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```py
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:
```
![sample_4_964](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
Example 2:

```py
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]

## 描述

给定
一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :


返回其层序遍历:

```py
[
     [1],
     [3,2,4],
     [5,6]
]
```

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 层次遍历，使用队列。
* 将当前层的所有节点押入队中，记下当前队列中元素的个数。
* for 循环取出当前层的元素，每取一个元素，将其的 children 元素押入队列尾部。

```py
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

```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-12-28-429-N-ary-Tree-Level-Order-Traversal.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-429-n-ary-tree-level-order-traversal/) ，作者信息和本声明.
