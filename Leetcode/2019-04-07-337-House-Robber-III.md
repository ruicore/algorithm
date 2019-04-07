# LeetCode 337. House Robber III

## Description

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

```py
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

Example 2:

```py
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
```

## 描述

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

```py
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
```

示例 2:

```py
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
```

### 思路

* 用一个包含两个元素的数组 result ，result\[0] 表示偷当前节点的房子，result\[1] 表示不偷当前节点的房子。
* 如果偷当前的房子，那么 result\[0] =  当前节点的值 + max(左右子树中，不偷根节点房子可以获得的最大值)。
* 如果不偷当前的房子，那么 result\[1] = max(左子树中偷或不偷根节点房子可以获得的最大值) + max(右子树中偷或不偷根节点房子可以获得的最大值)
* 最后可以获得的最大值值为 max(result)

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-07 10:43:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-07 11:00:22


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.recursion(root))

    def recursion(self, root):
        # result[0] 表示偷当前的房子，result[1] 表示不偷当前的房子
        if not root: return [0, 0]
        result = [0, 0]
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        # 偷当前的房子：result[0] ：当前节点的值+ 左右子树中不偷根节点房子的最大值
        result[0] = root.val + left[1] + right[1]
        # 不偷当前的房子：result[1] 那么左右子树的根节点偷不偷都可以，选最大值
        result[1] = max(left[0], left[1]) + max(right[0], right[1])
        return result
```

源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-04-07-337-House-Robber-III.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-337-house-robber-iii/) ，作者信息和本声明.
