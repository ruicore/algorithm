# LeetCode 297. Serialize and Deserialize Binary Tree

## Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

```py
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## 描述

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

```py
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5
```

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

### 思路

* 序列化的方式有很多种，我们这里使用前序遍历来序列化二叉树，借助队列来反序列化字符串流.
* 序列化：使用前序遍历遍历一趟二叉树，我们用空格来区分每个节点的值，用"None"来表示空节点.
* 反序列化：将字符换按空格分开，存储在队列中，递归的反序列化左右子树.

```py
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
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-02-08-297-Serialize-and-Deserialize-Binary-Tree.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-297-serialize-and-deserialize-binary-tree/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
