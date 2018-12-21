# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-21 11:18:38
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-21 14:26:43


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        # zero表示已经到达最终位置的0的下一个位置
        # nums[0:zero-1]之间的数字都是0，它们都已经到达了最终位置
        # one 表示已经到达最终位置的1的下一个位置
        # nums[zero:one-1]之间的数字都是1，它们都已经到达了最终位置
        zero, one, length = 0, 0, len(nums)
        # 只需要遍历一次
        for i in range(length):
            if nums[i] == 0:
                # 如果当前是0，则把当前位置的值置为nums[one],把nums[one]置为nums[zero]
                # 把nums[zero]置为0
                nums[i], nums[one], nums[zero] = nums[one], nums[zero], 0
                zero += 1
                one += 1
            # 如果当前位置是1，则把当前位置置为nums[one],把nums[one]置为0
            elif nums[i] == 1:
                nums[i], nums[one] = nums[one], 1
                one += 1


if __name__ == "__main__":
    so = Solution()
    nums = [2, 0]
    so.sortColors(nums)
    print(nums)
