# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-03 12:36:42
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-03 13:00:03


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


import json
from collections.abc import Iterable


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def deserialize(self, s: str):
        json_list = json.loads(s)

        def _deserialize(json_list):
            if isinstance(json_list, Iterable):
                nested = NestedInteger()
                for x in json_list:
                    nested.add(_deserialize(x))
                return nested
            else:
                return NestedInteger(json_list)

        return _deserialize(json_list)
