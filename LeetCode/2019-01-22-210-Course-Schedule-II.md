# LeetCode 210. Course Schedule II

## Description

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, \[\[1,0]] 
Output: \[0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, \[\[1,0],\[2,0],\[3,1],\[3,2]]
Output: \[0,1,2,3] or \[0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is \[0,1,2,3]. Another correct ordering is \[0,2,1,3] .

## 描述

现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: \[0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, \[\[1,0]] 
输出: \[0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, \[\[1,0],\[2,0],\[3,1],\[3,2]]
输出: \[0,1,2,3] or \[0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 \[0,1,2,3] 。另一个正确的排序是 \[0,2,1,3] 。

### 思路

* 此题目和是207题[CourseSchedule](https://leetcode.com/problems/course-schedule)进阶题，我们要返回可能上课的顺序.
* 整体思路和[207](https://www.ruicore.cn/leetcode-207-course-schedule/)一样，我们额外增加一个数量，来记录访问的入度为0的课程即可.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-22 12:23:34
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-22 22:23:34

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
        # !!! 注意题目并没有保证一定有界
        # 如果不能将所有的课程上完，我们返回空
        for item in indegree:
            if item: return []
        return res
```
源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-22-210-Course-Schedule-II.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-210-course-schedule-ii/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
