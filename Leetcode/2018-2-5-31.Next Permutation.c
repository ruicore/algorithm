#define _CRT_SECURE_NO_WARNINGS //去掉vs安全检查
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>

void nextPermutation(int* nums, int numsSize) 
{
	int i = 0, tmp = nums[numsSize - 1], pos = numsSize-2;
	int left = 0, right = 0;
	int pos_small = 0;
	
	while (tmp<=nums[pos])//找到不是依次增长的数
	{
		tmp = nums[pos];
		pos--;
	}
	if (pos == -1)
	{
		left = 0, right = numsSize - 1;
		while (left<right)
		{
			tmp = nums[left];
			nums[left] = nums[right];
			nums[right] = tmp;
			left++;
			right--;
		}
	}
	else
	{
		pos_small = pos + 1;
		while (nums[pos_small] > nums[pos] && pos_small < numsSize)
		{
			pos_small++;
		}
		pos_small--;

		tmp = nums[pos];
		nums[pos] = nums[pos_small];
		nums[pos_small] = tmp;

		left = pos + 1;
		right = numsSize - 1;
		while (left<right)
		{
			tmp = nums[left];
			nums[left] = nums[right];
			nums[right] = tmp;
			left++;
			right--;
		}
	}
}

int main()
{
	int nums[10] = { 6,5,4,3,2,1 };
	nextPermutation(nums, 6);
	for (int i = 0; i < 6; i++)
	{
		printf_s("%d ", nums[i]);
	}
	system("pause");
}

