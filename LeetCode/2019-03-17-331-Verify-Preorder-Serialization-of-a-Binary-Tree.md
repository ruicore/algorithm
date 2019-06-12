# LeetCode 331. Verify Preorder Serialization of a Binary Tree

## Description

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

```py
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
```

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false

## 描述

序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

```py
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
```

例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
示例 2:

输入: "1,#"
输出: false
示例 3:

输入: "9,#,#,1"
输出: false

### 思路

* 使用栈，如果两个 # 连续出现，根据前序遍历的定义，前面一个一定是叶子节点，我们将这两个 # 弹出，然后将叶子节点重置为 None (即#)，如此循环下去。
* 如果满足前序遍历，那么最后栈中有且仅有一个元素，且是 # 。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-17 09:44:27
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-17 10:03:55


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # stack：用于记录遍历到的节点值
        # count：stack 中剩余的节点个数
        stack, count = [], 0
        for item in preorder.split(","):
            stack.append(item)
            count += 1
            # 如果 stack 中末位两个元素是 #，说明这两个节点前面是一个叶子节点
            # 将两个 # 弹出 ，将叶子节点置为 None，即 #
            # 如果是前序遍历，那么 stack 最后一定会剩下一个 # 
            while count > 1 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                if not stack: return False
                stack[-1] = "#"
                count -= 2
        # 当且仅当 stack 中只剩下一个元素且为 # 时返回 True.
        return True if len(stack) == 1 and stack[0] == "#" else False
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-03-17-331-Verify-Preorder-Serialization-of-a-Binary-Tree.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://www.ruicore.cn/leetcode-331-verify-preorder-serialization-of-a-binary-tree/) ，作者信息和本声明.
