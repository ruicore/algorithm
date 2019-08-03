# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-08-03 10:48:30
# @Last Modified by:   何睿
# @Last Modified time: 2019-08-03 10:53:15

import copy
import random

from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.shuffle_ = nums
        self.original = copy.copy(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.shuffle_)
        return self.shuffle_
