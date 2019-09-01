# LeetCode 399. Evaluate Division

## Description

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:

```py
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].
```

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

```py
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
```

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

## 描述

给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :

```py
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]
```

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

```py
equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
```

输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

* 这道题可以转换为图来做。
* a / b = 2,b / c= 3,则 a / c = a / b * b / c。
* 令给定的表达式的除数与被除数为两个节点，链接这两个节点边的权重为表达式的值（ a / b = 2 => 可以形成两条边：a --> b = 2.0,b --> a == 0.5）。
* 为了求的 a / c 的值，就是找一条路径从 a 到 c，然后把所有边的权重乘起来。
* 使用深度优先搜索，找到满足条件的任意一条路径即可。

```py
# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-09-01 12:45:54
# @Last Modified by:   何睿
# @Last Modified time: 2019-09-01 16:28:09

from typing import List
from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.__build_graph(equations, values)
        return list(map(lambda query: self.__query(graph, query[0], query[1], set()), queries))

    def __build_graph(self, equations, values):
        """
        构建图
        """
        graph = defaultdict(dict)
        for e, v in zip(equations, values):
            root, node = e
            graph[root][node] = v
            graph[node][root] = 1 / v

        return graph

    def __query(self, garph, start, end, visited):

        # 根据题中的描述，表达式中的字母必须出现在 equations 过
        # 因此 x / x 不能返回 1，因为 x 没有出现过
        if start not in garph and end not in garph:
            return -1.0
        if start == end:
            return 1.0

        visited.add(start)
        for next_ in garph[start]:
            if next_ in visited:
                continue
            tmp = self.__query(garph, next_, end, visited)
            if tmp > -1:
                return tmp * garph[start][next_]

        return -1
```
源代码文件在 [这里](https://github.com/ruicore/Algorithm/blob/master/LeetCode/2019-09-01-399-Evaluate-Division.py) 。
©本文首发于 何睿的博客 ，欢迎转载，转载需保留 [文章来源](https://ruicore.cn/leetcode-399-evaluate-division/) ，作者信息和本声明.
