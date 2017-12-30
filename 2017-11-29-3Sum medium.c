#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>

//Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0 ? Find all unique triplets in the array which gives the sum of zero.
//
//Note : The solution set must not contain duplicate triplets.
//
//	For example, given array S = [-1, 0, 1, 2, -1, -4],
//
//	A solution set is :
//[
//	[-1, 0, 1],
//	[-1, -1, 2]
//]

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
int** threeSum(int* nums, int numsSize, int* returnSize)
{
	int **result = NULL, **temp_result = NULL;
	int i = 0, j = 0, negative = 0, count = 0, left = 0, right = 0;
	int pos = 0;

	if (numsSize < 3)
	{
		*returnSize = 0;
		return NULL;
	}
		
	temp_result = (int**)malloc(sizeof(int*)*(numsSize*(numsSize-1)*(numsSize-2)/6));
	Insert_sort(nums,numsSize);
	for (i = 0; i < numsSize; i++)
	{
		left = i+1, right = numsSize - 1, negative = -nums[i];
		if (i&&nums[i] == nums[i - 1]) continue;
	
		while (left<right)
		{
			if (nums[left] + nums[right] < negative)
			{
				left++;
			}
			else if (nums[left] + nums[right] > negative)
			{
				right--;
			}
			else
			{
				temp_result[count] = (int*)malloc(sizeof(int) * 3);
				temp_result[count][0] = nums[i];
				temp_result[count][1] = nums[left];
				temp_result[count][2] = nums[right];
				left++;
				right--;
				count++;
			}
		}
	}
	if (count)
	{
		for (i = 0; i < count; i++)
			Insert_sort(temp_result[i], 3);
		result = (int**)malloc(sizeof(int*)*count);
		result[0] = (int*)malloc(sizeof(int) * 3);
		for (i = 0; i < 3; i++)
			result[0][i] = temp_result[0][i];
		*returnSize = 1;
		for (i = 1; i<count; i++)
		{
			if (temp_result[i][0] == result[pos][0] && temp_result[i][1] == result[pos][1] && temp_result[i][2] == result[pos][2])
				continue;
			else
			{
				pos++;
				(*returnSize)++;
				result[pos] = (int*)malloc(sizeof(int) * 3);
				for (j = 0; j < 3; j++)
					result[pos][j] = temp_result[i][j];
			}
		}
	}
	else
	{
		*returnSize = 0;
		result = NULL;
	}
	for (i = 0; i < count; i++)
		free(temp_result[i]);
	free(temp_result);

	return result;
}

int main()
{
	int nums[16] = { -1,0,1,2,-1,-4};
	int i = 0, j = 0, a = 0;
	int *returesize = &a;
	int **re = NULL;
	re=threeSum(nums, 6, returesize);
	for (i = 0; i < *returesize; i++)
	{
		for (j = 0; j < 3; j++)
			printf_s("%d ", re[i][j]);
		printf_s("\n");
	}

	system("pause");
	return 0;
}
