# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-13 11:25:33
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-13 13:16:53


# 使用双向链表，存储页面信息，每一个节点都需要连个指针，一个指向前驱结点，一个指向后继节点
# 根据题意key相当于页面号，value相当于页面中的内容
# 链表中的head，tail节点用作辅助节点
class Node:
    def __init__(self, key, value):
        # key相当于请求的页面
        self.key = key
        # value相等于页面中存储的信息
        self.value = value
        # 指向后继节点
        self.next = None
        # 指向前驱结点
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # 页面最大容量
        self.capacity = capacity
        # 字典用于存储链表节点的索引，根据key查找页面
        self._dict = dict()
        # 链表头节点
        # 头节点后面的节点是最早使用的
        self.head = Node(0, 0)
        # 链表尾节点
        # 尾节点前面的节点是刚刚才使用过的
        self.tail = Node(0, 0)
        # 让链表头尾相连
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 如果要查找的页面已经被分配
        if key in self._dict:
            # 获取当前节点
            node = self._dict[key]
            # 我们将此节点移动到尾节点前面，表示此节点最近被使用过
            # 此操作分两步 1. 在节点在双向链表中删除（只是删除节点引用，不删除节点本身）
            self._remove(node)
            # 将节点添加到双向链表的末尾（tail节点前面）
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # 如果要添加的页面已经被分配到页面中，将当前节点删除（删除在链表中的指向，并且删除节点本身）
        if key in self._dict:
            self._remove(self._dict[key])
            del self._dict[key]
        # 新建一个节点
        node = Node(key, value)
        # 添加当前节点
        self._add(node)
        # 建立字典，以key为键，节点的引用为值
        self._dict[key] = node
        # 如果当前的最大容量已经超过了给定的容量，则删除head后面的第一个节点（最近最久未被使用）
        if len(self._dict) > self.capacity:
            node = self.head.next
            # 在双线链表中删除节点
            self._remove(node)
            # 删除字典中的引用
            del self._dict[node.key]
            # 删除当前节点本身
            del node

    def _remove(self, node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
        node.prev = None
        node.next = None

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
