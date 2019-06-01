# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-06-01 16:53:14
# @Last Modified by:   何睿
# @Last Modified time: 2019-06-01 18:25:18

import bisect
from typing import List, Dict, Set


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.added = set()  # type:Set([int])
        self.num_bisect = list()  # type:List[int]
        # 第一个区间初始化为 -2，或者比 -2 更小的数
        self.invs = [[-2, -2]]  # type:List[List[int]]

    def addNum(self, val: int) -> None:

        # 如果 val 已经被添加过，那么不用再次添加
        if val in self.added: return
        self.added.add(val)
        # 用 bisect 将数字插入到数组中，为下一次生成区间做准备
        # 在这里使用 insort_left 或 insort_right 效果一样
        bisect.insort_left(self.num_bisect, val)

    def getIntervals(self) -> List[List[int]]:

        # 外层循环，为每一个 num 找到其应该落在的区间
        for num in self.num_bisect:
            # 内层循环，遍历每一个区间
            for i in range(len(self.invs)):
                # 如果 num 在区间 invs[i] 的内部，则什么都不做
                if self.invs[i][0] < num < self.invs[i][1]:
                    break

                # 如果 num 在区间的 self.invs[i] 的右边一个
                # 则扩充 self.invs[i] 区间
                elif num == self.invs[i][1] + 1:
                    self.invs[i][1] += 1

                    # 如果 self.invs[i] 后面还有区间
                    # 并且 num 和 self.invs[i+1]的左边界相差 1
                    # 将区间 self.invs[i] 与 self.invs[i+1]合并，删除 self.invs[i+1]
                    if i + 1 < len(self.invs):
                        if self.invs[i + 1][0] == num + 1:
                            self.invs[i][1] = self.invs[i + 1][1]
                            del self.invs[i + 1]
                    break
                
                # 如果 num 在区间的 self.invs[i] 的左边一个
                # 扩充左区间
                elif num + 1 == self.invs[i][0]:
                    self.invs[i][0] = num
                    break
                else:
                    # 如果 num 比前一个区间的尾部值大并到了最后一个位置
                    if i + 1 == len(self.invs) and num > self.invs[i][1] + 1:
                        self.invs.append([num, num])
                        break
                     # 如果 num 比前一个区间的尾部值大比后一个区间前部值小
                    elif self.invs[i][1] + 1 < num < self.invs[i + 1][0] - 1:
                        self.invs.insert(i + 1, [num, num])

        self.num_bisect = list()
        return self.invs[1:]
