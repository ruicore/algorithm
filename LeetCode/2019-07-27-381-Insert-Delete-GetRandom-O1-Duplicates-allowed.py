# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-07-27 15:43:51
# @Last Modified by:   何睿
# @Last Modified time: 2019-07-27 18:14:22

import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """

        index = self.index
        array = self.array
        iscontain = False

        if val not in index:
            index[val] = []
            iscontain = True

        last_index = len(index[val])
        index[val].append(len(array))
        array.append((val, last_index))

        return iscontain

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        index = self.index
        array = self.array

        if val not in index:
            return False

        val_last_index = index[val][-1]

        last_tuple = array[-1]
        last_index = last_tuple[1]
        last_num = last_tuple[0]

        array[val_last_index], array[-1] = array[-1], array[val_last_index]

        index[last_num][last_index] = val_last_index

        del array[-1]
        del index[val][-1]

        if not index[val]:
            del index[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.array)[0]
