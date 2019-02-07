# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-07 09:14:58
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-07 13:31:18


class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        res = []
        expression = [0] * (2 * len(num) - 1)
        self.__dfs(num, target, 0, expression, 0, 0, 0, res)
        return res

    def __dfs(self, num, target, start, exp, vaild, prev, curr, res):
        if start == len(num):
            if curr == target:
                res.append("".join(exp[0:vaild]))
                return
        n = 0
        s = start
        l = vaild
        if s: vaild += 1
        while start < len(num):
            n = n * 10 + (ord(num[start]) - ord('0'))
            if num[s] == "0" and start - s > 0: break
            exp[vaild] = num[start]
            vaild += 1
            start += 1
            if s == 0:
                self.__dfs(num, target, start, exp, vaild, n, n, res)
                continue
            exp[l] = "+"
            self.__dfs(num, target, start, exp, vaild, n, curr + n, res)
            exp[l] = "-"
            self.__dfs(num, target, start, exp, vaild, -n, curr - n, res)
            exp[l] = "*"
            self.__dfs(num, target, start, exp, vaild, prev * n,curr - prev + prev * n, res)


if __name__ == "__main__":
    so = Solution()
    res = so.addOperators("179898705", 6565)
    print(res)