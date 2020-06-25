#define _CRT_SECURE_NO_WARNINGS //去掉vs安全检查
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>

int searchInsert(int* nums, int numsSize, int target) 
{
	int left = 0, right = numsSize - 1, mid = 0;

	while (left<=right)
	{
		mid = (left + right) / 2;
		if (nums[mid] == target)
			return mid;
		if (nums[mid] > target)
			right = mid - 1;
		else
		{
			left = mid + 1;
		}
	}
	
	return left;
}