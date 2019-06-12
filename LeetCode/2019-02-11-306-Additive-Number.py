# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-11 20:50:12
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-11 21:25:41


class Solution:
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        # 根据题意，累计加数至少有三个
        if len(num) < 3: return False
        self.res = False
        # 深度优先搜索，遍历所有可能的解
        self.__dfs(0, num, [])
        return self.res

    def __dfs(self, start, num, coms):
        # 递归结束条件，当num中没有数字时，检查当前组合是否满足条件
        if start == len(num):
            # 如果当前组合合法，我们将self.res置为True
            if self.__valid(coms): self.res = True
            return
        # 记录起始位置
        index = start
        while index < len(num):
            # 如果当前数字的起始数字是"0'退出循环（注意单独一个'0'本身是合法的）
            if num[start] == "0" and index != start: break
            # 如果当前的组合已经有了至少3个数，我们检查前面的所有数是否是累加数
            # 如果不是我们退出循环，表示当前的分支不用再查找，减少时间
            if len(coms) > 2 and not self.__valid(coms): break
            # 递归遍历分支
            self.__dfs(index + 1, num, coms + [num[start:index + 1]])
            index += 1

    def __valid(self, coms):
        # 如果一共都没有三个数，返回False
        if len(coms) < 3: return False
        for i in range(len(coms) - 2):
            # 只要有一个不满足累加数的条件，返回False
            if int(coms[i]) + int(coms[i + 1]) != int(coms[i + 2]):
                return False
        return True
