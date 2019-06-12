# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-08 09:48:07
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-09 16:37:40


class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        children = len(ratings)
        # 首先给每一个孩子分一颗糖果
        res = [1 for _ in range(children)]
        # 然后正向遍历，如果当前孩子的评分大于前面一个孩子的评分，则把前一个孩子分的糖果数目加一分给当前孩子
        # 这样就满足了每个分高的孩子的糖果大于前一个孩子的糖果
        for i in range(1, children):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1]+1
        # 然后反向遍历，如果当前孩子评分比后面一个孩子高，并且档当前孩子已经分得的糖不多有后面一个孩子
        # 我们给当前孩子分其后面一个孩子糖果加一个数的糖
        for i in range(children-2, -1, -1):
            if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = res[i+1]+1
        # 最后我们返回其总和即可
        return sum(res)
