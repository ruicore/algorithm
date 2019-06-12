# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-23 11:15:08
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 16:13:18


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left, right, middle = 0, len(nums)-1, 0
        # 循环条件，只有当left小于等于right时，循环才执行
        while left <= right:
            # 从左边开始，找到连续相等的数字的最后一个值
            while left < right and nums[left] == nums[left+1]:
                left += 1
            # 从右边开始，找到连续相等的数字的第一个值
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            # 取中间值
            middle = left+((right-left) >> 1)
            print(left, right, middle)
            # 如果中间值和要找的值相等，则返回Ture
            if nums[middle] == target:
                return True
            # 如果左边的数字是连续的
            elif nums[left] <= nums[middle]:
                # 如果target在连续的区间之内
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # 如果右边的区间是连续的
            elif nums[middle] < nums[right]:
                # 如果target在连续的区间之内
                if nums[middle] < target <= nums[right]:
                    left = middle+1
                else:
                    right = middle-1
        return False


if __name__ == "__main__":
    so = Solution()
    res = so.search(nums=[3, 1], target=0)
    print(res)
