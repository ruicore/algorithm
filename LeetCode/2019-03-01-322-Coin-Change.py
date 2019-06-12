# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-03-01 10:21:19
# @Last Modified by:   何睿
# @Last Modified time: 2019-03-01 14:33:42


class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        # 声明一个二维矩阵
        matrix = [[i for i in range(amount + 1)] for _ in range(2)]
        # 初始化第一行
        for i in range(amount + 1):
            # 如果当前位置表示的需要兑换的钱数可以被整除，将当前位置置为需要钱的个数
            if i % coins[0] == 0:
                matrix[0][i] = i // coins[0]
            # 否则将当前的钱数目置为 amount+1
            else:
                matrix[0][i] = amount + 1
        for i in range(1, len(coins)):
            for j in range(amount + 1):
                row = i % 2
                # 不使用第 i 个硬币，仅使用 i 前面的所有硬币
                # 则一共需要当前行上一行对应位置的硬币
                top = matrix[(i - 1) % 2][j]
                # 使用当前的硬币，如果当前需要兑换的硬币面值大于当前硬币的面值
                if j >= coins[i]:
                    # 动态规划：兑换面值为 a 的硬币，在已经使用了coins[0:col-1]这些硬币的情况下
                    # 可以由 a - coins[col] 需要的硬币加上硬币 coins[col]，
                    # 所以需要的硬币个数为 matrix[row][a - coins[col]]+1；
                    # 也可以不使用当前的硬币，仅仅使用前 i 个硬币
                    # 那么需要的硬币个数为 matrix[row-1][col]
                    # 取出最下值
                    matrix[row][j] = min(top, matrix[row][j - coins[i]] + 1)
                else:
                    matrix[i % 2][j] = top
        res = 0
        # 为了节省空间，我们的矩阵仅仅使用了两行，
        # 如果 coins 的个数为奇数个，那么最终结果在第一行
        if len(coins) % 2:
            res = -1 if matrix[0][-1] == amount + 1 else matrix[0][-1]
        # 如果 coins 的个位数为偶数个，那么最终结果为第二行
        else:
            res = -1 if matrix[1][-1] == amount + 1 else matrix[1][-1]
        return res

    def coinChange2(self, coins: [int], amount: int) -> int:
        # 思路同方法一完全一样，仅仅是换了一种写的方式
        # python 对于列表解析式的执行效率更快
        count = amount + 1
        line = [i for i in range(count)]
        for i in range(1, count):
            line[i] = min(line[i - c] if i >= c else count for c in coins)
            if line[i] != count: line[i] += 1
        return line[-1] if line[-1] != count else -1