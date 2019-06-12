# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-08 16:23:16
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-08 17:58:28

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 我们使用二叉树的前序遍历来序列化二叉树
        # 我们用空格来区分每个节点
        # 我们用"None"来记录末尾的节点 
        if not root: return 'None '
        self.res = ''
        self.__serialize(root)
        return self.res

    def __serialize(self, root):
        # 二叉树的前序遍历，递归实现
        if not root:
            self.res += "None "
            return
        self.res += str(root.val) + " "
        self.__serialize(root.left)
        self.__serialize(root.right)
        return

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 反序列化，我们把输入的字符串用空格区分
        # 注意要去掉最后一个空格
        # 我们用队列来存储所有节点的值
        _data = deque(data[:-1].split(' '))
        return self.__deserialize(_data)

    def __deserialize(self, data):
        # 当没有节点时返回空
        if not data: return None
        # 每次从队首弹出元素
        value = data.popleft()
        if value == "None": return None
        root = TreeNode(int(value))
        # 序列化左子树
        root.left = self.__deserialize(data)
        # 序列化右子树
        root.right = self.__deserialize(data)
        return root