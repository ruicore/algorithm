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