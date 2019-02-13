# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-02-12 10:38:03
# @Last Modified by:   何睿
# @Last Modified time: 2019-02-12 11:05:30


class NumArray:
    def __init__(self, nums: 'List[int]'):
        # 声明一个线段树
        self.segtree = None
        # 给定数组元素的个数
        self.size = len(nums)
        if self.size:
            # 线段树个数为原数组的两倍
            self.segtree = [0] * (self.size * 2)
            # 生成线段树
            self.__build(nums)

    def update(self, i: 'int', val: 'int') -> 'None':
        # 获取元素的真实索引
        i += self.size
        # 更新给定元素的值
        self.segtree[i] = val
        while i > 0:
            # 获取叶节点的左右节点
            left, right = i, i
            # 如果当前节点是左节点
            if i % 2 == 0:
                # 右节点是当前节点的右边一个
                right = i + 1
            # 如果当前是右节点
            else:
                # 左节点是当前节点的左边一个
                left = i - 1
            # 更新父节点
            self.segtree[i // 2] = self.segtree[left] + self.segtree[right]
            i //= 2

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        # 获取元素在树中的索引
        i += self.size
        j += self.size
        res = 0
        while i <= j:
            # 如果i是右节点
            if i % 2 != 0:
                # 加上右节点的值
                res += self.segtree[i]
                # i 指向左节点
                i += 1
            # 如果j是左节点
            if j % 2 != 1:
                # 加上左节点的值，
                res += self.segtree[j]
                # 更新j指向右节点
                j -= 1
            # i，j指向其父节点
            i //= 2
            j //= 2
        return res

    def __build(self, nums):
        # 构造线段树的函数
        for i in range(self.size):
            self.segtree[i + self.size] = nums[i]
        for i in range(self.size - 1, -1, -1):
            self.segtree[i] = self.segtree[2 * i] + self.segtree[2 * i + 1]
        return
