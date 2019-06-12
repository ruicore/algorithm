# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-22 17:55:43
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 10:35:05


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果是空则返回0
        if not nums:
            return 0
        index, count = 1, 1
        for i in range(1, len(nums)):
            # 如果两个字符相等
            if nums[i-1] == nums[i]:
                # count计数自增一次
                count += 1
            # 如果不等，count重置为1
            else:
                count = 1
            # 如果count小于等于2，则把nums[i]放到有效位置的后一个位置
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        # 删除无用元素[也可不用删除，LeetCode不会检查后面的元素]
        del nums[index:]
        return index


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    so = Solution()
    res = so.removeDuplicates(nums)
    print(res, nums)
