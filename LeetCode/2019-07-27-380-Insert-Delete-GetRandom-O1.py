# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-27 13:59:36
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-27 14:24:11

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = dict()
        self.array = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index:
            return False
        self.index[val] = len(self.array)
        self.array.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.index:
            return False

        last_num = self.array[-1]
        val_index = self.index[val]

        self.index[val], self.index[last_num] = self.index[last_num], self.index[val]
        self.array[val_index] = self.array[-1]
        del self.index[val]
        del self.array[-1]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)
 