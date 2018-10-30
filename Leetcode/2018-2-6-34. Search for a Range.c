#define _CRT_SECURE_NO_WARNINGS //去掉vs安全检查
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>

int* searchRange(int* nums, int numsSize, int target, int* returnSize) 
{
	int left = 0, right = numsSize-1, mid = 0;
	int* res = (int*)malloc(sizeof(int) * 2);

	while (left<=right)
	{
		mid = (left + right) >> 1;
		if (nums[mid] == target)
			break;
		if (nums[mid] < target)
			left = mid + 1;
		else
			right = mid - 1;
	}

	if (left <= right)
	{
		left = mid - 1;
		while (left >= 0 && nums[left] == nums[mid])
		{
			left--;
		}
		right = mid + 1;
		while (right < numsSize&&nums[right] == nums[mid])
		{
			right++;
		}
		res[0] = left + 1;
		res[1] = right - 1;
		*returnSize = 2;
		return res;
	}
	else
	{
		res[0] = -1;
		res[1] = -1;
		*returnSize = 2;
		return res;
	}

}

