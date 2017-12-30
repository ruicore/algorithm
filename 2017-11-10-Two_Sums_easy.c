#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>


//Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//
//You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
//Example:
//Given nums = [2, 7, 11, 15], target = 9,
//
//Because nums[0] + nums[1] = 2 + 7 = 9,
//return[0, 1]



int* twoSum(int* nums, int numsSize, int target) 
{
	int temp = 0;
	int i = 0, j = 0;
	int* numstemp = (int *)malloc(sizeof(int)*numsSize);
	int min = 0, max = numsSize - 1;
	int *result = (int*)malloc(sizeof(int) * 2);
	int serath = 0;

	for (i = 0; i < numsSize; i++)
		numstemp[i] = nums[i];

	for (i = 1; i<numsSize; i++)
		for (j = i; j >0; j--)
		{
			if (numstemp[j] < numstemp[j - 1])
			{
				temp = numstemp[j];
				numstemp[j] = numstemp[j - 1];
				numstemp[j - 1] = temp;
				continue;
			}
			break;
		}

	do
	{
		if ((numstemp[min] + numstemp[max]) > target)
			max--;
		else if ((numstemp[min] + numstemp[max]) < target)
			min++;
		else
			break;
	} while (target-(numstemp[min]+numstemp[max]));

	for (i = 0; i < numsSize; i++)
	{
		if (numstemp[min] == nums[i])
		{
			result[0] = i;
			serath = i;
			break;
		}
		
	}

	if (numstemp[min] - numstemp[max])
	{
		for (i = 0; i < numsSize; i++)
		{
			if (numstemp[max] == nums[i])
			{
				result[1] = i;
				break;
			}
		}
	}
	else
	{
		for (i = serath+1; i < numsSize; i++)
		{
			if (numstemp[max] == nums[i])
			{
				result[1] = i;
				break;
			}
		}
	}
	
	return result;
}


int main()
{
	int p[2] = { 3, 3 };
	int *resut=twoSum(p, 2, 6);
	
	printf_s("%d + %d = %d", resut[0], resut[1], 26);

	system("pause");
}
