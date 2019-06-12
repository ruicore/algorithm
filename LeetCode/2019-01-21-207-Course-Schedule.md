# LeetCode 207. Course Schedule

## Description

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2,\[\[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, \[\[1,0],\[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

## 描述

现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, \[\[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, \[\[1,0],\[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

### 思路

* 本题考察图，本题使用广度优先搜索.
* 我们构建一个字典，值为当前课程，值为数组，list中包含当前课程结束接着可以上的课程.
* 我们维护一个数组，数组中的值为数组索引所对应课程需要多少个前驱课程，如list[4]=7,表示要上4号课程，之前要上节课程.
* 我们使用一个队列进行深度右边遍历，先遍历入度为0的课程，每次遍历一个课程就将该课程的下一个课程入度减一，同时检查下一个课程是否被减到了0，若是则将其添加到队列尾，进行下一次遍历.最后我们检查所有课程的入度，如果所有的课程入度都为0，说明所有的课程都已经上完，若不是则说明还有课程无法上完，我们返回False.

```python
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-21 12:05:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-21 20:26:27

from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses: return 0
        nextcourse, indegree = {}, [0] * numCourses
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
            # 下一次将要上的课程
            for _next in nextcourse.get(c, []):
                # 当前课程已经上了，下一节课入度减一
                indegree[_next] -= 1
                # 将新产生的入度为0的课程添加到队列中
                if not indegree[_next]: queue.append(_next)
        for item in indegree:
            if item: return False
        return True
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2019-01-21-207-Course-Schedule.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-207-course-schedule/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
