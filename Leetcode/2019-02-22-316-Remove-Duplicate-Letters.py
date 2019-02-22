# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-22 14:27:31
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-22 15:38:39

import collections


class Solution:
    def removeDuplicateLetters(self, s: 'str') -> 'str':
        # stack 用于存储结果
        # visited 表示当前的字符已经遍历过
        stack, visited = [], set()
        # times 是一个字典，键为字符，值为字符出现过的次数
        times = collections.Counter(s)
        for item in s:
            # 让字典 times 中记录的对应次数减少一次
            times[item] -= 1
            # 如果 item 还没有遍历过，即 item 没有出现在结果中
            # visited 和 stack 里面的字符内容是一样的
            # 只不过我们用stack 是为了从栈顶开始删除
            # 用 visited 可以在 O(1) 时间复杂度内判断一个元素是否被遍历过并且在 O(1) 内删除一个元素
            if item not in visited:
                # 如果当前元素比栈顶元素小并且栈顶元素在当前元素后面还会出现
                # 那么当前元素应该带栈顶元素的前面
                # 我们弹出栈顶元素，在 visited 中删除栈顶元素的记录
                while stack and item < stack[-1] and times[stack[-1]] != 0:
                    visited.remove(stack.pop())
                # 此时有下列三种情况
                # 1. 栈已经空了 
                # 2. 当前元素大于栈顶元素 
                # 3. 当前元素小于栈顶元素但是栈顶元素在当前元素后面不再出现
                # 我们将当前元素压入栈顶，在 visited 元组中记录当前元素已经被访问过
                stack.append(item)
                visited.add(item)
        # 注意题目要求返回字符串
        return ''.join(stack)