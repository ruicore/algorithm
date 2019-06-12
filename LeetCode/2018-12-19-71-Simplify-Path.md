# LeetCode 71. Simplify Path

## Description

Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look [here](https://en.wikipedia.org/wiki/Path_(computing)#Unix_style).

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

## 描述

给定文件的绝对路径（Unix下的路径）字符串，简化此字符串。

举例:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

在UNIX的文件系统中，英文句点（'.'）表示当前目录，因此在简化绝对路径时可以忽略它。 并且，一个双英文句点（".."）表示向上移动一个目录，因此返回了双句点前面的路径。 有关Unix系统文件路径的更多信息，请移步[这里](https://en.wikipedia.org/wiki/Path_(computing)#Unix_style).

### 思路

* 这道题目主要使用了[栈](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))这种数据结构.
* 我们首先拆分字符串，以"/"为拆分依据(python中可以直接使用拆分函数).
* 我们声明一个数组形式的栈stack,然后我们依次检查每一个元素.
1. 如果当前位置是".",则什么也不做.
2. 如果当前位置是"..",从stack中pop出一个元素(如果stack中有数据，如果没有，什么也不做)
3. 如果不是以上两种情况，把当前元素压入栈.
4. 最后以"/"为连接元素，把栈中的所有元素连接成一个字符串.

```python
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 如果path为空，返回Nonoe
        if not path:
            return None
        # 以"/"拆分字符串
        path = path.split("/")
        # 声明一个空栈
        stack = []
        # 依次检查每一个元素
        for item in path:
            # 这里使用的是python3自带的拆分函数，会返回空值，所以需要判断一下
            # 如果是空值或者"."则什么也不做
            if not item or item == '.':
                continue
            # 如果是".."
            elif item == "..":
                # 如果栈不空，则弹出栈顶元素
                if stack:
                    stack.pop()
            # 如果不为空，不是".",不是".."则压入栈
            else:
                stack.append(item)
        # 用"/"连接所有元素，返回
        return '/'+'/'.join(stack)
```

源代码文件在[这里](https://github.com/ruicore/Algorithm/blob/master/Leetcode/2018-12-19-71-Simplify-Path.py).
©本文首发于[何睿的博客](https://www.ruicore.cn/leetcode-71-simplify-path/)，欢迎转载，转载需保留文章来源，作者信息和本声明.
