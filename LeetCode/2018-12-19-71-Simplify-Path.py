# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-19 16:29:44
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-19 16:43:47


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return None
        path = path.split("/")
        stack = []
        for item in path:
            if not item or item == '.':
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return '/'+'/'.join(stack)

if __name__ == "__main__":
    so = Solution()
    a  = "/../"
    res = so.simplifyPath(a)
    print(res)