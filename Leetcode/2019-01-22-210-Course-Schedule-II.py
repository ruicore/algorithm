# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 12:23:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 12:23:34

from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res, nextcourse, indegree = [], {}, [0] * numCourses
        # 构建字典，键为课程，值为上完编号为键的课可以上的下一节课
        for item in prerequisites:
            if item[1] not in nextcourse:
                nextcourse[item[1]] = [item[0]]
            else:
                nextcourse[item[1]].append(item[0])
            # 统计每一个课程的入度
            indegree[item[0]] += 1
        # 统计入度为0的课程
        queue = deque()
        for i in range(numCourses):
            if not indegree[i]: queue.append(i)
        # 只要有入度为0的课程就继续循环
        while queue:
            c = queue.popleft()
            res.append(c)
            # 下一次将要上的课程
            for _next in nextcourse.get(c, []):
                # 当前课程已经上了，下一节课入度减一
                indegree[_next] -= 1
                # 将新产生的入度为0的课程添加到队列中
                if not indegree[_next]: queue.append(_next)
        # 如果不能将所有的课程上完，我们返回空
        for item in indegree:
            if item: return []
        return res
