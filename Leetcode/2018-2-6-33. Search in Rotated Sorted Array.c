#define _CRT_SECURE_NO_WARNINGS //去掉vs安全检查
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>

int search(int* nums, int numsSize, int target) 
{
	int mid = 0, left = 0, right = 0;
	int i = 0;

	if (numsSize == 0)
		return -1;

	if (numsSize == 1)
	{
		if (target == nums[0])
			return 0;
		else
			return -1;
	}

	left = 0;
	right = numsSize - 1;

	while (left<=right)
	{
		mid = (left + right) / 2;

		if (nums[mid] == target)
			return mid;
		else if (nums[mid] < nums[right])//如果右边是递增区间
		{
			if (target > nums[mid] && target <= nums[right])//如果目标值在递增区间内
				left = mid + 1;
			else
				right = mid - 1;//如果目标值不再递增区间内
		}
		else//如果左边是递增区间
		{
			if (target >= nums[left] && target < nums[mid])
			{
				right = mid - 1;
			}
			else
				left = mid + 1;
		}
	}

	return -1;
}

