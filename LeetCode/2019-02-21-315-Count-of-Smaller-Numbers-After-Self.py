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
            # smaller 表示比当前节点小的节点个数
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
            bisect.insort_right(visited, num)
        # 返回逆序的结果数组
        return res[::-1]
