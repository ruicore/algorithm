#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>
#include <limits.h>



//16. 3Sum Closest
//Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.Return the sum of the three integers.You may assume that each input would have exactly one solution.
//
//For example, given array S = { -1 2 1 - 4 }, and target = 1.
//
//The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

void Insert_sort(int *nums, int numSize)
{
	int i = 0, j = 0;
	int temp = 0;

	for (i = 1; i < numSize; i++)
	{
		for (j = i; j > 0; j--)
		{
			if (nums[j] < nums[j - 1])
			{
				temp = nums[j - 1];
				nums[j - 1] = nums[j];
				nums[j] = temp;
			}
			else
			{
				break;
			}
		}
	}

	return;
}
int threeSumClosest(int* nums, int numsSize, int target) 
{
	int i = 0, j = 0, left = 0, right = 0, diff = INT_MAX, temp_sum=0,temp_diff = 0, resu_target = 0;
	Insert_sort(nums, numsSize);
	
	if (numsSize <= 3)
	{
		for (i = 0; i < numsSize; i++)
			resu_target += nums[i];
		return resu_target;
	}
	else
	{
		for (i = 0; i < numsSize - 2; i++)
		{
			left = i + 1, right = numsSize - 1;
			while (left<right)
			{
				temp_sum = nums[left] + nums[right] + nums[i];
				temp_diff = abs(temp_sum - target);
				if (temp_diff < diff)
				{
					diff = temp_diff;
					resu_target = temp_sum;
				}
				if (temp_sum < target)
					left++;
				else if (temp_sum > target)
					right--;
				else
					return temp_sum;	
			}
		}
	}
	
	return resu_target;
}


int main()
{
	int a[4] = { 0,2,1,-3 };
	printf_s("%d", threeSumClosest(a, 4, 1));
	system("pause");

	return 0;
}
