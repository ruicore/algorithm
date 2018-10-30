# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-08-30 20:12:18
# @Last Modified by:   何睿
# @Last Modified time: 2018-08-30 20:12:50


"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        length = len(digits)
        index = length-1
        last = digits[index]
        while last+1 == 10:
            result.insert(0, 0)
            index -= 1
            if index == -1:
                index += 1
                digits.insert(0, 0)
            last = digits[index]
        digits[index] += 1
        result = digits[:index+1]+result
        return result


if __name__ == "__main__":
    so = Solution()
    re = so.plusOne([9])
    print(re)
