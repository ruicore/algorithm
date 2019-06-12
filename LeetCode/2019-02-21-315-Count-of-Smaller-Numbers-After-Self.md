# LeetCode 315. Count of Smaller Numbers After Self

## Description

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

```py
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

## 描述

给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

```py
输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
```

### 思路

* 基本思路是我们从后往前遍历，依次把数字插入到一个数据结构中，每次插入的时候返回数据结构中比这个数小的数的个数，用一个数组记录返回的结果，这里把记录结果的数组命名为 res。
* 我们最后返回 res 的逆序 「因为我们是逆序地从给定的数组中选取数字的」。
* 关于数据结构的选取：
* 方法一：对于 python 语言，我们借助 python 自带的库函数 bisect ，通过数组来实现。有关  bisect 的语法，请参考 [这里](https://docs.python.org/3.0/library/bisect.html)。
* bisect.bisect_left(list, item) 函数把 item 插入到 list 中，并且保持 list 是排序的顺序，如果 item 已经存在于 list 将会把 item 插入到 list 的最左边。
* 我们声明一个数组 visited 用于插入元素，我们用 bisect.bisect_left(visited, item) 获得 item 应该插入到 visited 中的位置，把这个值添加到数组 res 中。这个位置的值就是数组中小于等于 item 元素的个数，注意 ：这里一定要用 bisect_left，不能用 bisect_right 因为如果出现了 重复的元素，bisect_right 把重复的元素算在内 「因为 bisect_right 会插入在重复元素的右边」，而题意是找小于当前元素的元素个数，不包含等于。
* 获取了元素插入的位置后，我们使用 bisect.insort_right 将元素插入到 visited 中 「使用 bisect.insort_left 也可以」。
* 返回 res 的逆序。
* 方法二：使用二叉搜索数。有关二叉搜索数和平衡二叉搜索树请参考这个 [视频](https://www.youtube.com/watch?v=jDM6_TnYIqE)。
* 注意：1. 我们这里的二叉搜索树不需要实现全部功能，这道题里面只需要用到 insert 功能。2. 二叉搜索树不存储重复的元素。
* 二叉树的节点我们声明五个变量：1. value 用于存储节点的值。 2. count 用于表示当前值出现的次数，默认为1。3. smaller 表示比当前节点值小的节点的个数。 4. left_child 左子树。5. right_child 右子树。
* 在向二叉树中插入值 value 的时候，如果插入的值比当前的节点小，当前节点的 smaller 自增一次，并且将 value 插入到左子树中，在最后创建新节点的后返回 0。
* 如果插入的值比当前节点的值大，我们记下当前位置比 value 小的节点个数 count + smaller，然后将 value 插入到当前节点的右子树中，在最后创建新节点后返回 count + smaller。
* 如果要插入的元素的值和当前节点的值相等，返回 当前节点的 smaller 值。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-20 13:55:15
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-21 11:48:51

# python 内部二分搜索库
import bisect


# 二叉搜索树的节点
class Node:
    def __init__(self, value=None):
        # 节点的值
        self.value = value
        # 二叉搜索树不存储重复节点，我们用 count 来存值出现的次数
        self.count = 1
        # 比当前元素值小的元素个数
        self.smaller = 0
        # 左子树
        self.left_child = None
        # 右子树
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return 0
        else:
            return self._insert(value, self.root)

    def _insert(self, value, node):
        # 如果当前需要插入的值比当前节点的值小
        if value < node.value:
            # node.smaller 自增一次
            node.smaller += 1
            # 如果当前节点还没有左子树
            if node.left_child == None:
                # 创建一个新的节点
                node.left_child = Node(value)
                # 返回 0  表示比当前插入元素还小的元素个数为 0
                return 0
            else:
                # 否则将当前元素插入到当前节点的左子树
                return self._insert(value, node.left_child)
        # 如果当前需要插入的值比当前节点的值大
        elif value > node.value:
            # smaller 表示当前节点连接的左子树的所有节点个数
            # 左子树的所有节点值一定比当前节点小
            # 由于树是动态创建的，因此比 value 值小的节点在当前节点的左子树和当前节点的右子树的左子树中
            smaller = node.count + node.smaller
            # 如果当前节点还没有右子树
            if node.right_child == None:
                # 创建一个新的节点
                node.right_child = Node(value)
                # 返回 smaller
                return smaller
            else:
                # 如果有右子树，说明当前值不仅比当前节点的左子树的节点值大
                # 有可能比当前节点的右子树的左子树节点大，
                # smaller 仅仅记录了当前节点的左子树
                # 返回 smaller + 当前节点右子树中比要插入的值小的元素个数
                return smaller + self._insert(value, node.right_child)
        else:
            # 如果当前要插入的值已经在二叉搜索树中，count 自增一次
            node.count += 1
            # 返回 node.smaller
            return node.smaller


class Solution:
    # 第一种方法，我们借助二叉搜索树实现
    # 需要自己实现二叉搜索数 「只需要实现插入部分，查找和删除在这里用不到」
    def countSmaller(self, nums: 'List[int]') -> 'List[int]':
        Tree = BinarySearchTree()
        res = []
        for num in nums[::-1]:
            # 从后向前插入，每次插入一个值，返回树中比当前元素小的元素的个数
            res.append(Tree.insert(num))
        # 因为我们是从后面向前插入的，所以需要返回逆序的结果数组
        return res[::-1]

    # 方法二，借助python 二分搜索库
    def countSmaller2(self, nums: 'List[int]') -> 'List[int]':
        res, visited = [], []
        for num in nums[::-1]:
            # num 插入位置的索引就是比他小的元素的个数
            res.append(bisect.bisect_left(visited, num))
            # 将 num 元素插入到 visited 数组中 
            # 这里使用 insort_right 或者 insort_left 均可
            bisect.insort_right(visited, num)
        # 返回逆序的结果数组
        return res[::-1]
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-21-315-Count-of-Smaller-Numbers-After-Self.py)。
©本文首发于 [何睿的博客](https://www.ruicore.cn/leetcode-315-count-of-smaller-numbers-after-self/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
